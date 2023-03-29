import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ast
import cv2

def plot_img(img_bin):
    figsize = 11, 9  # 设定图片大小，数字可以调整
    figure, ax = plt.subplots(figsize=figsize)
    jpg_as_np = np.frombuffer(img_bin, np.uint8)
    img = cv2.imdecode(jpg_as_np, cv2.IMREAD_COLOR)
    ax.imshow(img, interpolation='nearest')
    plt.show()
    return

if __name__ == '__main__':
    path = "D:\ChangAn\有图数据\\080"  # 待读取的文件夹
    path_list = os.listdir(path)
    # for filename in path_list:
        # print(os.path.join(path, filename))
    #csv_path = "D://ChangAn//有图数据//0805//1659670062.6_1659670103.73.csv"  # 改为有imageData_image/rawdata_fc数据的 csv文件路径
    for item ,i in enumerate(path_list):
        # try:
            data = pd.read_csv(path + "\\" + i)
            # size = (960 ,540)
            size = (960 ,360)

            fps = 20
            index = data.shape[0]       # index是data中的行数
            img_array = []
            # path_export = "rD:\\080\\export\\" + str(item) +".mp4"
            path_export = "D:\\080\\export\\" + str(item) + ".mp4"

            # print(path_export)
            # video = cv2.VideoWriter(r"D:\\080\\export\\" + str(item) + ".mp4", cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps,
            #                         size)  # fps是帧数，size是图片尺寸
            video = cv2.VideoWriter(os.path.join('r', path_export), cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps,
                                    size)
            for i in range(index):
                img = data.loc[i, 'imageData_image/rawdata_fc']
                img_bin = ast.literal_eval(img)
                # plot_img(img_bin)
                img_array.append(np.array(img_bin))
                image = cv2.imdecode(np.frombuffer(img_bin, np.uint8), 1)
                size = image.shape
                print(size[0] , size[1])
                video.write(image[0:360])
                print(video)
            video.release()
        # except Exception as e:
        #     print(e)