import io
import cv2
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
import os
import pickle
import PIL

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为微软雅黑
plt.rcParams['axes.unicode_minus'] = False

# x x轴 自变量，但是是竖着的
x = np.linspace(-50, 50, 1000)
# y1 y1 是一个三次函数

path = "D:\ChangAn\数据整理\无图数据\\0822\hdmap"  # 待读取的文件夹,需要每次都进行设置
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
    path_export = "D:\\ChangAn\\drawing\\Lines\\0822\\" + str(item) + ".mp4"
    current_path = path + "\\" + i
    # size = (700,330)
    size = (960, 540)
    fps = 20
    print(current_path + "------------")
    with open(current_path, 'rb') as f:
        p = pickle.load(f)
    # video = cv2.VideoWriter(os.path.join('r', path_export), cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
    #                         fps,size)
    for item, num in enumerate(p):
        # print(str(num[0]['curve_parameter_a0']) + "  " +str(num[0]['curve_parameter_a1']) +
        #       "  " +str(num[0]['curve_parameter_a2'])+ "  " +str(num[0]['curve_parameter_a3']))
        # a0 = num[0]['curve_parameter_a0']
        # a1 = num[0]['curve_parameter_a1']
        # a2 = num[0]['curve_parameter_a2']
        # a3 = num[0]['curve_parameter_a3']
        print(len(num))
    #     y1 = a3 * x ** 3 + a2 * x ** 2 + a1 * x + a0
    #     #旋转操作
    #     origin = (0., 0)
    #     X1, Y1 = rotate(x, y1, origin)
    #     # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.3))
    #     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 5.4))
    #     ax1.set_title("原始图像")
    #     ax1.scatter(x, y1, color="blue", marker='o', s=10)
    #     ax1.plot(x, y1, 'r-')
    #     ax2.set_title(u"逆时针旋转90°图像")
    #     ax2.scatter(X1, Y1, color="blue", marker='o', s=20)
    #     ax2.plot(X1, Y1, 'r-')
    #     # plt.show()
    #     # print(fig)
    #     buffer = io.BytesIO()  #申请内存缓存空间
    #     plt.savefig(buffer,format='png')
    #     buffer.seek(0)
    #     dataPIL = PIL.Image.open(buffer).convert('RGB')
    #     data = np.asarray(dataPIL)
    #    # cv2.imshow("image", data)
    #    # cv2.waitKey(0)
    #    #  for ni in range(10):
    #    #      for nj in range(10):
    #    #          np.delete(data[ni][nj], 3, axis=0)
    #     video.write(data)
    #     buffer.close()  # 释放缓存
    #     # print(data.shape)
    #     # print(video)
    #     # break
    #     # except Exception as e:
    #     #     print(e)
    #         # continue
    # video.release()
    # break
