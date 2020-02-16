#!/usr/bin/env python


import rospy #imports the python library for ros 

if __name__ == '__main__': #if statement that checks for ros 
    rospy.init_node('my_first_node') #start node

    rospy.loginfo("this node has been started") #if you want to put information in the terminal when node is run

    rate = rospy.Rate(10) #sets the rate in hertz of how much the ros node will execute 

    while not rospy.is_shutdown(): #runs the node until it is stopped by the user 
        rospy.loginfo("hello!!")
        rate.sleep() #holds the rate constant while node is running 
        
    #rospy.sleep(1) #will kill the node after 1 second

    #rospy.loginfo("exit now")