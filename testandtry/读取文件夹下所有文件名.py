import os
path="D:/ChangAn"  #待读取的文件夹
path_list=os.listdir(path)
# path_list.sort() #对读取的路径进行排序
for filename in path_list:
	print(os.path.join(path,filename))