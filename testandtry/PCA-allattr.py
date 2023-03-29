import copy

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
import os
import pickle

path = "D:\ChangAn\数据整理\有图数据\car_attr"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)
current_path_1 = "D:\ChangAn\数据整理\有图数据\json_objs"
current_path_2 = "D:\ChangAn\数据整理\有图数据\hdmap"

for item, i in enumerate(path_list):
    current_path = path + "\\" + i
    print(current_path + "------------")
    with open(current_path, 'rb') as f2:
        p4 = pickle.load(f2)
        # p41 = pickle.load(f2)
    with open(current_path_1 + "\\" + i, 'rb') as f3:
         p5 = pickle.load(f3)
    with open(current_path_2+ "\\" + i, 'rb') as f4:
         p6 = pickle.load(f4)

         # print(p4)
    # for i in p4:
        # print(p4[0][0]['track_id'])
    print(len(p4))
    print(len(p4[0]))
    # for num in p4[0]:
    ' track_id的个数 平均距离 最近距离 最远距离 横纵向平均速度 横纵向平均加速度'
    for ii,j ,t in zip(p4 , p5 , p6):
        num_track_id = 0
        ave_num_long_dis = 0
        ave_num_lat_dis = 0
        ave_long_absolute = 0
        ave_lat_absolute = 0
        ave_lane_width = 0
        for q , s in zip(p5,p6):
            for r,t in zip(q,s):
                if(r['track_id'] != 0 ):
                    num_track_id = num_track_id + 1
                    ave_num_long_dis = ((num_track_id-1)* ave_num_long_dis + r['longitudinal_distance'])/num_track_id
                    ave_num_lat_dis =  ((num_track_id-1)* ave_num_lat_dis + r['lateral_distance'])/num_track_id
                    ave_long_absolute = ((num_track_id-1)* ave_long_absolute + r['longitudinal_absolute_velocity'])/num_track_id
                    ave_lat_absolute = ((num_track_id-1)* ave_lat_absolute + r['lateral_absolute_velocity'])/num_track_id
                # if t['lane_attributelists']['lane_attributelists_' + str(0)]['lane_width_list']['lane_width_list_' + str(0)]['value'] != 0:


        ii.append(copy.deepcopy(num_track_id))
        ii.append(copy.deepcopy(ave_num_long_dis))
        ii.append(copy.deepcopy(ave_num_lat_dis))
        ii.append(copy.deepcopy(ave_long_absolute))
        ii.append(copy.deepcopy(ave_lat_absolute))

    # with open(current_path, 'rb') as f2:
    #     p4 = pickle.load(f2)
    # for num in p4:
        # print(num[0])
    X = np.array(p4)
    # X = np.array([[-1, 1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    '''
    plt.subplot(221)
    pca=PCA(n_components=1)
    pca.fit(X)
    # print(pca.transform(X))
    explained_var = pca.explained_variance_ratio_  # 获取贡献率
    x = [1,2,3,4]
    y = [explained_var[0],0,0,0]
    print("各个主成分的贡献率为:"+str(explained_var))
    plt.bar(x,y,0.4,color="green")
    '''
    # plt.subplot(222)
    pca = PCA(n_components=2)
    pca.fit(X)
    pca_y = pca.transform(X)
    # explained_var = pca.explained_variance_ratio_  # 获取贡献率
    # x = [1, 2,3,4]
    # y = [explained_var[0], explained_var[1],0,0]
    # plt.bar(x, y, 0.4, color="green")
    '''
        plt.subplot(223)
        pca = PCA(n_components=3)
        pca.fit(X)
        # print(pca.transform(X))
        explained_var = pca.explained_variance_ratio_  # 获取贡献率
        x = [1, 2,3,4]
        y = [explained_var[0], explained_var[1],explained_var[2],0]
        plt.bar(x, y, 0.4, color="green")
        plt.subplot(224)
        pca = PCA(n_components=4)
        pca.fit(X)
        # print(pca.transform(X))
        explained_var = pca.explained_variance_ratio_  # 获取贡献率
        x = [1, 2,3,4]
        y = [explained_var[0], explained_var[1],explained_var[2], explained_var[3]]
        plt.bar(x, y, 0.4, color="green")
    plt.show()
    '''
# 首先，“原始数据各个变量单位不统一”， 我们并不一定非要将每个变量改成统一变量单位。 只要每个变量中所有数据都用同一个单位，数据
# 本身没有问题。主成分分析可以处理单位不同的数据。接下来，如果因为单位的不同，或
# 者变量数据本身分布不均，数据预处理是必须的。比如说变量a的分布是0-100， 变量b的分布是0-0.01， 这
# 对于主成分分析是有可能有影响。是否需要数据进行变化的衡量标准，比较主流的看法是：
