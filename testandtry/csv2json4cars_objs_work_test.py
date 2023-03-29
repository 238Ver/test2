import os
import pickle

# path = "D:\ChangAn\数据整理\无图数据\\0822\json_objs"  # 待读取的文件夹,需要每次都进行设置
path = "D:\ChangAn\数据整理\有图数据\json_objs"  # 待读取的文件夹,需要每次都进行设置

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
            print(num[0]['track_id'])
        # except Exception as e:
        #     print(e)
        #     continue