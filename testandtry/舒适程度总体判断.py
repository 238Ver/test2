import copy
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
import numpy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import stats

path = "D:\ChangAn\数据整理\无图数据\\0822\car_attr"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)
path1 = "D:\ChangAn\数据整理\无图数据\\0822\json_objs"  # 待读取的文件夹,需要每次都进行设置
path_list1 = os.listdir(path1)
path2 = "D:\ChangAn\数据整理\无图数据\\0822\lines"  # 待读取的文件夹,需要每次都进行设置
path_list2 = os.listdir(path1)
path3 = "D:\ChangAn\数据整理\无图数据\\0822\hdmap"  # 待读取的文件夹,需要每次都进行设置
path_list3 = os.listdir(path1)
path4 = "D:\ChangAn\数据整理\无图数据\\0822\points_freespace_fc"  # 待读取的文件夹,需要每次都进行设置
path_list4 = os.listdir(path1)
list_classify = []
list_classify_perframe = []
temp = []
complex_perframe = []
complex_avg = []
num_track_id = 1
for item, i in enumerate(path_list):
    current_path = path + "\\" + i
    print(current_path + "------------")
    with open(current_path, 'rb') as f2:
        p_car_attr = pickle.load(f2)
    with open(path1 + "\\" + i, 'rb') as f3:
        p_objs = pickle.load(f3)
    with open(path2 + "\\" + i, 'rb') as f6:
        p_lines = pickle.load(f6)
    with open(path3 + "\\" + i, 'rb') as f7:
        p_points = pickle.load(f7)
    num_track_id = 1
    num_lines_track_id = 1
    complex = []
    for num_car_attr, num_objs, num_lines, num_points \
            in zip((p_car_attr), (p_objs), (p_lines), (p_points)):
        # 条件1结束
        if (num_car_attr[2] == 0 or num_car_attr[3] == 0 or num_car_attr[0] == 0):
            temp.append(10)
        else:
            temp.append(1 / (num_car_attr[1] * num_car_attr[2] * num_car_attr[3]) % 100)
        # complex.append(abs(int(num_track_id) * (p_car_attr[0][0])))%100
        # complex.append(abs(int(num_track_id) * (p_car_attr[0][0]))%100)
        list_classify_perframe.append(copy.deepcopy(temp))
        complex_perframe.append(numpy.prod(temp) % 100)
        num_track_id = 1
        temp.clear()
    complex.append(numpy.average(complex_perframe))
    # complex_avg.append(np.var(complex)%100 if np.mean(complex) != None else 0 )
    # counts = np.bincount(complex)
    # # 返回众数
    # np.argmax(counts)
    complex_avg.append(stats.mode(complex)[0][0] % 100 if np.mean(complex) != None else 0)
    # print(list_classify_perframe)
    list_classify.append(copy.deepcopy(list_classify_perframe))
    # list_classify.clear()

    x = list(range(1, len(p_car_attr) + 1, 1))
    # x = range(len(p_car_attr))
    # x = [1,2,3,4]
    # x =np.transpose(x)
    # y = x
    print(len(x))
    print(len(complex))
    # plt.plot(x,complex_perframe)
    # plt.show()
    complex_perframe.clear()
x2 = list(range(1, len(os.listdir(path)) + 1, 1))
plt.plot(x2, complex_avg)
plt.show()
# print(complex_avg)
