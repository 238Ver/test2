from testandtry.clazz_hdmap import HdMap

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ast
import os
import json
import re


def dict2HdMap(d):
    # return Point(str(d[list(d.keys())[0]]),d['motion_state'], d['type'], d['position_longitudinal_distance'], d['position_lateral_distance'])
    return HdMap(d['motion_state'], d['type'], d['position_longitudinal_distance'], d['position_lateral_distance'])


path = "D:\ChangAn\有图数据\\080"  # 待读取的文件夹,需要每次都进行设置
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
        # obs = data.loc[i, 'link_list/hdmap']
        obs = data.loc[i, 'objs/fus_objs']

        # print(obs)
        # print(i)
        # print(type(obs))  # obs是str类型，指的是先定位行，后定位列得到的一个数据
        json_str_data = obs  # json_str_data 字符串，里面是单引号
        if len(json_str_data) < 1000:
            continue
        tran = lambda s: re.sub("\'", "\"", s)  # 单引号转双的方法 ，tran(json_str_data) 字符串里面是双引号
        split_sign_1 = '\''
        # print(type(tran(json_str_data)))
        # print(tran(json_str_data)['lane_attributelists'])
        # tran2list = tran(json_str_data).split('},')
        # print(tran2list[0])
        # new_string = json_str_data[3]


        # json_data = demjson.encode(tran(json_str_data))
        json_str_data = json_str_data.replace('False', 'false')
        json_str_data = ', '+json_str_data[1:len(json_str_data)-1]
        json_str_arr = json_str_data.split(', \'objs_')
        json_data_list = []
        json_str_arr = json_str_arr[1:]
        for i in range(len(json_str_arr)):
            s = json_str_arr[i]
            s = s[s.index('{'):]
            # s = s[:539]+' '+s[540:]
            try:
                json_data = json.loads(tran(s),strict=False)  # dict里面是字典
            except Exception as e:
                continue
            print(s[510:600],'----------------------------------')
            # print(json_data['obj_refer_points']['obj_refer_points_1']['longitudinal_distance'])
        print(len(json_str_data),'===============================')
        break
        # print(tran(json_str_data)[370:390])
        '''
        for item, i in enumerate(tran2list):
            split_sign = ' {'
            # print("888888888" + str(item))
            if (item == 0):
                new_string = i[i.index(split_sign):]
                new_string = new_string + '}'
                # print("数据库00000")
                # print(i[:i.index(split_sign)])
                # print(new_string)
                point = json.loads(tran(new_string), object_hook=dict2HdMap())
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
        '''
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