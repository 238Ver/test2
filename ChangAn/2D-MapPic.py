import folium
import os
import pandas as pd
import numpy as np
# from testandtry.clazz_hdmap import HdMap

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ast
import os
import json
import re

from pythonProjectTest.testandtry.clazz_hdmap import HdMap


def read_gps_data(path):
    P = pd.read_csv(path, header=None, dtype=np.double).values  # 读取csv文件，输出为narray
    locations_nav = P[:, 0:2].tolist()  # narray转换成list
    locations_true = P[:, 2:4].tolist()
    return locations_nav, locations_true


def draw_gps(locations_nav, locations_true, output_path, file_name):
    """
    绘制gps轨迹图
    :param locations: list, 需要绘制轨迹的经纬度信息，格式为[[lat1, lon1], [lat2, lon2], ...]
    :param output_path: str, 轨迹图保存路径
    :param file_name: str, 轨迹图保存文件名
    :return: None
    """
    m = folium.Map(locations_true[0], zoom_start=30, attr='default')  # 中心区域的确定

    folium.PolyLine(  # polyline方法为将坐标用实线形式连接起来
        locations_true,  # 将坐标点连接起来
        weight=4,  # 线的大小为4
        color='red',  # 线的颜色为红色
        opacity=0.8,  # 线的透明度
    ).add_to(m)  # 将这条线添加到刚才的区域m内

    folium.PolyLine(  # polyline方法为将坐标用虚线形式连接起来
        locations_nav,  # 将坐标点连接起来
        weight=2,  # 线的大小为2
        color='blue',  # 线的颜色为蓝色
        opacity=0.8,  # 线的透明度
        dash_array='5'  # 虚线频率
    ).add_to(m)  # 将这条线添加到刚才的区域m内

    # 起始点，结束点
    folium.Marker(locations_true[0], popup='<b>Starting Point</b>').add_to(m)
    folium.Marker(locations_true[-1], popup='<b>End Point</b>').add_to(m)

    m.save(os.path.join(output_path, file_name))  # 将结果以HTML形式保存到指定路径

def dict2HdMap(d):
    # return Point(str(d[list(d.keys())[0]]),d['motion_state'], d['type'], d['position_longitudinal_distance'], d['position_lateral_distance'])
    return HdMap(d['motion_state'], d['type'], d['position_longitudinal_distance'], d['position_lateral_distance'])


path = "D:\ChangAn\有图数据\\0805"  # 待读取的文件夹,需要每次都进行设置
# path = "D:\ChangAn\无图数据1\\0802"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)
# print(len(path_list))
points = []

for item, i in enumerate(path_list):
    # try:
    data = pd.read_csv(path + "\\" + i)
    print(str(item) + " -----")
    print(data.shape, end='\n')
    print('55555555555555555555555555555555555555555555555555555555555555555555555555555555')
    print(path + "\\" + i)
    index = data.shape[0]  # index是data中的行数
    narray = []
    for i in range(index):
        # obs = data.loc[i, 'link_list/hdmap']
        lng = data.loc[i, 'vehicle_pos_lng/hdmap']
        lat = data.loc[i,'vehicle_pos_lat/hdmap']
        temp = [lat , lng]
        narray.append(temp)
        # print(narray)
    # draw_gps(narray, narray, 'D:\ChangAn\drawing',  str(item)+'.html')
    draw_gps(narray, narray, 'D:\ChangAn\drawing\RealMap有图',  str(item)+'.html')

    # break
print('-----------%d-------------' % item)
        # print('\n')

'''
print("下面开始输出points数组——一辆车的每一帧数据")
for item,i in enumerate(points):
    # print(item)
    print(i)
print(len(points))
'''
# except Exception as e:
#     print(e)


# locations_nav, locations_true = read_gps_data(path1)
# draw_gps(locations_nav, locations_true, '../drawing', '385276.html')
