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
path = "D:\ChangAn\数据整理\无图数据\\0822\lines"  # 待读取的文件夹,需要每次都进行设置
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
    for num in p4:
        # try:
            # print("///////////")
            # print(num['curve_parameter_a0'])
         print(num[0]['curve_parameter_a0'])

        # except Exception as e:
        #     print(e)
        #     continue
