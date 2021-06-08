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
    # lidarから見た物体の距離
    # 配列はangle_minからangle_maxまでをangle_incrementで刻んだ角度に対応
    np.savetxt(project_root + "/data/ranges.txt", data.ranges, fmt="%.6e", delimiter=",")
    # np.savetxt(project_root + "/data/range_min.txt", data.range_min, fmt="%.6e", delimiter=",")
    # np.savetxt(project_root + "/data/range_max.txt", data.range_max, fmt="%.6e", delimiter=",")
    # np.savetxt(project_root + "/data/angle_min.txt", data.angle_min, fmt="%.6e", delimiter=",")
    # np.savetxt(project_root + "/data/angle_max.txt", data.angle_max, fmt="%.6e", delimiter=",")
    # np.savetxt(project_root + "/data/angle_increment.txt", data.angle_increment, fmt="%.6e", delimiter=",")
    sys.exit(0)

def listener():

    # in ROS, nodes are unique named. If two nodes with the same
    # node are launched, the previous one is kicked off. The 
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaenously.
    rospy.init_node('sub_scan', anonymous=True)

    rospy.Subscriber("/scan", LaserScan, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
        
if __name__ == '__main__':
    listener()
