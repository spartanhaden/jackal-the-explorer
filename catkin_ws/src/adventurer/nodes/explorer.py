#!/usr/bin/env python

import rospy
import time
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
#from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion

seq_id = 0


def getGoal():

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.pose.position.x = -10.1
    goal.target_pose.pose.position.y = 15.1
    goal.target_pose.pose.position.z = 0
    goal.target_pose.pose.orientation.x = 0
    goal.target_pose.pose.orientation.y = 0
    goal.target_pose.pose.orientation.z = 1

    client.send_goal(goal)
    client.wait_for_result()


if __name__ == "__main__":

    rospy.init_node('explorer', anonymous=True)
    rate = rospy.Rate(10)
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    try:

        client.wait_for_server()
        getGoal()
        rate.sleep()

    except rospy.ROSInterruptException:
        pass
