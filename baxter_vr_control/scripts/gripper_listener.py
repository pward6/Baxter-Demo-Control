#!/usr/bin/env python
import rospy
from unity_baxter_msg.msg import gripperBool
import baxter_interface
import baxter_examples
import time, sys

rospy.init_node('unity_listener', anonymous=True)
gripper_right = baxter_interface.Gripper('right')
gripper_right.calibrate()

def callback(data):
	if data.gripperOn == 1:
		gripper_right.close()
	elif data.gripperOn == 0:
		gripper_right.open()

def listener():
	rospy.Subscriber("gripper_bool", gripperBool, callback)

	rospy.spin()

if __name__ == '__main__':
	listener()