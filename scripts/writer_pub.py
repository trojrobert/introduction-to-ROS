#!/usr/bin/env python

import rospy # This module is used to write ROS node in python(http://wiki.ros.org/rospy/Overview)
from std_msgs.msg import String # This module is responsible for the message type 

def writer():
    """Create a Publisher and send message through a topic"""
    
    # initiate a publisher node called "writer_node"
    # anonymous=True ensure every node is unique by adding random to end of a name 
    rospy.init_node('writer_node', anonymous=True)

    # ensures  the publisher publish to topic "/print_topic" with message type "String"
    # queue_size is the limit to the number of messages in queued messages 
    pub = rospy.Publisher('/print_topic', String, queue_size=10)

    # looping at a desired rate, the number of times per second to go through the while loop
    rate = rospy.Rate(1)
 
    # ensure the rospy is running until the program is shutdown 
    while not rospy.is_shutdown():
   
        writer_str = "Hello world, this is the message published   %s" % rospy.get_time()
        
	# Print message to screen, write message to node log file
	# write message to rosout
        rospy.loginfo(writer_str)

	# publish "writer_str" to topic "/print_topic"
        pub.publish(writer_str)

        # ensures the loop sleep for some seconds just like time.sleep 
        rate.sleep()

if __name__ == '__main__':
    try:
        writer()
    except rospy.ROSInterruptException:
        pass

