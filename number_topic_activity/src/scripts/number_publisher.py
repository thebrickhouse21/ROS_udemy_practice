#!/usr/bin/env python

import random #new library used! this helps us get random numbers!
import rospy 
from std_msgs.msg import Int64 #Now importing a 64 bit integer instead of a string 
msg =  Int64() #message type (goabal)

if __name__ == '__main__':

    rospy.init_node("number_publisher") #init node
    # !!!!!!!!!!!! for multiple publishers use this code----> rospy.init_node("number_publisher", anonymous=True)

    pub = rospy.Publisher("/number", Int64, queue_size=10) #init pub

    rate = rospy.Rate(1)#init rate

    while not rospy.is_shutdown(): #while the the node is running
        msg.data = random.randint(1,20) #assign a random int to the data
        pub.publish(msg) #publish data
        rate.sleep() #constant rate
    rospy.loginfo("node was stopped")#logged when node is stopped