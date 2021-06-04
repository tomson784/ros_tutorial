import numpy as np
import math
import matplotlib.pyplot as plt

ranges = np.loadtxt("../data/ranges.txt", delimiter=",")
angle_min = np.loadtxt("../data/angle_min.txt")
for r in ranges:
    #change infinite values to 0
    if math.isinf(r) == True:
        r = 0
    #convert angle and radius to cartesian coordinates
    x = math.trunc((r * 30.0)*math.cos(angle_min + (-90.0*3.1416/180.0)))
    y = math.trunc((r * 30.0)*math.sin(angle_min + (-90.0*3.1416/180.0)))

    plt.scatter(x, y)

plt.show()