from rivuletpy.utils.io import *
from rivuletpy.trace import *
import numpy as np
import os, math
# crop_region=np.shape()
# inputpath="/home/vv/Desktop/new/1"
# img=loadimg(inputpath)
# import numpy as np
# stack = []
# sample1=np.arange(-1,-17,-1).reshape(4,4)
# print(sample1)
# print(sample1[-1,-1])
# print(sample1[-1,-2])
# sample2=np.arange(1,37).reshape((3,4,3))
# bis = sample1 > 3
# x = np.array([1, 2, 3, 4])
# y =x > 2
# z=y.astype(int)
# print("int",z)
#
# print(sample1[2,2,2])
# print(sample1)
# print(sample2)
# stack.append(np.rot90(np.fliplr(np.flipud(sample1))))
# print(stack)
# stack.append(np.rot90(np.fliplr(np.flipud(sample2))))
# print(stack)
# out = np.dstack(stack)
# print("out begins")
# print(out)
# def combined(directory):
#     combined[]=loadtiff3d(directory)
# a=str(math.ceil(9.3))
# print(a)

# print("xmax:"+str(xmax))
# ymax=ys[-1]
# for file in list:  # 遍历文件夹
#     if not os.path.isdir(file):
#         print(file)
# a=loadimg(inputpath+"/"+"1_1"+".tif")
# print(a)
# print(a.dtype)
# list = os.listdir(inputpath)# 得到文件夹下的所有文件名称
# coordilist=[]
# for l in list:
#     location = l.split(".")[0]
#     x = int(location.split("_")[0])
#     y = int(location.split("_")[1])
#     coordilist.append([x,y])
# coordilist.sort(key=lambda k: [k[0], k[1]])
# print(coordilist[-1])
# list = os.listdir(directory) # dir is your directory path
# xs=[]
# ys=[]
# for l in list:
#     location=l.split(".")[0]
#     x=location.split("_")[0]
#     y=location.split("_")[1]
#     xs.append(int(x))
#     ys.append(int(y))
# xs.sort()
# ys.sort()
# xmax=xs[-1]
# ymax=ys[-1]
# for ylocation in range(1,ymax+1):
#     #every line combined
#     line=loadimg(directory+"/1_"+str(ylocation)+".tif")
#     for xlocation in range(2,xmax+1):
#         debris=loadimg(directory+"/"+str(xlocation)+"_"+str(ylocation)+".tif")
#         # print(str(xlocation)+"_"+str(ylocation),debris.shape)
#         line=np.concatenate((line, debris), axis=1)
#     if(ylocation==1):
#         wholepart=line
#         print(wholepart)
#     else:
#         wholepart=np.concatenate((wholepart,line),axis=0)
# writetiff3d(directory+"/wholepart.tif",wholepart)
# kong=[[[]]]
# a=np.ones((2,3,2))
# c=np.concatenate((kong,a),axis=2)
# print(c)
# def ratio(threshold,darray):
#     x,y,z=darray.shape
#     binsum=(darray>threshold).sum()
#     ratio=binsum/(x*y*z)
# def am_i_wrong(answer):
#     if answer == 'yes':
#         return True
#     else:
#         return False
# a=am_i_wrong('yes')
# print(a)
# class getinfo:
#     def __init__(self,name,thresholdt,pctg,crop_region=None,bi_matrix=None,thresholdbi=None,swc=None):
#         self.name=name
#         self.matrix_3d=None
#         self.pctg=pctg
#         self.bi_ratio=0
#         self.bi_matrix=None
#         self.threshodbi=0
#         self.thresholdt=thresholdt
#         self.tracelabel=False
#         self.swc = None
#     def get3d_mat(self):
#         self.matrix_3d=loadimg('/home/vv/Desktop/new/1/'+self.name+'.tif')
#         return self.matrix_3d
#     def cellsatisfied(self):
#         oneitem=loadimg('/home/vv/Desktop/new/1/'+self.name+'.tif')
#         self.bi_matrix=(oneitem>self.thresholdt).astype(int)
#         self.bi_ratio=float((oneitem > self.thresholdt).sum()/(oneitem.shape[0]*oneitem.shape[1]*oneitem.shape[2]))
#         return self.thresholdt, self.bi_matrix, self.bi_ratio
#     def traceornot(self):
#         if self.bi_ratio>self.pctg:
#             self.tracelabel=True
#         return self.tracelabel
#     def gettrace(self):
#         if self.tracelabel:
#             # Run rivulet2 for the first time
#             tracer = R2Tracer()
#             self.swc, soma = tracer.trace(self.matrix_3d, self.thresholdt)
#
#             tswc=self.swc._data.copy()
#             # print(self.swc._data.shape)
#             tswc[:, 2] += self.cropy  以2_3举例，横坐标加上cropx×截取的y-1（3），纵坐标加上cropy×截取的x-1(2）
#             tswc[:, 3] +=
#             self.swc._data = tswc
#             self.swc.save('/home/vv/Desktop/new/1/'+self.name+'.swc')
#         return self.swc._data
#     # def doall(self):
#
#
#
#
#
#
#
# xxx = getinfo('1_1_40_50',10,0.000000005)
# print(xxx.get3d_mat())
# print(xxx.cellsatisfied())
# print(xxx.traceornot())
# print(xxx.pctg,xxx.bi_ratio)
# print(xxx.gettrace())


