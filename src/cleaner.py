#!/usr/bin/env python
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt,pi

class turtlebot():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('cleaner', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    #Callback function implementing the pose value received
    def callback(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def get_distance(self, goal_x, goal_y):
        return sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
    
    def get_angle_to_goal(self, goal_x, goal_y):
        return atan2(goal_y - self.pose.y, goal_x - self.pose.x)

    def move2goal(self, goal_x, goal_y, tolerance):
        goal_pose = Pose()
        goal_pose.x = goal_x
        goal_pose.y = goal_y
        distance_tolerance = tolerance

        vel_msg = Twist()
        
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0

        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        
        dist = self.get_distance(goal_pose.x, goal_pose.y)
        
        while dist >= distance_tolerance and not rospy.is_shutdown():

            #Proportional Controller
            #linear velocity in the x-axis:
            vel_msg.linear.x = 1.5 * dist
            if (vel_msg.linear.x > 2.0):
            	vel_msg.linear.x = 2.0

            #angular velocity in the z-axis:
            ang_to_goal = self.get_angle_to_goal(goal_pose.x, goal_pose.y)
            ang_dif = (ang_to_goal - self.pose.theta)            
            if( (ang_dif) >= (pi) ):
                 ang_dif = ang_dif-(2*pi)
            if( (ang_dif) < -(pi) ):
                 ang_dif = ang_dif+(2*pi)             
            vel_msg.angular.z = 4 * (ang_dif)

            #Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
            
            dist = self.get_distance(goal_pose.x, goal_pose.y)

            
        #Stopping our robot after the movement is over
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        self.velocity_publisher.publish(vel_msg)
        return
   
    def cleaner(self):
        A = [ [1,1],[1,10], [2,10],[2,1], [3,1],[3,10], [4,10],[4,1], [5,1],[5,10], [6,10],[6,1], [7,1],[7,10], [8,10],[8,1], [9,1],[9,10], [10,10], [10,1]]

        for X in A:
                print("Position_x = ", X[0], " Position_y = ", X[1])
                self.move2goal(X[0], X[1], 0.3)
        rospy.spin()
        
if __name__ == '__main__':
    try:
        #Testing our function
        x = turtlebot()
        x.cleaner()

    except rospy.ROSInterruptException: 
        pass
