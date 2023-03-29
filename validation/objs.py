import pandas as pd
import os

path = "D:\ChangAn\无图数据2\\0812"  # 待读取的文件夹,需要每次都进行设置
path_list = os.listdir(path)
data = pd.read_csv("D:\ChangAn\无图数据3\\0822\\1661164729.65_1661164790.1.csv")
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', 100)
print(data['objs/fus_objs'])
