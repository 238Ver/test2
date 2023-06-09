import numpy as np
import matplotlib.pyplot as pl

a = np.array([4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9])
b = np.array([i/len(a) for i in range(1, len(a)+1)])
aa = np.array([i/10 for i in range(40, 91)])
ss = np.array([ 0.06200455,  0.07389492,  0.08721351,  0.10198928,  0.11823225,
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

pl.scatter(a,b,color = "blue", marker = 'o', s = 20)
pl.plot(aa, ss, 'r-')
pl.show()