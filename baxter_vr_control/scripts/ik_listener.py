#!/usr/bin/env python
import rospy
import moveit_commander as mc
import sys
import time
import copy
import geometry_msgs.msg
from unity_baxter_msg.msg import controllerPos



rospy.init_node('L_IK_solver', anonymous=True)

def calculate_IK(group_name, left_target_pose, right_target_pose):
	joint_state_topic = ['joint_states:=/robot/joint_states']
	mc.roscpp_initialize(joint_state_topic)

	robot = mc.RobotCommander()
	group = mc.MoveGroupCommander(group_name)

    	left_current_pose = group.get_current_pose(end_effector_link='left_gripper').pose
    	right_current_pose = group.get_current_pose(end_effector_link='right_gripper').pose

	group.set_pose_target(left_target_pose, end_effector_link='left_gripper')
	group.set_pose_target(right_target_pose, end_effector_link='right_gripper')

	plan=group.plan()
	group.go(wait = True)




def callback(data):
	group_name = "both_arms"
	left_target_pose = geometry_msgs.msg.Pose()
	right_target_pose = geometry_msgs.msg.Pose()
	#set equal to position from unity hand controller
	#currently set to default values for testing
	left_target_pose.position.x = data.leftX  #default to 0.45
	left_target_pose.position.y = data.leftY #default to 0.3
	left_target_pose.position.z = data.leftZ #default to 0.2
	left_target_pose.orientation.x = data.leftRotX
	left_target_pose.orientation.y = data.leftRotY
	left_target_pose.orientation.z = data.leftRotZ
	left_target_pose.orientation.w = data.leftRotW

	right_target_pose.position.x = data.rightX #default to 0.6
	right_target_pose.position.y = data.rightY #default to 0.4
	right_target_pose.position.z = data.rightZ #default to 0.2
	right_target_pose.orientation.x = data.rightRotX
	right_target_pose.orientation.y = data.rightRotY
	right_target_pose.orientation.z = data.rightRotZ
	right_target_pose.orientation.w = data.rightRotW

	calculate_IK(group_name, left_target_pose, right_target_pose)

def listener():
	rospy.Subscriber("controller_pos", controllerPos, callback)
	rospy.spin()

if __name__ == '__main__':
	print("starting Baxter inverse kinematics...")
	listener()
	mc.roscpp_shutdown()
	mc.os._exit(0)
