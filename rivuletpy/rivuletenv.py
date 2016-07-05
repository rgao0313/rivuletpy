import gym
from gym import spaces
from gym.utils import seeding

from .utils.io import *
from .utils import rendering3
from .utils.backtrack import *
from .utils.preprocessing import rivulet_preprocessing
from .stalkers import DandelionStalker

import os
from matplotlib import pyplot as plt
import numpy
from numpy import pi
from euclid import * 

class RivuletEnv(gym.Env):
    metadata = {'render.modes': ['human', 'rgb_array']}


    def __init__(self, **userconfig):
        self.config = {'imgpath': 'test-small.tif', 'swcpath':'test-small.swc','length': 5,
                       'coverage': 0.98, 'threshold': 0,
                       'render': False, 'cached': True, 'nsonar': 30, 'gap': 8,
                       'raylength': 8}
        self.config.update(userconfig)
        self.viewer = None
        self._dt, self._t, self._ginterp, self._bimg, cropregion = rivulet_preprocessing(self.config['imgpath'], self.config)

        spt = np.asarray(np.unravel_index(self._dt.argmax(), self._dt.shape))
        self._somapt = Point3(spt[0], spt[1], spt[2])

        swc = loadswc(self.config['swcpath'])
        for n in swc: # cropswc
            n[2] -= cropregion[1, 0]
            n[3] -= cropregion[0, 0]
            n[4] -= cropregion[2, 0]    
        self._swc = swc

        # Action Space 
        # low = np.array([-2*pi, -2*pi, -2*pi, 0]) # For RotStalker
        # high = np.array([2*pi, 2*pi, 2*pi, 3])
        low = np.array([-1, -1, -1, 0]) # For DandelionStalker 
        high = np.array([1, 1, 1, 0.5])
        self.action_space = spaces.Box(low, high)

        self.obs_dim = self.config['nsonar'] + 4
        high = np.array([1.0] * self.obs_dim)
        low = np.array([-self.config['raylength']] * self.obs_dim)
        self.observation_space = spaces.Box(low, high)


    def _reset(self):
        # Reinit dt map
        self._rewardmap = self._dt.copy()
        self._tt = self._t.copy() # For selecting the furthest foreground point
        self._tt[self._bimg==0] = -2
        maxtpt = np.asarray(np.unravel_index(self._tt.argmax(), self._tt.shape))
        self._stalker = DandelionStalker(Point3(maxtpt[0], maxtpt[1], maxtpt[2]), nsonar=self.config['nsonar'], raylength=self.config['raylength'])
        self._erase(self._stalker.pos)
        return np.append(self._stalker.sample(self._bimg), [0.,0.,0.,0.])


    def _erase(self, pos):
        posx, posy, posz = [int(np.asscalar(v)) for v in np.floor(self._stalker.pos.xyz)]
        r = getradius(self._bimg, posx, posy, posz)
        self._rewardmap[max(posx-r, 0) : min(posx+r+1, self._tt.shape[0]),
                        max(posy-r, 0) : min(posy+r+1, self._tt.shape[1]), 
                        max(posz-r, 0) : min(posz+r+1, self._tt.shape[2])] = -1
        self._tt[max(posx-r, 0) : min(posx+r+1, self._tt.shape[0]),
                 max(posy-r, 0) : min(posy+r+1, self._tt.shape[1]), 
                 max(posz-r, 0) : min(posz+r+1, self._tt.shape[2])] = -1


    def _step(self, action):
        done = False
        ob, pos = self._stalker.step(action, self._rewardmap)
        posx, posy, posz = [int(np.asscalar(v)) for v in np.floor(pos.xyz)]
        reward = self._rewardmap[posx, posy, posz]
        repeat = self._tt[posx, posy, posz] == -1 # It steps on a voxel which has been explored before

        # Erase the current block stalker stays from reward map with the radius estimated from bimg
        self._erase(self._stalker.pos)

        # Check a few crieria to see if reinitialise stalker
        notmoving = len(self._stalker.path) >= 30 and np.linalg.norm(self._stalker.path[-30] - self._stalker.pos) <= 1 
        close2soma = self._stalker.pos.distance(self._somapt) < self._dt.max()
        largegap = len(self._stalker.path) > self.config['gap'] 
        pathvoxsum = np.array([self._bimg[math.floor(p.x), 
                               math.floor(p.y), 
                               math.floor(p.z)] for p in self._stalker.path[-self.config['gap']:] ]).sum()
        largegap = largegap and pathvoxsum == 0
        outofbound = not inbound(pos.xyz, self._rewardmap.shape)

        # Place stalker at the current geodesic furthest point
        if notmoving or largegap or outofbound or repeat:
            maxtpt = np.asarray(np.unravel_index(self._tt.argmax(), self._tt.shape))
            self._stalker.pos.x, self._stalker.pos.y, self._stalker.pos.z = maxtpt
            self._erase(self._stalker.pos)
            self._stalker.path = []

        if close2soma:
            # print('close2soma:\t', close2soma)
            done = True

        assert ob.size == self.obs_dim

        return ob, reward, done, {}


    def _render(self, mode='human', close=False):
        if self.viewer is None:
            bounds = self._swc[:, 2:5].max(axis=0) * 4
            bounds = np.floor(bounds).astype('int16')
            self.viewer = rendering3.Viewer3(800, 800, 800)
            self.viewer.set_bounds(0, bounds[0], 0, bounds[1], 0, bounds[2])

            ids = [node[0] for node in self._swc]
            for node in self._swc:
                # draw a line between this node and its parents when its parent exists 
                if node[6] in ids:
                    parent = next(parent for parent in self._swc if node[6] == parent[0])
                    line = rendering3.Line3((node[2], node[3], node[4]), (parent[2], parent[3], parent[4]))
                    line.set_color(1,0,0)
                    line.set_line_width(2)
                    self.viewer.add_geom(line)

        # Draw stalker
        self._stalker.render(self.viewer)

        return self.viewer.render(return_rgb_array = mode=='rgb_array')

    def _close(self):
        pass

    def _configure(self):
        pass

    def _seed(self, seed):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]



