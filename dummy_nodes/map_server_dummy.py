#!/usr/bin/env python
import rospy
import roslib; roslib.load_manifest('kobuki_msgs')
#from geometry_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction
from nav_msgs.msg import OccupancyGrid, MapMetaData


if __name__ == "__main__":

    pub_mapserver = rospy.Publisher('map', OccupancyGrid)
    pub_mapserver_metadata = rospy.Publisher('map_metadata', MapMetaData)
    rospy.init_node('map_server_dummy')
    rate = rospy.Rate(3) # 3Hz
    occ_grid = OccupancyGrid()
    
    occ_grid.header.stamp.secs = 1381944789
    occ_grid.header.stamp.secs = 447167907
    occ_grid.header.frame_id = "map"
    occ_grid.info.resolution = 0.05
    occ_grid.info.width = 512
    occ_grid.info.height = 480
    occ_grid.info.origin.position.x = 0.0
    occ_grid.info.origin.position.y = 0.0
    occ_grid.info.origin.position.z = 0.0
    occ_grid.info.origin.orientation.x = 0.0
    occ_grid.info.origin.orientation.y = 0.0
    occ_grid.info.origin.orientation.z = 0.0
    occ_grid.info.origin.orientation.w = 1.0
    occ_grid.data = [0 for i in range(512*480)]

    metadata = MapMetaData()

    metadata.map_load_time.secs = 1381949468
    metadata.map_load_time.nsecs = 318325596
    metadata.resolution = 0.05
    metadata.width = 512
    metadata.height = 480
    
    metadata.origin.position.x = 0.0
    metadata.origin.position.y = 0.0
    metadata.origin.position.z = 0.0
    metadata.origin.orientation.x = 0.0
    metadata.origin.orientation.y = 0.0
    metadata.origin.orientation.z = 0.0
    metadata.origin.orientation.w = 1.0
	
    while not rospy.is_shutdown(): 
        pub_mapserver.publish(occ_grid)
        pub_mapserver_metadata.publish(metadata)
        rate.sleep()

