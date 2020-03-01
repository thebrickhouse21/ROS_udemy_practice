#!/usr/bin/env python

import rospy 
from my_robot_msgs.msg import HardwareStatus

if __name__ == '__main__':
    rospy.init_node("hardware_status_publisher")

    

    pub = rospy.Publisher("/my_robot/hardware_status", HardwareStatus, queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        msg = HardwareStatus()
        msg.temperature = 45
        rospy.loginfo("i am on like ron")
        msg.are_motors_up = True
        msg.debug_message = "Everything is running well"
        pub.publish(msg)
        rate.sleep()