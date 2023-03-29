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
path = "D:\ChangAn\数据整理\无图数据\\0822\hdmap"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)

for item, i in enumerate(path_list):
    path_export = "D:\\ChangAn\\drawing\\hdmap\\0822\\" + str(item) + ".mp4"
    current_path = path + "\\" + i
    # size = (700,330)
    size = (960,540)
    fps = 20
    base_x = 0
    base_y = 0
    print(current_path + "------------")
    with open(current_path, 'rb') as f:
         p = pickle.load(f)
    for item , num in enumerate(p):
        print("第"  + str(item) + "帧-----------------------")
        # fig, (ax1) = plt.subplots(1, figsize=(9.6, 5.4))
        # ax1.plot(0, 0, marker='o', color='red')
        for j_item ,j in enumerate(num):
            print(str(len(j['lines'])) + " " + str(type(j['lines'])))
            for t_item ,t in enumerate(j['lines']):
                # print(j['lines'][t]['markings']['markings_0']['color'])
                if(j['lines'][t]['line_type'] == 0): print("实线" + str(j['lines'][t]['markings']['markings_0']['color']))
                if(j['lines'][t]['line_type'] == 1): print("虚线" + str(j['lines'][t]['markings']['markings_0']['color']))
                if (j['lines'][t]['line_type'] == 2): print("双虚线" + str(j['lines'][t]['markings']['markings_0']['color']))
                if (j['lines'][t]['line_type'] == 3): print("虚实线" + str(j['lines'][t]['markings']['markings_0']['color']))
                if (j['lines'][t]['line_type'] == 4): print("实虚线" + str(j['lines'][t]['markings']['markings_0']['color']))
                if (j['lines'][t]['line_type'] == 5): print("双实线" + str(j['lines'][t]['markings']['markings_0']['color']))


                    # j['lines']['lines_' + str(0)]['line_type']
            # print('track_id ' +str(j['track_id']) +'  '
            #       'longitudinal_distance ' + str(j['longitudinal_distance']) +'  '
            #        'lateral_distance' + str(j['lateral_distance']) + ' '
            #       'length ' + str(j['length']) +'  '
            #       'width ' + str(j['width'])+'  '+'  '
            #       'status' + str(j['status'])
            #       )
        #     if j['longitudinal_distance'] != 0 and j['lateral_distance'] != 0:
        #         ax1.spines['bottom'].set_position(('data', 0))  # 指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
        #         ax1.spines['left'].set_position(('data', 0))
        #         ax1.spines['right'].set_position(('data', 0))
        #         ax1.spines['top'].set_position(('data', 0))
        #         ax1.plot(j['longitudinal_distance'] + base_x, j['lateral_distance'] + base_y , marker='v', color="black")
        # plt.show()