from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin) * np.random.rand(n) + vmin


# np.random.rand(n)产生1*n数组，元素大小0-1
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100

azim = -60
elev = 30
# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for i in range(100):
    for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
        plt.clf()  # 清除之前画的图
        fig = plt.gcf()  # 获取当前图
        ax = fig.gca(projection='3d')  # 获取当前轴
        ax.view_init(elev, azim)  # 设定角度

        xs = randrange(n, 23, 32)
        ys = randrange(n, 0, 100)
        zs = randrange(n, zlow, zhigh)
        ax.scatter(xs, ys, zs, c=c, marker=m)
        plt.pause(0.001)  # 暂停一段时间，不然画的太快会卡住显示不出来

        elev, azim = ax.elev , ax.azim - 0.5
        plt.ioff()  # 关闭画图窗口

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

ani = animation.ArtistAnimation(fig=fig, artists=artists, repeat=False, interval=10)
# plt.show()
ani.save('2.gif',writer='pillow', fps=30)
plt.show()
