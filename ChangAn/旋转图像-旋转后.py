import numpy as np
import matplotlib.pyplot as plt

a = np.array([4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9])
b = np.array([i/float(len(a)) for i in range(1, len(a)+1)])
A = np.array([i/10. for i in range(40, 91)])
B = np.array([ 0.06200455,  0.07389492,  0.08721351,  0.10198928,  0.11823225,
                0.13593267,  0.15506088,  0.1755675 ,  0.19738431,  0.22042543,
                0.244589  ,  0.26975916,  0.29580827,  0.32259936,  0.34998862,
                0.377828  ,  0.40596767,  0.43425846,  0.46255411,  0.49071331,
                0.51860153,  0.54609255,  0.57306977,  0.5994272 ,  0.62507019,
                0.64991591,  0.67389356,  0.69694438,  0.71902138,  0.74008905,
                0.76012273,  0.77910799,  0.79703987,  0.81392209,  0.82976609,
                0.84459023,  0.85841887,  0.87128143,  0.88321163,  0.89424658,
                0.90442608,  0.91379189,  0.92238706,  0.93025537,  0.93744079,
                0.94398702,  0.94993712,  0.95533313,  0.96021585,  0.96462454,
                0.96859684])



def rotate(x,y, origin=(0,0)):
    # shift to origin
    x1 = x - origin[0]
    y1 = y - origin[1]

    #rotate
    x2 = -y1
    y2 = x1

    # shift back
    x3 = x2 + origin[1]
    y3 = y2 + origin[0]

    return x3, y3

# now let's do the rotation
origin = (9.,0.5)
a1, b1 = rotate(a,b, origin )
A1, B1 = rotate(A,B, origin )


fig, (ax1, ax2) = plt.subplots(1,2, figsize=(7,3.3))

ax1.set_title("original")
ax1.scatter(a, b, color = "blue", marker = 'o', s = 20)
ax1.plot(A, B, 'r-')

ax2.set_title(u"90° ccw rotated")
ax2.scatter(a1, b1, color = "blue", marker = 'o', s = 20)
ax2.plot(A1, B1, 'r-')

plt.show()