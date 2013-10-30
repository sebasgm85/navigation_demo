#!/usr/bin/env python  
import roslib; roslib.load_manifest('kobuki_msgs')
import rospy
import tf
import time
from geometry_msgs.msg import PoseWithCovarianceStamped, Point, Quaternion, Pose, PoseWithCovariance


def set_initial_pose():
    pub_initialpose = rospy.Publisher('initialpose', PoseWithCovarianceStamped)

    initial_pose_param = {}
    initial_orientation_param = {}

    if rospy.has_param('/cov_factor'): # Represents a covariance proportional factor to reduce or increase the separation of particles
        cov_factor = rospy.get_param('/cov_factor')
    else:
        cov_factor = 1.0

    initial_pose_param["x"] = 1.0
    initial_pose_param["y"] = 1.0
    initial_pose_param["z"] = 0.0

    initial_orientation_param["x"] = 0.0
    initial_orientation_param["y"] = 0.0
    initial_orientation_param["z"] = 0.372749678514
    initial_orientation_param["w"] = 0.927931935633

    if type(initial_pose_param["x"])==float and type(initial_pose_param["y"])==float and type(initial_pose_param["z"])==float and type(initial_orientation_param["x"])==float and type(initial_orientation_param["y"])==float and type(initial_orientation_param["z"])==float and type(initial_orientation_param["w"])==float:
        valid_pose = True
    else:
        valid_pose = False
        rospy.logwarn("Invalid 'initialpose'")

    
    if valid_pose:
        initial_pose = PoseWithCovarianceStamped()
        initial_pose.header.stamp = rospy.Time.now()
        initial_pose.header.frame_id = "/map"
        initial_pose.pose.pose.position = Point(initial_pose_param["x"], initial_pose_param["y"], initial_pose_param["z"])
        initial_pose.pose.pose.orientation = Quaternion(initial_orientation_param["x"], initial_orientation_param["y"], initial_orientation_param["z"], initial_orientation_param["w"])
        initial_pose.pose.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0,
                                        0.06, 0.25, 0.0, 0.0, 0.0, 0.0,
                                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                        0.0, 0.0, 0.0, 0.0, 0.0, 0.06404220844521101]

        if cov_factor != 1.0:
            initial_pose.pose.covariance = [cov_factor*l for l in initial_pose.pose.covariance]

        #pub_initialpose.publish(initial_pose)
        rospy.sleep(1.0)
        str = "Initial pose successfully set"
        rospy.loginfo(str)

	return pub_initialpose, initial_pose

if __name__ == '__main__':
    rospy.init_node('amcl_dummy')
    br = tf.TransformBroadcaster()
    pub_initialpose, initialpose = set_initial_pose()

    try:
        pub_initialpose.publish(initialpose)
    except rospy.ROSInterruptException:
        pass

    while True:
        br.sendTransform((0, 0, 0), tf.transformations.quaternion_from_euler(0, 0, 0), rospy.Time.now(), 'base_footprint', 'map')
        time.sleep(0.2)
        rospy.loginfo("Publishing base_footprint to map transform")
