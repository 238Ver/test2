import cv2
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
    """
    D://ChangAn//有图数据//0805//1659667549.44_1659667584.69.csv   16
    一 1659666219.43_1659666263.64.csv   16
    二 1659666333.89_1659666371.57       16
    三 1659666617.49_1659666654.17       16
    四 1659669082.32_1659669115.1        16
    五 1659669115.49_1659669149.18       16
    六 1659669983.53_1659670020.52       16
    七 1659669115.49_1659669149.18       16
    八 1659670062.6_1659670103.73        16
    """
    csv_path = "D://ChangAn//无图数据1//0802//1659428125.53_1659428167.45.csv"  # 改为有imageData_image/rawdata_fc数据的 csv文件路径

    data = pd.read_csv(csv_path)
    print(data.shape)

    # print(data)
    ''' index = 125  # 将index设定为data中的具体行数
    # img = data.loc[index, 'esp_yaw_rate/stp_motion']
    # print(img)
    img = data.loc[index, 'imageData_image/rawdata_fc']

    img_bin = ast.literal_eval(img)
    plot_img(img_bin)
    '''
