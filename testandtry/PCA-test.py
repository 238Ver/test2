import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
import os
import pickle

path = "D:\ChangAn\数据整理\无图数据\\0802\car_attr"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)


for item, i in enumerate(path_list):
    current_path = path + "\\" + i
    print(current_path + "------------")
    with open(current_path, 'rb') as f2:
         p4 = pickle.load(f2)
         # print(p4)
    # for i in p4:
        # print(p4[0][0]['track_id'])
    print(len(p4))
    print(len(p4[0]))
    # for num in p4[0]:
    for num in p4:
        print(num[0])
        X = np.array(p4)
        # X = np.array([[-1, 1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
        plt.subplot(221)

        pca=PCA(n_components=1)
        pca.fit(X)
        # print(pca.transform(X))
        explained_var = pca.explained_variance_ratio_  # 获取贡献率
        x = [1,2,3,4]
        y = [explained_var[0],0,0,0]
        print("各个主成分的贡献率为:"+str(explained_var))
        plt.bar(x,y,0.4,color="green")
        plt.subplot(222)
        pca = PCA(n_components=2)
        pca.fit(X)
        # print(pca.transform(X))
        explained_var = pca.explained_variance_ratio_  # 获取贡献率
        x = [1, 2,3,4]
        y = [explained_var[0], explained_var[1],0,0]
        plt.bar(x, y, 0.4, color="green")
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

# 首先，“原始数据各个变量单位不统一”， 我们并不一定非要将每个变量改成统一变量单位。 只要每个变量中所有数据都用同一个单位，数据
# 本身没有问题。主成分分析可以处理单位不同的数据。接下来，如果因为单位的不同，或
# 者变量数据本身分布不均，数据预处理是必须的。比如说变量a的分布是0-100， 变量b的分布是0-0.01， 这
# 对于主成分分析是有可能有影响。是否需要数据进行变化的衡量标准，比较主流的看法是：

# from sklearn.decomposition import PCA
# import numpy as np
#
# X = np.random.random((10000, 90))  # 数据
# print(X.shape)
# pca = PCA(n_components=3, whiten=True, random_state=42)  # 降维至3个特征
# newX = pca.fit_transform(X)
# print(newX.shape)
# explained_var = pca.explained_variance_ratio_  # 获取贡献率
# print(explained_var)