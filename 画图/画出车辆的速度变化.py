import io
import cv2
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
import os
import pickle
import PIL

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为微软雅黑
plt.rcParams['axes.unicode_minus'] = False

path = "D:\ChangAn\数据整理\无图数据\\0822\car_attr"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)

for item, i in enumerate(path_list):
    path_export = "D:\\ChangAn\\drawing\\Speed\\0822\\" + str(i[:-4]) + ".mp4"
    current_path = path + "\\" + i
    # size = (700,330)
    size = (960,540)
    fps = 20
    base_x = 0
    base_y = 0
    print(current_path + "------------")
    with open(current_path, 'rb') as f:
         p = pickle.load(f)
    video = cv2.VideoWriter(os.path.join('r', path_export), cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                            fps, size)
    fig, (ax1) = plt.subplots(1, figsize=(9.6, 5.4))
    ax1.set_title(str(i[:-4]) + "汽车速度曲线")
    plt.grid("on")
    former_x = 0.0
    former_y = 0.0
    for item , num in enumerate(p):
        print("第"  + str(item) + "帧")
        ax1.plot(item , num[1] , marker='o', markersize=3 , color="black")
        if item!=0:
            ax1.plot([former_x, item], [former_y,num[1]])
        former_x = item
        former_y = num[1]
    # plt.show()
        buffer = io.BytesIO()  # 申请内存缓存空间
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        dataPIL = PIL.Image.open(buffer).convert('RGB')
        data = np.asarray(dataPIL)
        # cv2.imshow("image", data)
        # cv2.waitKey(0)
        video.write(data)
        buffer.close()  # 释放缓存
    video.release()