# def reset(self, crop_region, zoom_factor):
#     '''
#     Pad and rescale swc back to the original space
#     '''
#
#     tswc = self._data.copy()
#     if zoom_factor != 1.:  # Pad the swc back to original space
#         tswc[:, 2:5] *= 1. / zoom_factor
#
#     # Pad the swc back
#     tswc[:, 2] += crop_region[0, 0]
#     tswc[:, 3] += crop_region[1, 0]
#     tswc[:, 4] += crop_region[2, 0]
#     self._data = tswc
# a=loadswc('/home/vv/Desktop/new/1.r2.swc')
# b=loadswc('/home/vv/Desktop/new/1/1_1.swc')
# print(a.shape)
# # print(a[1333,0:5]) 从1333开始出现断点,把所有小的swc文件拼合在一起数量大于大文件的行数
# print(b.shape)
# # print(b[44:66,2:5])

# all = os.listdir('/home/vv/Desktop/new/1_100_90')
# for a in all:
#     if "_" in a:
#         print(a)
# print(all)

# file=open('/home/vv/Desktop/new/1_100_90/txt/100_90.txt','r')
# for line in file:
#     if "_" in line:
#         print(line)
#0818 this version is for fileinfo first version
# from rivuletpy.utils.io import *
# import os, glob
# inputpath="/home/vv/Desktop/new/1.tif"
# img=loadimg(inputpath)
# dirpath=inputpath.split(".")[0]
#
#
# def cropimg(cropx,cropy,threshold,img):
#     #The savefile consists of cropx_cropy eg: 2_3.tif
#     savepath = dirpath + "_"+str(cropx)+"_"+str(cropy)+"/"
#     os.mkdir(savepath)
#     os.mkdir(savepath + "txt")
#     locinfo=""
#     locfile = open(savepath + "txt/"+str(cropx)+"_"+str(cropy)+".txt", "w")
#     x,y,z=img.shape
#     # print(x,y,z)
#     for i in range(cropy,y,cropy):
#         #The output of every line
#         for j in range(cropx,x,cropx):
#             oneitem=img[j-cropx:j,i-cropy:i,:]
#             loc=str(int(i/cropy))+"_"+str(int(j/cropx))
#             locinfo=locinfo+"\n"+loc
#             writetiff3d(savepath+loc+".tif", oneitem)
#         #if there is one left at the end of the line, here it is
#         if(x%cropx!=0):
#             linelast=img[x-x%cropx:x,i-cropy:i,:]
#             loc=str(int(i/cropy)) +"_"+ str(int(j/cropx+1))
#             locinfo=locinfo+"\n"+loc
#             writetiff3d(savepath + loc +
#                         ".tif", linelast)
#     # print("final line begins")
#     if(y%cropy!=0):
#         for k in range(cropx,x,cropx):
#             lastline=img[k-cropx:k,y-y%cropy:y,:]
#             loc=str(int(i/cropy+1)) + "_"+str(int(k/cropx))
#             locinfo = locinfo+"\n"+loc
#             writetiff3d(savepath + loc +
#                         ".tif", lastline)
#     #行列均有剩的最后一个
#     # print("lucky last one")
#     if((y%cropy!=0)and(x%cropx!=0)):
#         lastone=(img[x-x%cropx:x,y-y%cropy:y,:])
#         loc=str(int(i/cropy+1)) +"_"+ str(int(j/cropx+1))
#         locinfo = locinfo+"\n"+loc
#         writetiff3d(savepath + loc
#                     +".tif", lastone)
#     locfile.write(locinfo)
#     locfile.close()
#
# def combined(directory):
#     file = open(directory+"/txt/", 'r')
#     for line in file:
#         if "_" in line:
#             line = line.split('\n')[0]
#     xmax=int(line.split('_')[0])
#     ymax=int(line.split('_')[1])
#     rest=".tif"
#
#     for ylocation in range(1, ymax + 1):
#         # every same x in y direction combined
#         liney = loadimg(directory + "/1_" + str(ylocation) + rest)
#         for xlocation in range(2, xmax + 1):
#             debris = loadimg(directory + "/" + str(xlocation) + "_" + str(ylocation) + rest)
#             liney = np.concatenate((liney, debris), axis=1)
#         #every x direction combined to get the final one part
#         if (ylocation == 1):
#             wholepart = liney
#             print(wholepart)
#         else:
#             wholepart = np.concatenate((wholepart, liney), axis=0)
#     writetiff3d(directory + "/wholepart.tif",wholepart)
# cropimg(100,90,10,img)
# combined("/home/vv/Desktop/new/1_100_90")
import glob
for txt in glob.glob(os.path.join("/home/vv/Desktop/new/1_100_90/txt", '*.txt')):
    file=open(txt,'r')
    for line in file:
        print(line)







