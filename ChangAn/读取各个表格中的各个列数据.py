import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ast
import os
import json
import re



path = "D:\ChangAn\无图数据1\\0805"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)

for item, i in enumerate(path_list):
    # try:
    data = pd.read_csv(path + "\\" + i)
    print(str(item) + " -----")
    print(data.shape, end='\n')
    index = data.shape[0]  # index是data中的行数

    for i in range(index):
        obs = data.loc[i, 'points/freespace_fc']
        print(obs)
        print(i)
        print(type(obs))  # obs是str类型，指的是先定位行，后定位列得到的一个数据

        json_str_data = obs
        tran = lambda s: re.sub("\'", "\"", s)  # 单引号转双的操作
        # print(tran(json_str_data))
        json_data = json.loads(tran(json_str_data))
        print('*******')
        print(type(json_data))
        print(json_data['points_0']['position_longitudinal_distance'])
    print('-----------%d-------------' % item)
    print('\n')

# except Exception as e:
#     print(e)
