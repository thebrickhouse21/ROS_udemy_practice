#!/usr/bin/env python



import rospy 
from std_msgs.msg import Int64
from std_srvs.srv import SetBool #importing the server for our reset service 

i = Int64() #counter type (global)
def callback_recieved_number(msg): #call back function....there are more than one way to implement a counter
                                    #some may do it directly in the callback function which is cool 
                                    #just make sure you define pub=none globally 
    rospy.loginfo(msg)#display the number

def callback_reset_counter(req): #this is our callback function for the service, it's pretty simple it just takes in the req parameter
    if req.data:                #and sets the global counter variable "i" to zero and sends a message based on what you sent 
        i.data = 0              #the service True or False.
        return True, "Counter has been reset"
    return False, "Counter has NOT been reset :("

if __name__ == '__main__':
    rospy.init_node('number_counter') #init node

    sub = rospy.Subscriber("/number", Int64, callback_recieved_number) #init subscriber
    

    pub = rospy.Publisher("/number_counter", Int64, queue_size=10) #init publisher
    
    
    reset_service = rospy.Service("/reset_counter", SetBool, callback_reset_counter) #init reset service, notice since SetBool is our data type we can 
                                                                                    #only send a True or False value when calling the service.

    rate = rospy.Rate(1)#set rate

    while not rospy.is_shutdown(): #this runs for the publisher this way the counter is counted while the node is up 
        i.data = i.data + 1 #increment counter

        pub.publish(i) #publish to topic
        rate.sleep() #const rate

    rospy.loginfo("Node was stopped") #log this when node is stopped

    #this is a cool chunk of code because this node is both a publisher and subscriber & has the reset service! WOW!
    #publishing to /number_counter topic
    #subscribing to /number topic 
    #service is on /reset_counter