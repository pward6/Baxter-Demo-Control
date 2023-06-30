#!/usr/bin/python
import rospy
import baxter_interface
import os

rospy.init_node("demo_listener")
right_arm = baxter_interface.Limb('right')
gripper = baxter_interface.Gripper('right')
robot = baxter_interface.RobotEnable()

robot.enable()
gripper.calibrate()

waypoints = []
gripper_actions = []

def parse_demo_file(file_name):
	global gripper_actions, waypoints
	with open(file_name, "r") as f:
		for line in f:
			entries = line.split(';')
			positions = {}
				for entry in entries:
					if entry.startswith("{"):
						entry = entry[1:-1]
						pairs = entry.split(",")

		for pair in pairs:
			key_value = pair.split(":", 1)
			if len(key_value) == 2:
			key,value = key_value
			key = key.strip()
			key = key[1:-1]
			value = value.strip()
				if key.startswith("right_"):
					positions[key] = float(value)

		if positions:
			waypoints.append(positions)
		else:
			gripper = entry.strip()
			if gripper:
				gripper_actions.append(gripper)


def execute_actions(waypoints,gripper_actions):
	print("Moving through waypoints...\n")
	for i in range(len(waypoints)):
		right_arm.move_to_joint_positions(waypoints[i])
		if gripper_actions[i] == "open":
			gripper.open()
		elif gripper_actions[i] == "close":
			gripper.close()
		rospy.sleep(1)

def main():
	global waypoints, gripper_actions, robot
	demo_file = raw_input("Enter the demo file you'd like to run: ")
	subdirectory = "~/ros_ws/src/baxter_demo_maker/demos/"
	file_path = os.path.expanduser(os.path.join(subdirectory, demo_file))
	if not os.path.exists(subdirectory):
		os.makedirs(subdirectory)
		parse_demo_file(file_path)
	execute_actions(waypoints, gripper_actions)

	robot.disable()

if __name__ == '__main__':
	main()
