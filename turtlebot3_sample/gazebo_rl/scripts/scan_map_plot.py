import numpy as np
import math
import matplotlib.pyplot as plt

ranges = np.loadtxt("../data/ranges.txt", delimiter=",")
angle_min = np.loadtxt("../data/angle_min.txt")
angle_max = np.loadtxt("../data/angle_max.txt")
angle_increment = np.loadtxt("../data/angle_increment.txt")
angle = angle_min
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.scatter(0,0)
for r in ranges:
    # change infinite values to 0
    if math.isinf(r) == True:
        continue
    # convert angle and radius to cartesian coordinates
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    print(x, y)
    ax.scatter(x, y)
    angle += angle_increment

plt.show()