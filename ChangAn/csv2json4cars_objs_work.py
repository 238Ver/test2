import copy
import pandas as pd
import os
import json
import re
import pickle
# path = "D:\ChangAn\无图数据3\\0822"  # 待读取的文件夹,需要每次都进行设置
path = "D:\ChangAn\有图数据\\080"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)
json_data_list_frame = []
json_data_list_percar = []
temp_obs = []
current_path = ""
temp_times = 0
tran = lambda s: re.sub("\'", "\"", s)  # 单引号转双，json中只接受双引号 ，tran(json_str_data) 字符串里面是双引号
for item, i in enumerate(path_list):  # 第i个表格，意味着第i辆车
    # try:
    data = pd.read_csv(path + "\\" + i)
    data = data.astype(str)
    current_path = i
    print(" -----" + str(item) + " -----")
    print(data.shape, end='\n')
    print(path + "\\" + i)
    for i in range(data.shape[0]):  # 第i帧数据 data,shape[0]是data中的行数
        objs_fus_objs = data.loc[i, 'objs/fus_objs']
        json_str_data_obs = objs_fus_objs  # json_str_data 字符串，里面是单引号
        json_str_data_obs = json_str_data_obs.replace('False', 'false')
        json_str_data_obs = json_str_data_obs.replace('True', 'true')
        json_str_data_obs = ', ' + json_str_data_obs[1:len(json_str_data_obs) - 1]
        json_str_arr_obs = json_str_data_obs.split(', \'objs_')
        json_str_arr_obs = json_str_arr_obs[1:]
        for i in json_str_arr_obs:  # 处理分割好的字符串列表，将它们转换成json
            i = i[i.index('{'):]
            # print(t)
            try:
                json_data_obs = json.loads(tran(i), strict=False)  # dict里面是字典
                temp_obs.append(copy.deepcopy(json_data_obs))
            except Exception as e:
                temp_times = temp_times + 1
                continue
        json_data_list_frame = copy.deepcopy(temp_obs)
        temp_obs.clear()
        json_data_list_percar.append(copy.deepcopy(json_data_list_frame))
        json_data_list_frame.clear()
    # print(list(json_data_list_percar[0][0].keys()))
    filename = current_path[:-4] + ".txt"
    # with open("../ChangAn/json_objs/" + filename, 'wb') as f:  # 打开文件
    # with open("D:\ChangAn\数据整理\无图数据\\0822\json_objs\\" + filename, 'wb') as f:  # 打开文件
    with open("D:\ChangAn\数据整理\有图数据\json_objs\\" + filename, 'wb') as f:  # 打开文件

        pickle.dump(json_data_list_percar, f)  # 用 dump 函数将 Python 对象转成二进制对象文件
    json_data_list_percar.clear()
    # print("temp_times :" + str(temp_times))
    # break