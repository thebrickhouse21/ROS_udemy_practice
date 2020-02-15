#!/usr/bin/env python



import rospy 
from std_msgs.msg import String

#below is a callback function! important concept in computer programming
def callback_receive_radio_data(msg):
    rospy.loginfo("message recieved : ")
    rospy.loginfo(msg)


if __name__ == '__main__':
    rospy.init_node('smartphone')

    sub = rospy.Subscriber("/robot_news_radio", String, callback_receive_radio_data) #your subscriber!

    rospy.spin()#keeps the subscriber cycling through this code

#general explanation of this program:
#everything below the callback function are similar to everything seen before with creating nodes.
#the difference is that we are passing in a callback function to the "Subscriber" method. 
#this pretty much means that when the subscriber connects to the topic its going to run this 
#function. without it the subscriber does nothing.
    