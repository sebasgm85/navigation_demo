#!/usr/bin/env python  
import roslib; roslib.load_manifest('kobuki_msgs')
import rospy
import tf
import time
from geometry_msgs.msg import PoseWithCovarianceStamped, Point, Quaternion, Pose, PoseWithCovariance


def new_initialpose(initial_pose):
    br = tf.TransformBroadcaster()
    #convert = tf.TransformListener()
    #position, orientation = convert.lookupTransform('base_footprint', data.header.frame_id, data.header.stamp)
    position = (float(initial_pose.pose.pose.position.x), float(initial_pose.pose.pose.position.y), float(initial_pose.pose.pose.position.z))
    orientation = (float(initial_pose.pose.pose.orientation.x),float(initial_pose.pose.pose.orientation.y), float(initial_pose.pose.pose.orientation.z),float(initial_pose.pose.pose.orientation.w))
    br.sendTransform(position, orientation, rospy.Time.now(), 'map', 'base_footprint')
    rospy.loginfo("Publishing new initial pose")


if __name__ == '__main__':
    rospy.init_node('amcl_dummy')
    rate= rospy.Rate(1) # HZ
    rospy.Subscriber('initialpose', PoseWithCovarianceStamped, new_initialpose)
    br = tf.TransformBroadcaster()
    #convert = tf.TransformListener()

    try:
        #convert.waitForTransform('base_footprint', '/map', rospy.Time.now(), rospy.Duration(30.0))
        #position, orientation = convert.lookupTransform('base_footprint', 'map', rospy.Time.now())    
        #br.sendTransform(position, orientation, rospy.Time.now(), 'base_footprint', 'odom')
        while not rospy.is_shutdown():
            br.sendTransform((0, 0, 0), tf.transformations.quaternion_from_euler(0, 0, 0), rospy.Time.now(), 'base_footprint', 'odom')
            br.sendTransform((0, 0, 0), tf.transformations.quaternion_from_euler(0, 0, 0), rospy.Time.now(), 'odom', 'map')
            rospy.loginfo("Publishing base_footprint to map transform")
            rate.sleep()
            #rospy.spin()
    except rospy.ROSInterruptException:
        pass

