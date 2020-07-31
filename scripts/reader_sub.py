#!/usr/bin/env python

import rospy  #This module is used to write ROS node in python
from std_msgs.msg import String # This module is responsible for the message type

def callback(message):

    """Print message received from the subscriber
    
    args:
        message(str): The message received by the subscriber        

    """
    # Print message to screen, write message to node log file
    # write message to rosout
    rospy.loginfo("Caller - "+ rospy.get_caller_id() + " I received - %s", message.data)
  
def reader():
    """Create a subscriber and receive message from a topic"""

    # initiate a subscriber node called "reader_node"
    # anonymous=True ensure every node is unique by adding random numbers to end
    rospy.init_node('reader_node', anonymous=True)

    # ensures  the subscriber subscribes to topic "/print_topic" with message type "String"
    # the subscriber subscribe to topic "/print_topic" which is same as the topic that 
    # the Publisher publish to, with the same message type “string”, then call the callback function
    rospy.Subscriber('/print_topic', String, callback)

    # ensure the python program does not exit, that is it keeps it in execution mode
    rospy.spin()
    
if __name__ == '__main__':
    reader()
