import pandas as pd
import os
import json
import re

path = "D:\ChangAn\有图数据\\080"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)
# print('5555')
print(len(path_list))
points = []

for item, i in enumerate(path_list):
    # try:
    data = pd.read_csv(path + "\\" + i)
    print(str(item) + " -----/////////////////////////////////////////")
    print(data.shape, end='\n')
    print(path + "\\" + i)
    index = data.shape[0]  # index是data中的行数
    print(str(index) + '-----33333333333333333333')
    for i in range(index):
        lines = data.loc[i, 'lines/fus_lines']
        lines_arr = []
        # print(type(lines))  # lines是str类型，指的是先定位行，后定位列得到的一个数据
        json_str_data = lines  # json_str_data 字符串，里面是单引号
        tran = lambda s: re.sub("\'", "\"", s)  # 单引号转双的方法 ，tran(json_str_data) 字符串里面是双引号
        json_str_data = json_str_data.replace('False', 'false')
        # print(tran(json_str_data))
        tran2list = tran(json_str_data).split('},')
        # print(len(tran2list))

        new_string = ''
        for num, i in enumerate(tran2list):
            split_sign = ' {'
            # print("888888888" + str(item))
            if (num == 0):
                new_string = i[i.index(split_sign):]
                new_string = new_string + '}'
            elif (num == len(tran2list) - 1):
                new_string = i[i.index(split_sign):]
                new_string = new_string[:-1]
            else:
                new_string = i[i.index(split_sign):]
                new_string = new_string + '}'
        json_data = json.loads(new_string)  # dict里面是字典
        # print(json_data)
    print('-----------%d-------------' % item)
        # print('\n')
