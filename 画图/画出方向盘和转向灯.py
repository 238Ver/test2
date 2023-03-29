import io
import math

import cv2
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
import os
import pickle
import PIL
from PIL import Image

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为微软雅黑
plt.rcParams['axes.unicode_minus'] = False

path = "D:\ChangAn\数据整理\无图数据\\0822\car_attr"  # 待读取的文件夹,需要每次都进行设置
# path = "D:\ChangAn\数据整理\有图数据\car_attr"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)

for item, i in enumerate(path_list):
    path_export = "D:\\ChangAn\\drawing\\steeringwheel\\0822\\" + str(i[:-4]) + ".mp4"
    # path_export = "D:\\ChangAn\\drawing\\steeringwheel\\0822\\" + str(i[:-4]) + ".H264"
    # path_export = "D:\\ChangAn\\drawing\\steeringwheel\\有图\\" + str(i[:-4]) + ".mp4"
    current_path = path + "\\" + i
    # size = (960,540)
    size = (640, 480)
    fps = 20
    base_x = 0
    base_y = 0
    print(current_path + "------------")
    with open(current_path, 'rb') as f:
        p = pickle.load(f)
    video = cv2.VideoWriter(os.path.join('r', path_export), cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                            fps, size)
    # video = cv2.VideoWriter(os.path.join('r', path_export), cv2.VideoWriter_fourcc('H', '2', '6', '4'),
    #                         fps, size)
    plt.figure(12)
    ax1 = plt.subplot(221)
    img1 = Image.open("方向盘.png")
    imgnolight = Image.open("light0.jpg")
    imgleftlight = Image.open("light1.jpg")
    imgrightlight = Image.open("light2.jpg")

    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                        wspace=0.2, hspace=0.5)
    # plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
    #                     wspace=0, hspace=0.5)
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    ax2 = plt.subplot(222)
    ax3 = plt.subplot(212)
    plt.cla()
    # fig, (ax1,ax2) = plt.subplots(1,2, figsize=(10.6, 5.4))
    # ax1.set_title(str(i[:-4]) + "汽车方向盘和转向灯")
    ax3.grid("on")
    ax3.set_title(str(i[:-4]) + "汽车方向盘和转向灯", fontsize=10)
    former_x = 0.0
    former_y = 0.0
    for item, num in enumerate(p):
        print("第" + str(item) + "帧")
        ax1 = plt.subplot(221)
        # img2 = img1.rotate(360 - math.degrees(num[4]))
        img2 = img1.rotate(math.degrees(num[4]))

        ax1.imshow(img2)

        ax2 = plt.subplot(222)
        if num[-1] == 0:
            ax2.imshow(imgnolight)
        if num[-1] == 1:
            ax2.imshow(imgleftlight)
        if num[-1] == 2:
            ax2.imshow(imgrightlight)

        ax3.plot(item, num[4], marker='o', markersize=3, color="black")
        if item != 0:
            ax3.plot([former_x, item], [former_y, num[4]])
        former_x = item
        former_y = num[4]
        # plt.show()
        buffer = io.BytesIO()  # 申请内存缓存空间
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        dataPIL = PIL.Image.open(buffer).convert('RGB')
        data = np.asarray(dataPIL)
        # cv2.imshow("image", data)
        # cv2.waitKey(0)
        ax1.cla()
        plt.cla()
        video.write(data)
        buffer.close()  # 释放缓存
    video.release()
