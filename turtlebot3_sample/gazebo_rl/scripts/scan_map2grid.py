import numpy as np
import math
import matplotlib.pyplot as plt

ranges = np.loadtxt("../data/ranges.txt", delimiter=",")
angle_min = np.loadtxt("../data/angle_min.txt")
angle_max = np.loadtxt("../data/angle_max.txt")
angle_increment = np.loadtxt("../data/angle_increment.txt")
angle = angle_min

grid_num = 40
resolution = 0.1

# 範囲の下限値が決まっている場合
def real2grid_index(x, y, x_min, y_min, resolution):
    return math.floor((x-x_min)/resolution),\
           math.floor((y-y_min)/resolution)

# グリッド数が固定される場合
def real2grid_index_fixed_grid_num(x, y, w, h, resolution):
    return math.floor(x/resolution - w/2),\
           math.floor(y/resolution - h/2)

for r in ranges:
    # change infinite values to 0
    if math.isinf(r) == True:
        continue
    # convert angle and radius to cartesian coordinates
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    angle += angle_increment


