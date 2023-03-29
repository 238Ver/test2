import copy
import pandas as pd
import os
import json
import re
import pickle

path = "D:\ChangAn\无图数据1\\0802"  # 待读取的文件夹,需要每次都进行设置
# path = "D:\ChangAn\有图数据\\080"  # 待读取的文件夹,需要每次都进行设置

car_attr = []
path_list = os.listdir(path)
# column_name = ['esp_yaw_rate/stp_motion', 'esp_vehicle_speed/stp_motion', 'esp_lat_accel/stp_motion',
#                'esp_long_accel/stp_motion',
#                'sas_steering_angle/stp_motion',  'vehicle_pos_lng/hdmap', 'vehicle_pos_lat/hdmap',
#                'vehicle_pos_current_link_id/hdmap',
#                'vehicle_pos_current_lane_num/hdmap', 'path_planning_routing_path/hdmap', 'lane_curvature_100m/hdmap',
#                'lane_curvature_200m/hdmap', 'lane_curvature_300m/hdmap', 'timestamp/location', 'heading/location',
#                'latitude/location', 'longitude/location',
#                'altitude/location', 'bcm_turn_light_switch_sts/bcmlight']
column_name = ['esp_yaw_rate/stp_motion', 'esp_vehicle_speed/stp_motion', 'esp_lat_accel/stp_motion',
               'esp_long_accel/stp_motion',
               'sas_steering_angle/stp_motion',  'lane_curvature_100m/hdmap',
               'lane_curvature_200m/hdmap', 'lane_curvature_300m/hdmap', 'heading/location',
                'bcm_turn_light_switch_sts/bcmlight']
temp = []
temp_lines = []
current_path = ""
tran = lambda s: re.sub("\'", "\"", s)  # 单引号转双，json中只接受双引号 ，tran(json_str_data) 字符串里面是双引号
for item, i in enumerate(path_list):  # 第i个表格，意味着第i辆车
    # for item, i in range(0):  # 第i个表格，意味着第i辆车
    # try:
    data = pd.read_csv(path + "\\" + i)
    current_path = i
    print(" -----" + str(item) + " -----")
    print(data.shape, end='\n')
    print(path + "\\" + i)
    for i in range(data.shape[0]):  # 第i帧数据 data,shape[0]是data中的行数
        temp.append(data.loc[i,column_name[0]])
        temp.append(data.loc[i, column_name[1]])
        temp.append(data.loc[i , column_name[2]])
        temp.append(data.loc[i , column_name[3]])
        temp.append(data.loc[i , column_name[4]])
        temp.append(data.loc[i , column_name[5]])
        temp.append(data.loc[i , column_name[6]])
        temp.append(data.loc[i , column_name[7]])
        temp.append(data.loc[i , column_name[8]])
        # temp.append(data.loc[i , column_name[9]])
        # temp.append(data.loc[i , column_name[10]])
        # temp.append(data.loc[i , column_name[11]])
        # temp.append(data.loc[i , column_name[12]])
        # temp.append(data.loc[i, column_name[13]])
        # temp.append(data.loc[i, column_name[14]])
        # temp.append(data.loc[i, column_name[15]])
        # temp.append(data.loc[i, column_name[16]])
        # temp.append(data.loc[i, column_name[17]])
        # temp.append(data.loc[i, column_name[18]])
        car_attr.append(copy.deepcopy(temp))
        temp.clear()
    filename = current_path[:-5] + ".txt"
    # with open("D:\ChangAn\数据整理\无图数据\\0802\car_attr\\" + filename, 'wb') as f:  # 打开文件
    with open("D:\ChangAn\数据整理\有图数据\car_attr\\" + filename, 'wb') as f:  # 打开文件
        pickle.dump(car_attr, f)  # 用 dump 函数将 Python 对象转成二进制对象文件
    car_attr.clear()