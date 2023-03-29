import pandas as pd
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
    print('666666666666666666665666666666666666666666666666')
    print(path + "\\" + i)
    index = data.shape[0]  # index是data中的行数
    for i in range(index):
        hdmap = data.loc[i, 'link_list/hdmap']
        # print(hdmap)
        # print(i)
        # print(type(hdmap))  # hdmap是str类型，指的是先定位行，后定位列得到的一个数据
        json_str_data = hdmap  # json_str_data 字符串，里面是单引号
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
        json_str_arr = json_str_data.split(', \'links_')
        json_data_list = []

        json_str_arr = json_str_arr[1:]
        for i in range(len(json_str_arr)):
            s = json_str_arr[i]
            s = s[s.index('{'):]
            try:
                json_data = json.loads(tran(s),strict=False)  # dict里面是字典
            except Exception as e:
                print(e)
                continue
            keys = json_data['lane_attributelists'].keys()
            print(keys)
            print(json_data['lane_attributelists']['lane_attributelists_0']['lane_width_list']['lane_width_list_0']['value'])
        # print(len(json_str_data),'===============================')
        # break
print('-----------%d-------------' % item)

'''
print("下面开始输出points数组——一辆车的每一帧数据")
for item,i in enumerate(points):
    # print(item)
    print(i)
print(len(points))
'''
# except Exception as e:
#     print(e)