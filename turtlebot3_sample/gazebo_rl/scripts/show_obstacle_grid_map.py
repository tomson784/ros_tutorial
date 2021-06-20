#!/usr/bin/env python
# -*- coding: utf-8 -*-

# lidarの /scan topic を受け取るスクリプト

import rospy
from sensor_msgs.msg import LaserScan
import rospkg
import sys

rospack = rospkg.RosPack()
project_root = rospack.get_path("gazebo_rl")

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

def callback(data):
    rospy.loginfo(rospy.get_caller_id())
    # レーザーの最小照射距離
    rospy.loginfo(data.range_min)
    # レーザーの最大照射距離
    rospy.loginfo(data.range_max)
    # レーザーの照射範囲（角度）
    rospy.loginfo(data.angle_min)
    # レーザーの照射範囲（角度）
    rospy.loginfo(data.angle_max)
    # レーザーの照射間隔（角度）
    rospy.loginfo(data.angle_increment)
    img_array = np.random.rand(40, 40)
    image = ax.imshow(img_array)
    plt.pause(0.1)
    image.remove()


rospy.init_node('sub_scan', anonymous=True)
rospy.Subscriber("/scan", LaserScan, callback)
rospy.spin()
