#!/usr/bin/env python
import roslib; roslib.load_manifest('kobuki_msgs')
import rospy
import tf
import time
from geometry_msgs.msg import PoseWithCovarianceStamped, Point, Quaternion, Pose, PoseWithCovariance, PoseStamped
from move_base_msgs.msg import MoveBaseGoal

def set_goalpose():
    pub_goalpose = rospy.Publisher('/move_base_simple/goal', PoseStamped)

    location =  Pose(Point(10.0, 0.0, 0.0), Quaternion(0.0, 0.0, 0.1, 0.0))
    goal = PoseStamped()
    goal.pose = location
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = 'map'
    goal.header.stamp = rospy.Time.now()

    return pub_goalpose, goal


if __name__ == '__main__':
    rospy.init_node('goalpose_pub')
    time.sleep(2)
    pub_goalpose, goal = set_goalpose()

    try:
        goal.pose.position.x += 5
        pub_goalpose.publish(goal)
    except rospy.ROSInterruptException:
        pass
