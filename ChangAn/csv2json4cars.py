import copy
import pandas as pd
import os
import json
import re
import pickle

path = "D:\ChangAn\无图数据1\\0802"  # 待读取的文件夹,需要每次都进行设置

column = []
path_list = os.listdir(path)
json_data_list_frame = []
json_data_list_percar = []

json_data_list = []
esp_yaw_rate_stp_motion = 0.0
esp_vehicle_speed_stp_motion = 0.0
esp_lat_accel_stp_motion = 0.0
esp_long_accel_stp_motion = 0.0
sas_steering_angle_stp_motion = 0.0

lines_fus_lines = []

vehicle_pos_lng_hdmap = 0.0
vehicle_pos_lat_hdmap = 0.0
vehicle_pos_current_link_id_hdmap = 0.0
vehicle_pos_current_lane_num_hdmap = 0.0
path_planning_routing_path_hdmap = 0.0
lane_curvature_100m_hdmap = 0.0
lane_curvature_200m_hdmap = 0.0
lane_curvature_300m_hdmap = 0.0

link_list_hdmap = []

timestamp_location = 0.0
heading_location = 0.0
latitude_location = 0.0
longitude_location = 0.0
altitude_location = 0.0
bcm_turn_light_switch_sts_bcmlight = 0.0

points_freespace_fc = []

column_name = ['objs/fus_objs', 'esp_yaw_rate/stp_motion', 'esp_vehicle_speed/stp_motion', 'esp_lat_accel/stp_motion',
               'esp_long_accel/stp_motion',
               'sas_steering_angle/stp_motion', 'lines/fus_lines', 'vehicle_pos_lng/hdmap', 'vehicle_pos_lat/hdmap',
               'vehicle_pos_current_link_id/hdmap',
               'vehicle_pos_current_lane_num/hdmap', 'path_planning_routing_path/hdmap', 'lane_curvature_100m/hdmap',
               'lane_curvature_200m/hdmap', 'lane_curvature_300m/hdmap',
               'link_list/hdmap', 'timestamp/location', 'heading/location', 'latitude/location', 'longitude/location',
               'altitude/location', 'bcm_turn_light_switch_sts/bcmlight',
               'points/freespace_fc']
