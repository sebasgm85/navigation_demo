#!/usr/bin/env python
import roslib; roslib.load_manifest('kobuki_msgs')
import rospy
import tf
import time
from geometry_msgs.msg import PoseWithCovarianceStamped, Point, Quaternion, Pose, PoseWithCovariance, PoseStamped
from move_base_msgs.msg import MoveBaseGoal

def set_goalpose():
    
    location =  Pose(Point(10.0, 10.0, 0.0), Quaternion(0.0, 0.0, 0.372749678514, 0.927931935633))
    goal = PoseStamped()
    goal.pose = location
    goal.header.frame_id = '/map'
    goal.header.stamp = rospy.Time.now()

    return goal


if __name__ == '__main__':
    rospy.init_node('goalpose_pub')
    pub_goalpose = rospy.Publisher('/move_base_simple/goal', PoseStamped)
    time.sleep(0.5)

    try:
        goal = set_goalpose()
        pub_goalpose.publish(goal)
    except rospy.ROSInterruptException:
        pass
