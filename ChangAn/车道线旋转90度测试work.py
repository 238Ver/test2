import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为微软雅黑
plt.rcParams['axes.unicode_minus'] = False

# x x轴 自变量，但是是竖着的
# year = [2010, 2011, 2012, 2013, 2014, 2015]
x = np.linspace(-50, 50, 1000)

# y1 y1 是一个三次函数

# y1 = 1.7812280654907227 * x ** 3 + 0.01120835728943348 * x ** 2 + 0.0003255920310039073 * x + -1.844612711465743e-06
# y1 =  -1.2043999504385283e-06 * x ** 3 + -0.00040054478449746966 * x ** 2 +  -0.0056392839178442955 * x + 1.4954980611801147
# y1 = -4.170927923041745e-07 * x ** 3 + -2.6268895453540608e-05 * x ** 2 +  -0.0018928225617855787 * x +  1.488905668258667
# y1 = 1.500805139541626 * x ** 3 +  0.012225998565554619 * x ** 2 + -4.410295878187753e-05 * x + 1.0348124988013296e-06
# y1 = 1.7812280654907227 * x ** 3 +  0.01120835728943348 * x ** 2 + 0.0003255920310039073 * x + -1.844612711465743e-06
# y1 = 1.6521326303482056 +   -0.004804055672138929 * x * +  2.1401259800768457e-05 * x **2+  -1.4686143856579292e-07*x**3
# y1 =  3.555676357791526e-07 * x ** 3 +  -0.004652056843042374 * x ** 2 + -0.004652056843042374 * x + 1.5899113416671753
y1 =   -2.504800477254321e-06 * x ** 3 +  0.0008369667921215296 * x ** 2 + 0.028414707630872726 * x +  0.6208932399749756
# y1 = 0 * x ** 3 + 0 * x ** 2 + 0 * x + 0

# y1 = 2*x

# 定义成交量
y2 = x ** 2


def rotate(x, y, origin=(0, 0)):
    # shift to origin
    x1 = x - origin[0]
    y1 = y - origin[1]

    # rotate
    x2 = -y1
    y2 = x1

    # shift back
    x3 = x2 + origin[1]
    y3 = y2 + origin[0]

    return x3, y3


# now let's do the rotation
origin = (0., 0)
X1, Y1 = rotate(x, y1, origin)

# fig, ax = plt.subplots(1, 1)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.3))
# 共享x轴，生成次坐标轴

# ax_sub = ax.twinx()

# ax.set_xlim(left=0, right=20)
# ax.set_ylim(bottom=0, top=0)
'''ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))  # 指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
ax.xaxis.set_ticks_position('bottom')
ax.invert_xaxis()'''
# 绘图


ax1.set_title("original")
ax1.scatter(x, y1, color="blue", marker='o', s=10)
ax1.plot(x, y1, 'r-')

ax2.set_title(u"90°rotate")
ax2.scatter(X1, Y1, color="blue", marker='o', s=20)
ax2.plot(X1, Y1, 'r-')

'''
l1, = ax.plot(x, y1, 'r-', label='price')
# l2, = ax_sub.plot(x, y2, 'g-', label='total')
l3, = ax.plot(X1,Y1,'g-')
# 放置图例
plt.legend(handles=[l1, l3], labels=['price', 'total'], loc=0)'''
# 设置主次y轴的title
# ax.set_ylabel('房价(元)')
# ax_sub.set_ylabel('成交量(套)')
# # 设置x轴title
# ax.set_xlabel('这是x轴 应该竖起来')
# # 设置图片title
# ax.set_title('主次坐标轴演示图')
plt.show()