temp_obs = []
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
        objs_fus_objs = data.loc[i, column_name[0]]
        # esp_yaw_rate_stp_motion = data.loc[i,column_name[1]]
        # esp_vehicle_speed_stp_motion = data.loc[i, column_name[2]]
        # esp_lat_accel_stp_motion = data.loc[i , column_name[3]]
        # esp_long_accel_stp_motion = data.loc[i , column_name[4]]
        # sas_steering_angle_stp_motion = data.loc[i , column_name[5]]
        # lines_fus_lines = data.loc[i , column_name[6]]
        # vehicle_pos_lng_hdmap = data.loc[i , column_name[7]]
        # vehicle_pos_lat_hdmap = data.loc[i , column_name[8]]
        # vehicle_pos_current_link_id_hdmap = data.loc[i , column_name[9]]
        # vehicle_pos_current_lane_num_hdmap = data.loc[i , column_name[10]]
        # path_planning_routing_path_hdmap = data.loc[i , column_name[11]]
        # lane_curvature_100m_hdmap = data.loc[i , column_name[12]]
        # lane_curvature_200m_hdmap = data.loc[i , column_name[13]]
        # lane_curvature_300m_hdmap = data.loc[i , column_name[14]]

        json_str_data_obs = objs_fus_objs  # json_str_data 字符串，里面是单引号
        # if len(json_str_data) < 1000:
        #     continue
        json_str_data_obs = json_str_data_obs.replace('False', 'false')
        json_str_data_obs = ', ' + json_str_data_obs[1:len(json_str_data_obs) - 1]
        json_str_arr_obs = json_str_data_obs.split(', \'objs_')
        json_str_arr_obs = json_str_arr_obs[1:]
        # print(len(json_str_arr))

        for i in json_str_arr_obs:  # 处理分割好的字符串列表，将它们转换成json
            i = i[i.index('{'):]
            # s = json_str_arr[i]
            # s = s[s.index('{'):]
            # print(i)
            try:
                json_data_obs = json.loads(tran(i), strict=False)  # dict里面是字典
                temp_obs.append(copy.deepcopy(json_data_obs))
            except Exception as e:
                continue
        column.append(copy.deepcopy(temp_obs))
        # column.append(copy.deepcopy(esp_yaw_rate_stp_motion))
        # column.append(copy.deepcopy(esp_vehicle_speed_stp_motion))
        # column.append(copy.deepcopy(esp_lat_accel_stp_motion))
        # column.append(copy.deepcopy(esp_long_accel_stp_motion))
        # column.append(copy.deepcopy(sas_steering_angle_stp_motion))

        ''' 下面进行车道线列表的获取'''
        # json_str_data_lines = lines_fus_lines  # json_str_data 字符串，里面是单引号
        # json_str_data_lines = json_str_data_lines.replace('False', 'false')
        # tran2list = tran(json_str_data_lines).split('},')
        # new_string = ''
        # for num, i in enumerate(tran2list):
        #     # if (num == 0):
        #     #     new_string = i[i.index(' {'):]
        #     #     new_string = new_string + '}'
        #     if (num == len(tran2list) - 1):
        #         new_string = i[i.index(' {'):]
        #         new_string = new_string[:-1]
        #     else:
        #         new_string = i[i.index(' {'):]
        #         new_string = new_string + '}'
        #     json_data_lines = json.loads(new_string)  # dict里面是字典
        #     temp_lines.append(copy.deepcopy(json_data_lines))
        # column.append(copy.deepcopy(temp_lines))
        # temp_lines.clear()
        ''''''
        # column.append(copy.deepcopy(vehicle_pos_lng_hdmap))
        # column.append(copy.deepcopy(vehicle_pos_lat_hdmap))
        # column.append(copy.deepcopy(vehicle_pos_current_link_id_hdmap))
        # column.append(copy.deepcopy(vehicle_pos_current_lane_num_hdmap))
        # column.append(copy.deepcopy(path_planning_routing_path_hdmap))
        # column.append(copy.deepcopy(lane_curvature_100m_hdmap))
        # column.append(copy.deepcopy(lane_curvature_200m_hdmap))
        # column.append(copy.deepcopy(lane_curvature_300m_hdmap))
        json_data_list_frame = copy.deepcopy(column)
        json_data_list_percar.append(copy.deepcopy(json_data_list_frame))
        column.clear()
        # print(json_data_list_percar[0])
    # json_data_list.append(copy.deepcopy(json_data_list_percar))
    # json_data_list_percar.clear()
    # print(len(json_data_list_percar), '/////////////////')
    # print(len(json_data_list_frame)) # 帧长度
    # print(len(json_data_list_percar)) #有多少帧
    # json_data_list_frame.clear()

    # print(len(json_data_list), '===============================')
    filename = current_path[-4] + ".txt"
    with open("../ChangAn/json_objs/" + filename, 'wb') as f:  # 打开文件
        pickle.dump(json_data_list_percar, f)  # 用 dump 函数将 Python 对象转成二进制对象文件
    json_data_list_percar.clear()
    # print(type(json_data_list_obj))
    # print("+++" + str(json_data_list_obj[0][0][0][0]['track_id']) +"+++"+ str(json_data_list_obj[0][0][0][0]['longitudinal_distance']))
    # break

# for i in json_data_list[0]:
#     print(i[0][0]['track_id'])
# for i in json_data_list_obj[0]:
#     print(i[1])
# for i in json_data_list_obj[0]:
#     print(i[2])
# for i in json_data_list_obj[0]:
#     print(i[3])
# for i in json_data_list_obj[0]:
#     print(i[4])
# for i in json_data_list_obj[0]:
#     print(i[5])
# # for i in json_data_list_obj[0]:
# #     print(i[6][0])
# for i in json_data_list_obj[0]:
#     print(i[7])
# for i in json_data_list_obj[0]:
#     print(i[14])
