#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import rospkg
import sys

rospack = rospkg.RosPack()
project_root = rospack.get_path("gazebo_rl")

import numpy as np

def callback(data):
    rospy.loginfo(rospy.get_caller_id())
    rospy.loginfo(data.range_min)
    rospy.loginfo(data.range_max)
    rospy.loginfo(data.angle_min)
    rospy.loginfo(data.angle_max)
    rospy.loginfo(data.angle_increment)
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
