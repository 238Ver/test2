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

# path = "D:\ChangAn\数据整理\有图数据\\0802\json_objs"  # 待读取的文件夹,需要每次都进行设置
path = "D:\ChangAn\数据整理\有图数据\json_objs"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)

for item, i in enumerate(path_list):
    path_export = "D:\\ChangAn\\drawing\\Lines\\080\\" + str(item) + ".mp4"
    current_path = path + "\\" + i
    # size = (700,330)
    size = (960,540)
    fps = 20
    base_x = 0
    base_y = 0
    print(current_path + "------------")
    with open(current_path, 'rb') as f:
         p = pickle.load(f)
    fig, (ax1,ax2) = plt.subplots(1,2, figsize=(9.6, 5.4))
    # ax1.plot(0, 0, marker='o', color='red')
    for item , num in enumerate(p):
        print("第"  + str(item) + "帧")
        for j_item ,j in enumerate(num):
            if j['longitudinal_distance'] != 0 and j['lateral_distance'] != 0:
                # ax2.spines['bottom'].set_position(('data', 0))  # 指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
                # ax2.spines['left'].set_position(('data', 0))
                # ax2.spines['right'].set_position(('data', 0))
                # ax2.spines['top'].set_position(('data', 0))
                ax2.plot(j['longitudinal_distance'] + base_x, j['lateral_distance'] + base_y , marker='v', color="black")
        plt.show()