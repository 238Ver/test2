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

        num_lines_track_id = num_lines[0]['line_track_id']
        if (num_lines[0]['line_track_id'] != num_lines_track_id and num_lines_track_id != 0):
            temp.append(2)
            num_lines_track_id = 1
        2
        if abs(num_car_attr[1] > 0.001):
            temp.append(2)
        else:
            temp.append(1)

        # 3
        for q in p_objs:
            for r in q:
                if (r['track_id'] != 0):
                    num_track_id = num_track_id + 1
        temp.append(num_track_id)

        # 4
        for q in p_points:
            for r in q:
                if (r['type'] == 3):
                    temp.append(2)
                    flag = 1
                    break
            if flag == 1:
                break
            else:
                temp.append(1)

        # 5
        # 6
        # for q in zip(p_objs):
        #     for r in zip(q):
        #         if(r['track_id'] != 0 ):
        #             num_track_id = num_track_id + 1
        #
        # a = [1, 2, 3]
        # b = [2, 3, 4, 5]
        # inter = [i for i in a if i in b]
        # temp.append(inter)
        # 7
        if num_car_attr[1] <= 20: temp.append(1)
        if num_car_attr[1] > 20 and num_car_attr[1] <= 40: temp.append(2)
        if num_car_attr[1] > 40: temp.append(3)
        # complex.append(abs(int(num_track_id) * (p_car_attr[0][0])))%100
        # complex.append(abs(int(num_track_id) * (p_car_attr[0][0]))%100)
        list_classify_perframe.append(copy.deepcopy(temp))
        complex_perframe.append(numpy.prod(temp) % 100)
        num_track_id = 1
        temp.clear()
    complex.append(numpy.mean(complex_perframe))
    # print(list_classify_perframe)
    list_classify.append(copy.deepcopy(list_classify_perframe))
    complex_avg.append(np.mean(complex) % 100 if np.mean(complex) != None else 1)
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
