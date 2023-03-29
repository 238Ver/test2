import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图
import random
import ast
import io
from io import BytesIO
from io import StringIO
# import ByteIO
import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import resp
from pylab import mpl
import os
import pickle
import PIL

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为微软雅黑
plt.rcParams['axes.unicode_minus'] = False

# x x轴 自变量，但是是竖着的
x = np.linspace(-100, 100, 10000)
# y1 y1 是一个三次函数

# path = "D:\ChangAn\数据整理\无图数据\\0822\lines"  # 待读取的文件夹,需要每次都进行设置
path = "D:\ChangAn\数据整理\有图数据\\lines"  # 待读取的文件夹,需要每次都进行设置

path_list = os.listdir(path)

def rotate(x, y, origin=(0, 0)):
    # shift to origin
    x1 = x - origin[0]
    y1 = y - origin[1]

    # rotate
    x2 = -y1
    y2 = x1

    # shift back
    x3 = x2 + origin[1]
    y3 = y2 + origin[0]
    return x3, y3

def K_means(data, K):
    """
    程序说明：
    本函数实现二维和三维数据的K_means聚类算法
    data:输入的数据，维度(m, 2)或者(m, 3)
    K:表示希望分出来的类数
    """
    num = np.shape(data)[0]

    cls = np.zeros([num], np.int)

    random_array = np.random.random(size=k)
    random_array = np.floor(random_array * num)
    rarray = random_array.astype(int)
    print('数据集中随机索引', rarray)

    center_point = data[rarray]
    print('初始化随机中心点', center_point)

    change = True  # change表示簇中心是否有过改变，又改变了就需要继续循环程序，没改变则终止程序
    while change:
        for i in range(num):
            temp = data[i] - center_point  # 此句执行之后得到的是两个数或三个数：x-x_0,y-y_0或x-x_0, y-y_0, z-z_0
            temp = np.square(temp)  # 得到(x-x_0)^2等
            distance = np.sum(temp, axis=1)  # 按行相加，得到第i个样本与所有center point的距离
            cls[i] = np.argmin(distance)  # 取得与该样本距离最近的center point的下标
        change = False
        for i in range(k):
            # 找到属于该类的所有样本
            club = data[cls == i]
            newcenter = np.mean(club, axis=0)  # 按列求和，计算出新的中心点
            ss = np.abs(center_point[i] - newcenter)  # 如果新旧center的差距很小，看做他们相等，否则更新之。run置true，再来一次循环
            if np.sum(ss.all(), axis=0) > 1e-4:
                center_point[i] = newcenter
                change = True
    print('K-means done!')
    return center_point, cls


"""
补充一点说明:我们下面左图的代码show_picture函数需要用到的cls，
其实就是一个[1, num]的矩阵，里面的元素就是对应第i个样本所属聚类中心的下标
放在第一个for循环的后面：cls[i] = np.argmin(distance)
因为如果第一个for循环得到的聚类已经是最终结果，那么它也不会执行后面的中心点更新的代码了
"""


def show_picture(data, center_point, cls, k):
    num, dim = data.shape
    color = ['r', 'g', 'b', 'c', 'y', 'm', 'k']
    if dim == 2:
        for i in range(num):
            mark = int(cls[i])
            plt.plot(data[i, 0], data[i, 1], color[mark] + 'o')

        # 下面把中心点单独标记出来：
        for i in range(k):
            plt.plot(center_point[i, 0], center_point[i, 1], color[i] + 'x')

    elif dim == 3:
        ax = plt.subplot(111, projection='3d')
        for i in range(num):
            mark = int(cls[i])
            ax.scatter(data[i, 0], data[i, 1], data[i, 2], c=color[mark])

        for i in range(k):
            ax.scatter(center_point[i, 0], center_point[i, 1], center_point[i, 2], c=color[i], marker='x')
    plt.show()


k=6 ##分类个数
z_MF = []
yl_OSNR = []
pn = np.random.normal(0, 10, 6400)

for i in range(6400):
  index_y = random.uniform(15,30)
  index_z = random.randint(0,3)
  z_MF.append(index_z)
  yl_OSNR.append(index_y)

pn = pn[:, np.newaxis]
#print(pn)

y = np.array(yl_OSNR)
y = y[:,np.newaxis]
#print(y)

z_MF = np.array(z_MF)
z = z_MF[:,np.newaxis]

temp = np.hstack((pn, y))
temp = np.hstack((temp, z))
# print(data.shape)
center_point,  cls = K_means(temp, k)

show_picture(temp, center_point, cls, k)


# for item, i in enumerate(path_list):
#     # path_export = "D:\\ChangAn\\drawing\\Lines\\0822\\" + str(item) + ".mp4"
#     path_export = "D:\\ChangAn\\drawing\\Lines\\有图数据\\" + str(item) + ".mp4"
#     current_path = path + "\\" + i
#     # size = (700,330)
#     size = (960,540)
#     fps = 20
#     print(current_path + "------------")
#     with open(current_path, 'rb') as f:
#          p = pickle.load(f)
#     video = cv2.VideoWriter(os.path.join('r', path_export), cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
#                             fps,size)
#     for item , num in enumerate(p):
#         # print(str(num[0]['curve_parameter_a0']) + "  " +str(num[0]['curve_parameter_a1']) +
#         #       "  " +str(num[0]['curve_parameter_a2'])+ "  " +str(num[0]['curve_parameter_a3']))
#         fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 5.4))
#         for j in range(len(num)):
#             if num[j]['curve_parameter_a0']!= 0 and num[j]['curve_parameter_a1']!=0 and num[j]['curve_parameter_a2']!=0 and num[j]['curve_parameter_a3']!=0 :
#                 a0 = num[j]['curve_parameter_a0']
#                 a1 = num[j]['curve_parameter_a1']
#                 a2 = num[j]['curve_parameter_a2']
#                 a3 = num[j]['curve_parameter_a3']
#                 y1 = a3 * x ** 3 + a2 * x ** 2 + a1 * x + a0
#                 #旋转操作
#                 origin = (0., 0)
#                 X1, Y1 = rotate(x, y1, origin)
#                 # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.3))
#                 ax1.set_title("原始图像")
#                 ax1.scatter(x, y1, color="blue", marker='o', s=10)
#                 ax1.plot(x, y1, 'r-')
#                 ax1.plot(0 , 0,marker = 'v')
#                 # ax1.plot(x, Y2 ,'r-')
#                 ax2.set_title(u"逆时针旋转90°图像")
#                 ax2.scatter(X1, Y1, color="blue", marker='o', s=20)
#                 ax2.plot(X1, Y1, 'r-')
#                 ax2.plot(0, 0, marker='v')
#                 # plt.show()
#                 # print(fig)
#         buffer = io.BytesIO()  #申请内存缓存空间
#         plt.savefig(buffer,format='png')
#         buffer.seek(0)
#         dataPIL = PIL.Image.open(buffer).convert('RGB')
#         data = np.asarray(dataPIL)
#
#         y = np.array(yl_OSNR)
#         y = y[:, np.newaxis]
#         # print(y)
#
#         z_MF = np.array(z_MF)
#         z = z_MF[:, np.newaxis]
#
#         temp = np.hstack((pn, y))
#         # data = np.hstack((temp, z))
#         # print(data.shape)
#         center_point, cls = K_means(data, k)
#
#         show_picture(data, center_point, cls, k)