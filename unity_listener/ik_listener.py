#!/usr/bin/env python
import rospy
import moveit_commander as mc
import sys
import geometry_msgs.msg
from unity_baxter_msg.msg import controllerPos

rospy.init_node('IK_solver')


def calculate_IK(group_name, target_pose):
mc.roscpp_initialize(sys.argv)

robot = mc.RobotCommander()

group = mc.MoveGroupCommander(group_name)

group.set_pose_target(target_pose)

plan=group.plan()
group.execute(plan, wait = True)

mc.roscpp_shutdown()
mc.os._exit(0)


def callback(data):
group_name = "left_arm"
target_pose = geometry_msgs.msg.Pose()
#examples
#set equal to position from unity hand controller
target_pose.position.x = data.leftX
target_pose.position.y = data.leftY
target_pose.position.z = data.leftZ
target_pose.orientation.x = data.leftRotX
target_pose.orientation.y = data.leftRotY
target_pose.orientation.z = data.leftRotZ
target_pose.orientation.w = 1.0
calculate_IK(group_name, target_pose)

def listener():
rospy.Subscriber("controller_pos", controllerPos, callback)

rospy.spin()


if __name__ == '__main__':
listener()