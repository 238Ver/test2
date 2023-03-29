from testandtry.clazz_point import Point

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ast
import os
import json
import re


def dict2Point(d):
    # return Point(str(d[list(d.keys())[0]]),d['motion_state'], d['type'], d['position_longitudinal_distance'], d['position_lateral_distance'])
    return Point(d['motion_state'], d['type'], d['position_longitudinal_distance'], d['position_lateral_distance'])


path = "D:\ChangAn\无图数据1\\0805"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)
# print('5555')
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
    for i in range(index):
        obs = data.loc[i, 'points/freespace_fc']
        # print(obs)
        # print(i)
        # print(type(obs))  # obs是str类型，指的是先定位行，后定位列得到的一个数据
        json_str_data = obs  # json_str_data 字符串，里面是单引号
        tran = lambda s: re.sub("\'", "\"", s)  # 单引号转双的方法 ，tran(json_str_data) 字符串里面是双引号
        # print(tran(json_str_data))

        tran2list = tran(json_str_data).split('},')
        # print(tran2list[0])

        json_data = json.loads(tran(json_str_data))  # dict里面是字典
        for item, i in enumerate(tran2list):
            split_sign = ' {'
            # print("888888888" + str(item))
            if (item == 0):
                new_string = i[i.index(split_sign):]
                new_string = new_string + '}'
                # print("数据库00000")
                # print(i[:i.index(split_sign)])
                # print(new_string)
                point = json.loads(tran(new_string), object_hook=dict2Point)
            elif (item == len(tran2list) -1):
                new_string = i[i.index(split_sign):]
                new_string = new_string[:-1]
                # print("数据库11111")
                # print(i[:i.index(split_sign)])
                # print(new_string)
                point = json.loads(tran(new_string), object_hook=dict2Point)
            else:
                new_string = i[i.index(split_sign):]
                new_string = new_string + '}'
                # print("数据库22222")
                # print(i[:i.index(split_sign)])
                # print(new_string)
                point = json.loads(tran(new_string), object_hook=dict2Point)

            points.append(point)
            # print('////////////////\\\\\\\\\\\\\\')
            # print(type(point))
            # print(point.position_longitudinal_distance)
            # print('*******')
            # print(type(json_data))
            # print(json_data['points_0']['position_longitudinal_distance'])
print('-----------%d-------------' % item)
        # print('\n')

print("下面开始输出points数组——一辆车的每一帧数据")
for item,i in enumerate(points):
    # print(item)
    print(i)
print(len(points))
# except Exception as e:
#     print(e)