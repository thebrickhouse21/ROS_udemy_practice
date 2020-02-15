#!/usr/bin/env python



import rospy
from std_msgs.msg import String #new import so you can add strings to your publisher

if __name__ == '__main__':

    rospy.init_node('robot_news_radio_transmitter') #initialize the node(the name)

    #creating a publisher, youre passing in the name of it, String(so it knows its a string, and a que size (tells the subscriber how long to wait for data))
    pub = rospy.Publisher("/robot_news_radio", String, queue_size=10)

    rate = rospy.Rate(2) #add a rate for your node in hertz

    while not rospy.is_shutdown(): #while loop to keep the node running until stopped
        msg = String() #tells the program that your data is a string 
        msg.data = "Hi, this is Dan from the Robot News Radio!" #assign data 
        pub.publish(msg) #publish the data to your publisher 
        rate.sleep() #keep the rate constant 

    rospy.loginfo("Node was stopped") #log this when the while loop is stopped 