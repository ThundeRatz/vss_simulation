#!/usr/bin/env python
# coding=utf-8
"""
    File:
        velocity_conversion.py

    Description:
        Simple python routine to convert velocity message
    from Twist format to Float64
"""

import rospy
from gazebo_msgs.msg import Twist

# A vel máxima do robô é 2 m/s
LIN_VEL = 1  # m/s
WHEEL_RADIUS = 0.030  # m
WHEEL_SEPARATION = 0.060 # m

ANG_VEL = LIN_VEL/WHEEL_RADIUS  # rad/s

vel_pub_dir = rospy.Publisher("/robot_0/vss_robot_right_controller/command", Float64, queue_size=1)
vel_pub_esq = rospy.Publisher("/robot_0/vss_robot_left_controller/command", Float64, queue_size=1)

def callback(data):
    vel_lin = data.linear.x
    vel_ang = data.angular.z

    rospy.loginfo(rospy.get_caller_id() + "Linear Velocity: %f \n Angular Velocity: %f", vel_lin, vel_ang)

    vel_dir = Float64(((1.0 * vel_lin) + (vel_ang * WHEEL_SEPARATION / 2)) * ANG_VEL/2)
    vel_esq = Float64(((1.0 * vel_lin) - (vel_ang * WHEEL_SEPARATION / 2)) * ANG_VEL/2)

    vel_pub_dir.publish(vel_dir)
    vel_pub_esq.publish(vel_esq)

def listener():

    rospy.init_node("vel_conversion")
    rospy.Subscriber("steering_topic", Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
