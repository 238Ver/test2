import copy
import pandas as pd
import os
import json
import re
import pickle
path = "D:\ChangAn\无图数据3\\0822"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)
# for item, i in enumerate(path_list):
#     current_path = path + "\\" + i
#     print(current_path + "------------")
#
#     data = pd.read_csv(path + "\\" + i)
#     json_str_data_points = data.loc[i, 'points/freespace_fc']  # json_str_data 字符串，里面是单引号
data = pd.read_csv("D:\ChangAn\无图数据3\\0822\\1661163845.63_1661163887.16.csv")
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', 100)
print(data['lines/fus_lines'])
