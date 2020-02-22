#!/usr/bin/env python



import rospy 
from std_msgs.msg import Int64
i = Int64() #counter type (global)
def callback_recieved_number(msg): #call back function....there are more than one way to implement a counter
                                    #some may do it directly in the callback function which is cool 
                                    #just make sure you define pub=none globally 
    rospy.loginfo(msg)#display the number


if __name__ == '__main__':
    rospy.init_node('number_counter') #init node

    sub = rospy.Subscriber("/number", Int64, callback_recieved_number) #init subscriber
    

    pub = rospy.Publisher("/number_counter", Int64, queue_size=10) #init publisher
    rate = rospy.Rate(1)#set rate
    
    while not rospy.is_shutdown(): #this runs for the publisher this way the counter is counted while the node is up 
        i.data = i.data + 1 #increment counter

        pub.publish(i) #publish to topic
        rate.sleep() #const rate

    rospy.loginfo("Node was stopped") #log this when node is stopped

    #this is a cool chunk of code because this node is both a publisher and subscriber
    #publishing to /number_counter topic
    #subscribing to /number topic 