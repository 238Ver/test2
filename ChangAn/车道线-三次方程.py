import matplotlib
from matplotlib import pyplot as plt
import numpy as np


# a是三次项系数 b是二次项系数 c是一次项系数 d是常数项系数
def calc(a, b, c, d):
    x = np.linspace(-40, 40, 100) #from 参数1  to 参数2 生成 参数3的数据
    y = a * x ** 3 + b * x ** 2 + c * x + d
    plt.figure(figsize=(8, 4))
    # ax = plt.subplots(2, 1)
    # ax_sub = ax.twinx()
    plt.plot(x, y, color="blue", linewidth=1.5)
    # plt.plot(x, y, color="blue", linewidth=1.5)
    # ax.set_xlim((50, 0))
    # ax.invert_xaxis()
    matplotlib.lines.Line2D
    plt.show()

calc(10, -4, 6, 4)