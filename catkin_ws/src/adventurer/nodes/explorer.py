#!/usr/bin/env python

import rospy
import time
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import random

# from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion

# set the maximum time allowed for mapping
max_trial_time = 600


# function to get a random goal pose
# def get_goal():
    # Get Randomized Goal Pose value
    # goal = set_goal()
#    pass


# function to set the random goal
def set_goal():
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.pose.position.x = 10
    goal.target_pose.pose.position.y = 1
    goal.target_pose.pose.position.z = 0
    goal.target_pose.pose.orientation.x = 0
    goal.target_pose.pose.orientation.y = 0
    goal.target_pose.pose.orientation.z = 1
    rospy.loginfo("New Goal Generated")

    return goal


if __name__ == "__main__":

    # arguments for map length and width
    # x = sys.argv[1]
    # y = sys.argv[2]

    rospy.init_node('explorer', anonymous=True)
    rate = rospy.Rate(10)
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()
    done = False

    try:
        goal = set_goal()
        client.send_goal(goal)
        # client.wait_for_result()
        init_time = time.time()
        # Terminate Goal after max_wait_time
        while not done:
            current_time = time.time()
            # enters if loop once max_wait_time is reached
            if (current_time - init_time) > max_trial_time:
                done = True
                # cancel all predefined goals set for the robot
                client.cancel_all_goals()
                rospy.loginfo("Setting done to true")
            rate.sleep()
        done = False

    except rospy.ROSInterruptException:
        pass

