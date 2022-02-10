#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt, pi



def update_pose(data):
    pose = data
    pose.x = round(pose.x, 4)
    pose.y = round(pose.y, 4)
        # self.pose.theta = round(self.pose.theta, 4)
        # print('self theta -',abs(self.pose.theta))

def euclidean_distance(goal_pose):
    return sqrt(pow((goal_pose.x - pose.x), 2) + pow((goal_pose.y - pose.y), 2))

def linear_vel(goal_pose, constant=1.5):
    return constant * euclidean_distance(goal_pose)

def steering_angle(goal_pose):
    return atan2(goal_pose.y - pose.y, goal_pose.x - pose.x)

def angular_vel(goal_pose, constant=6):
    return constant * (steering_angle(goal_pose) - pose.theta)

def angular_difference(angle):
    return (angle - pose.theta)

def rotate(angle,constant=1.5):
    return constant* (angular_difference(angle))

    # def rotate(self,goal_pose, constant=1)
    #     return constant * (self.angular_difference(goal_pose))

def move2goal():
    goal_pose = Pose()

    # Get the input from the user.
    x = [0,5,8,8,5,5]
    y = [0,5,5,8,8,5]
    theta = [-3*pi/4,0,pi/2,pi,-pi/2,0]
    distance_tolerance = 0.01
    angle_tolerance = 0.01
    vel_msg = Twist()
    for i in range(6):
        goal_pose.x = x[i]
        goal_pose.y = y[i]

        while euclidean_distance(goal_pose) >= distance_tolerance:
            # print('moving in here',self.euclidean_distance(goal_pose))
            vel_msg.linear.x = 0
            vel_msg.linear.x = linear_vel(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = angular_vel(goal_pose)
            velocity_publisher.publish(vel_msg)
            rate.sleep()

        while abs(angular_difference(theta[i])) >= angle_tolerance:
            # print('rotating in here',angular_difference(theta[i]))
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = rotate(theta[i])
            velocity_publisher.publish(vel_msg)
            rate.sleep()

    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

        
    rospy.spin()

if __name__ == '__main__':
    try:
        rospy.init_node('turtlebot_controller', anonymous=True)

        
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)

       
    
        pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, update_pose)
        pose = Pose()
        rate = rospy.Rate(10)
        data = pose
        update_pose(data)
        move2goal()
        euclidean_distance(goal_pose)
        linear_vel(goal_pose, constant=1.5)
        steering_angle(goal_pose)
        angular_vel(goal_pose, constant=6)
        angular_difference(angle)
        rotate(angle,constant=1.5)
        

    except rospy.ROSInterruptException:
        pass