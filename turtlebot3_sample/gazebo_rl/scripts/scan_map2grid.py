import numpy as np
import math
import matplotlib.pyplot as plt

ranges = np.loadtxt("../data/ranges.txt", delimiter=",")
angle_min = np.loadtxt("../data/angle_min.txt")
angle_max = np.loadtxt("../data/angle_max.txt")
angle_increment = np.loadtxt("../data/angle_increment.txt")
angle = angle_min + math.pi/2
range_max = np.loadtxt("../data/range_max.txt")

grid_num = 40
resolution = 2*range_max / grid_num

# 範囲の下限値が決まっている場合
def real2grid_index(x, y, x_min, y_min, resolution):
    return math.floor((x-x_min)/resolution),\
           math.floor((y-y_min)/resolution)

# グリッド数が固定される場合
def real2grid_index_fixed_grid_num(x, y, w, h, resolution):
    return math.floor(x/resolution + w/2),\
           math.floor(y/resolution + h/2)

obs_map = np.zeros([grid_num, grid_num])

for r in ranges:
    if math.isinf(r) == True:
        angle += angle_increment
        continue
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    x_idx, y_idx = real2grid_index_fixed_grid_num(x, y, grid_num, grid_num, resolution)
    # x_idx, y_idx = real2grid_index_fixed_grid_num(x, y, -3.5, -3.5, resolution)
    obs_map[grid_num-y_idx][x_idx] = 1
    angle += angle_increment

robot_x_idx, robot_y_idx = real2grid_index_fixed_grid_num(0, 0, grid_num, grid_num, resolution)
obs_map[grid_num-robot_y_idx][robot_x_idx] = 2

plt.imshow(obs_map)
plt.show()