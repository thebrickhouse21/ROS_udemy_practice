#!/usr/bin/env python

import rospy 
from std_msgs.msg import Int64

def callback_nice_number(msg):
    rospy.loginfo("The number is: "+ str(msg))

def callback_nice_counter(i):
    rospy.loginfo("The count is: "+ str(i))

if __name__ == '__main__':
    rospy.init_node("nice_display")


    sub2 = rospy.Subscriber("/number_counter", Int64, callback_nice_counter)
    sub1 = rospy.Subscriber("/number", Int64, callback_nice_number)
    

    rospy.spin()


    #the goal of this node is to subscribe to both topics given and display the data in a easy to read way
    #must make sure the other publishers are running first 
    #the "data:" part still gets displayed which is annoying but whatever
    #this is still a bit buggy I might revisit later.
    