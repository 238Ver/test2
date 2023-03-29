
#!/usr/bin/python3
#code-python(3.6)
import pandas as pd                 #导入pandas
import matplotlib.pyplot as plt
dt = pd.DataFrame({             #用字典去建立数据表，第一列的列名a,列值是[1,2,3,4,5];第二列的列名是b，列值是 [5, 6, 7, 8]，以此类推
    'a': [1, 2, 3, 4],
    'b': [5, 6, 7, 8],
    'c': [9, 10, 11, 12],
    'd': [13, 14, 15, 16]
})
dt.boxplot()  #对数据框中每列画箱线图，pandas自己有处理的过程，很方便
plt.show()
