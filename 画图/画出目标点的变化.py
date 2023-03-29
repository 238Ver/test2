import ast
import io
from io import BytesIO
from io import StringIO
# import ByteIO
import cv2
import matplotlib

# matplotlib.use('TkAgg')
matplotlib.use('Agg')
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

# path = "D:\ChangAn\数据整理\无图数据\\0822\json_objs"  # 待读取的文件夹,需要每次都进行设置
path = "D:\ChangAn\数据整理\有图数据\\json_objs"  # 待读取的文件夹,需要每次都进行设置

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


for item, i in enumerate(path_list):
    # path_export = "D:\\ChangAn\\drawing\\objs\\0822\\" + str(item) + ".mp4"
    path_export = "D:\\ChangAn\\drawing\\objs\\有图数据\\" + str(item) + ".mp4"
    current_path = path + "\\" + i
    # size = (700,330)
    size = (960, 540)
    fps = 20
    base_x = 0
    base_y = 0
    print(current_path + "------------")
    with open(current_path, 'rb') as f:
        p = pickle.load(f)
    video = cv2.VideoWriter(os.path.join('r', path_export), cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                            fps, size)
    for item, num in enumerate(p):
        # print(str(num[0]['curve_parameter_a0']) + "  " +str(num[0]['curve_parameter_a1']) +
        #       "  " +str(num[0]['curve_parameter_a2'])+ "  " +str(num[0]['curve_parameter_a3']))
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 5.4))
        # for j in range(len(num)):
        for j_item, j in enumerate(num):
            # if num[j]['curve_parameter_a0']!= 0 and num[j]['curve_parameter_a1']!=0 and num[j]['curve_parameter_a2']!=0 and num[j]['curve_parameter_a3']!=0 :
            if j['longitudinal_distance'] != 0 and j['lateral_distance'] != 0:
                y1 = j['lateral_distance'] + base_y
                # 旋转操作
                origin = (0., 0)
                x = j['longitudinal_distance'] + base_x
                X1, Y1 = rotate(x, y1, origin)
                # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.3))
                ax1.set_title("原始图像")
                ax2.plot(j['longitudinal_distance'] + base_x, j['lateral_distance'] + base_y, marker='v', color="black")
                ax1.scatter(x, y1, color="blue", marker='o', s=10)

                ax1.plot(x, y1, 'r-')
                ax1.plot(0, 0, marker='v')
                # ax1.plot(x, Y2 ,'r-')
                ax2.set_title(u"逆时针旋转90°图像")
                ax2.scatter(X1, Y1, color="blue", marker='o', s=20)
                ax2.plot(X1, Y1, 'r-')
                ax2.plot(0, 0, marker='v')
                # plt.show()
                # print(fig)
        buffer = io.BytesIO()  # 申请内存缓存空间
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        dataPIL = PIL.Image.open(buffer).convert('RGB')
        data = np.asarray(dataPIL)
        # cv2.imshow("image", data)
        # cv2.waitKey(0)
        #  for ni in range(10):
        #      for nj in range(10):
        #          np.delete(data[ni][nj], 3, axis=0)
        video.write(data)
        buffer.close()  # 释放缓存
        # print(data.shape)
        # print(video)
        # break
        # except Exception as e:
        #     print(e)
        # continue
    video.release()
    # break
