import os
import pickle
# a = 6
# temp = [1 ,2 ,3 ,4 ,5 ]
# for i in range(10):
#     temp.append(a)
#     if i == 5:
#         a = 100
#     print(temp)
# p1 = pickle.dumps(temp)
# print(p1)
# with open ("a.txt", 'wb') as f: #打开文件
#     pickle.dump(p1, f)
#     p2 = pickle.loads(p1)
#     print(p2)
# with open ("a.txt", 'r') as f1:
#     p3 = pickle.loads(f1)
#     print(p3)
import pandas as pd
path = "D:\ChangAn\数据整理\无图数据\\0822\hdmap"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)
path1 = "D:\ChangAn\无图数据3\\0822"  # 待读取的文件夹,需要每次都进行设置
path_list1 = os.listdir(path1)

for item, i in enumerate(path_list):
    current_path = path + "\\" + i
    print(current_path + "------------")
    with open(current_path, 'rb') as f2:
         p4 = pickle.load(f2)
         print(type(p4))
    for num in p4:
        print(num[0]['link_id'])


print(type(p4))
print(type(p4[0]))
print(type(p4[0][0]))

"""
各个车辆采集到的数据有：118
各个车辆采集到的数据有：118
各个车辆采集到的数据有：107
各个车辆采集到的数据有：110
各个车辆采集到的数据有：107
各个车辆采集到的数据有：113
各个车辆采集到的数据有：99
各个车辆采集到的数据有：109
各个车辆采集到的数据有：114
各个车辆采集到的数据有：108
各个车辆采集到的数据有：110
各个车辆采集到的数据有：109
各个车辆采集到的数据有：106
各个车辆采集到的数据有：122
各个车辆采集到的数据有：126
各个车辆采集到的数据有：147
各个车辆采集到的数据有：148
各个车辆采集到的数据有：139
各个车辆采集到的数据有：122
各个车辆采集到的数据有：107
各个车辆采集到的数据有：112
各个车辆采集到的数据有：127
各个车辆采集到的数据有：112
各个车辆采集到的数据有：167
各个车辆采集到的数据有：153
各个车辆采集到的数据有：157
各个车辆采集到的数据有：678

hdmap序列化之后的行数是118
hdmap序列化之后的行数是118
hdmap序列化之后的行数是107
hdmap序列化之后的行数是110
hdmap序列化之后的行数是107
hdmap序列化之后的行数是113
hdmap序列化之后的行数是99
hdmap序列化之后的行数是109
hdmap序列化之后的行数是114
hdmap序列化之后的行数是108
hdmap序列化之后的行数是110
hdmap序列化之后的行数是109
hdmap序列化之后的行数是106
hdmap序列化之后的行数是122
hdmap序列化之后的行数是126
hdmap序列化之后的行数是147
hdmap序列化之后的行数是148
hdmap序列化之后的行数是139
hdmap序列化之后的行数是122
hdmap序列化之后的行数是107
hdmap序列化之后的行数是112
hdmap序列化之后的行数是127
hdmap序列化之后的行数是112
hdmap序列化之后的行数是167
hdmap序列化之后的行数是153
hdmap序列化之后的行数是157
hdmap序列化之后的行数是678
"""