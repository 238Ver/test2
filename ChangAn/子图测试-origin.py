import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为微软雅黑
plt.rcParams['axes.unicode_minus'] = False

# x x轴 自变量，但是是竖着的
# year = [2010, 2011, 2012, 2013, 2014, 2015]
x = np.linspace(-40, 40, 1000)

# y1 y1 是一个三次函数

y1 = 1 * x ** 3 + 2 * x ** 2 + 3 * x + 4
# 定义成交量
y2 = x ** 2

fig, ax = plt.subplots(1, 1)
# 共享x轴，生成次坐标轴
ax_sub = ax.twinx()
# ax.set_xlim(left=0, right=20)
# ax.set_ylim(bottom=0, top=0)
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))  # 指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
ax.xaxis.set_ticks_position('bottom')
ax.invert_xaxis()
# 绘图
# l1, = ax.plot(year, price, 'r-', label='price')
l1, = ax.plot(x, y1, 'r-', label='price')
l2, = ax_sub.plot(x, y2, 'g-', label='total')
# 放置图例
plt.legend(handles=[l1, l2], labels=['price', 'total'], loc=0)
# 设置主次y轴的title
# ax.set_ylabel('房价(元)')
# ax_sub.set_ylabel('成交量(套)')
# # 设置x轴title
# ax.set_xlabel('这是x轴 应该竖起来')
# # 设置图片title
# ax.set_title('主次坐标轴演示图')
plt.show()
