#!/usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist
square = [2,2,2,2]

def straight_path():

    # linear velocity and distance to cover in one direction
    speed = 0.2
    distance = 2

    # Since turtle moving just in x-axis
    vel_msg.linear.x = 0.2
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    # Getting current time set 
    t0 = rospy.Time.now().to_sec()
    # Setting the current time for distance calculus
    current_distance = 0
    # Loop to move the turtle in an specified distance
    while(current_distance < distance):
        # Publish the velocity
        velocity_publisher.publish(vel_msg)
        # Takes actual time to velocity calculus
        t1 = rospy.Time.now().to_sec()
        # Calculates distancePoseStamped
        current_distance = speed*(t1 - t0)
    # After the loop, stops the robot
    vel_msg.linear.x = 0
    # Force the robot to stop
    velocity_publisher.publish(vel_msg)

def rotate():
    # angular velocity and direction
    angular_velocity = 0.2
    desired_angle = abs(math.radians(90))

    # Since turtle rotate in only z-axis
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = angular_velocity

    t0 = rospy.Time.now().to_sec()
    current_angle = 0
    while(current_angle < desired_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_velocity*(t1 - t0)

    vel_msg.linear.z = 0
    velocity_publisher.publish(vel_msg)


if __name__ == '__main__':
    try:
        # Testing our function
        rospy.init_node('square_openloop')
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
        vel_msg = Twist()
        for i in range(len(square)):
            straight_path()
            rotate()
    except rospy.ROSInterruptException:
        pass
