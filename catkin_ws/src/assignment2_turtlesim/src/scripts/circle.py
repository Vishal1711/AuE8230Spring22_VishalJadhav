#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


def circle():
    
    # Creates a new node with name 'circle' and make sure it is unique node using (anonymous=True) 
    rospy.init_node('circle', anonymous=True)
    # Publisher which will publish to topic /turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)


    #Create twist msgs which broke velocity into its linear and angular parts
    move_cmd = Twist()
    move_cmd.linear.x = 1.0
    move_cmd.angular.z = 1.0      # Constant twist velocity


    # Getting current time set publish rate
    current_time = rospy.Time.now()
    # go through the loop 10 times per second (10 Hz)
    rate = rospy.Rate(10)

    while rospy.Time.now() < current_time + rospy.Duration.from_sec(5.7):
        velocity_publisher.publish(move_cmd)
        rate.sleep()
        
        
if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass
