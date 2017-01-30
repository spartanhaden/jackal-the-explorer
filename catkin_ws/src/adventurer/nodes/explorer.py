#!/usr/bin/env python

import rospy
import time
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion

max_trial_time = 600
max_wait_time = 35

# Tested with jackal navigation tutorial


def get_goal():

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.pose.position.x = 1
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
        # Get Randomized Goal Pose values
        goal = get_goal()

        client.send_goal(goal)
        # client.wait_for_result()
        goal_time = time.time()
        # Terminate Goal after max_wait_time
        while not done:

            current_time = time.time()
            if (goal_time + max_wait_time) < current_time:
                done = True
                rospy.loginfo("Setting done to true")
            rate.sleep()
        done = False

    except rospy.ROSInterruptException:
        pass
