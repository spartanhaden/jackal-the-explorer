#!/usr/bin/env python

import rospy


def begin():
    rospy.init_node("explorer")


if __name__ == "__main__":
    try:
        begin()
    except rospy.ROSInterruptException:
        pass
