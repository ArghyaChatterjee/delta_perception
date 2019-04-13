#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author  : Heethesh Vhavle
Email   : heethesh@cmu.edu
Version : 1.0.0
Date    : Apr 13, 2019
'''

# Python 2/3 compatibility
from __future__ import print_function, absolute_import, division

# ROS modules
import rospy

# ROS messages
from visualization_msgs.msg import Marker


########################### Functions ###########################


def make_label(text, position, id=0, duration=0, color=[1.0, 1.0, 1.0]):
    """ 
    Helper function for generating visualization markers
    
    Args:
        text (str): Text string to be displayed.
        position (list): List containing [x,y,z] positions
        id (int): Integer identifying the label
        duration (rospy.Duration): How long the label will be displayed for
        color (list): List of label color floats from 0 to 1 [r,g,b]
    
    Returns: 
        Marker: A text view marker which can be published to RViz
    """
    marker = Marker()
    marker.header.frame_id = '/map'
    marker.id = id
    marker.type = marker.TEXT_VIEW_FACING
    marker.text = text
    marker.action = marker.ADD
    marker.scale.x = 0.05
    marker.scale.y = 0.05
    marker.scale.z = 0.05
    marker.color.a = 1.0
    marker.color.r = color[0]
    marker.color.g = color[1]
    marker.color.b = color[2]
    marker.lifetime = rospy.Duration(duration)
    marker.pose.orientation.w = 1.0
    marker.pose.position.x = position[0]
    marker.pose.position.y = position[1]
    marker.pose.position.z = position[2]
    return marker


def make_cuboid(position, scale, id=0, duration=0, color=[1.0, 1.0, 1.0]):
    """ 
    Helper function for generating visualization markers
    
    Args:
        position (list): List containing [x, y, z] positions
        scale (list): List containing [x, y, z] dimensions
        id (int): Integer identifying the label
        duration (rospy.Duration): How long the label will be displayed for
        color (list): List of label color floats from 0 to 1 [r, g, b]
    
    Returns: 
        Marker: A cube marker which can be published to RViz
    """
    marker = Marker()
    marker.header.frame_id = '/map'
    marker.id = id
    marker.type = marker.CUBE
    marker.text = str(id)
    marker.action = marker.ADD
    marker.scale.x = scale[0]
    marker.scale.y = scale[1]
    marker.scale.z = scale[2]
    marker.color.a = 1.0
    marker.color.r = color[0]
    marker.color.g = color[1]
    marker.color.b = color[2]
    marker.lifetime = rospy.Duration(duration)
    marker.pose.orientation.w = 1.0
    marker.pose.position.x = position[0]
    marker.pose.position.y = position[1]
    marker.pose.position.z = position[2]
    return marker


def publisher():
    # Setup node
    rospy.init_node('marker_publisher', anonymous=True)
    pub = rospy.Publisher('marker_publisher', Marker, queue_size=10)
    
    # Publish rate
    r = rospy.Rate(0.25)

    # Randomly publish some data
    while not rospy.is_shutdown():
        # Create the message array
        msg = make_cuboid([0, 0, 0], [0.05, 0.05, 0.05])
        
        # Header stamp and publish the message
        msg.header.stamp = rospy.Time.now()
        pub.publish(msg)

        # Sleep
        r.sleep()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
