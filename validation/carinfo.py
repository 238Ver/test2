import copy
import pandas as pd
import os
import pickle
path = "D:\ChangAn\无图数据3\\0822"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)
column_name = ['esp_yaw_rate/stp_motion', 'esp_vehicle_speed/stp_motion', 'esp_lat_accel/stp_motion',
               'esp_long_accel/stp_motion',
               'sas_steering_angle/stp_motion',  'vehicle_pos_lng/hdmap', 'vehicle_pos_lat/hdmap',
               'vehicle_pos_current_link_id/hdmap',
               'vehicle_pos_current_lane_num/hdmap', 'path_planning_routing_path/hdmap', 'lane_curvature_100m/hdmap',
               'lane_curvature_200m/hdmap', 'lane_curvature_300m/hdmap', 'timestamp/location', 'heading/location',
               'latitude/location', 'longitude/location',
               'altitude/location', 'bcm_turn_light_switch_sts/bcmlight']
data = pd.read_csv("D:\ChangAn\无图数据3\\0822\\1661163801.38_1661163845.62.csv")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', 100)
print(data[column_name[4]])
