#!/usr/bin/env python

"""
Author: Preston Ward
Date: 6/30/2023
"""

import rospy
from sensor_msgs.msg import JointState
import baxter_interface
import os

"""
This code is a pick and place demo creator. By running this script,
you can move Baxter's arms and save their angles as well as save gripper actions
This can be translated to other robots as well, as joint names and rostopic names are updated
"""

angles = []
current_angles_dict = {}
gripper_actions = []
default_gripper_action = "open"
joint_names = ['head_nod', 'head_pan','left_e0','left_e1','left_s0','left_s1','left_w0','left_w1','left_w2', 'right_e0','right_e1','right_s0','right_s1','right_w0','right_w1','right_w2']
file_path = ""
numButtons = 0
current_joint_state = None



def callback(data):
    global angles, current_angles_dict
    current_angles_dict = dict(zip(data.name,data.position))

def keyboard_input_callback():
    global angles, gripper_actions, numButtons, current_angles_dict, file_path
    key = raw_input("Press s to save a position, c to close, o to open, and q to quit: ")
    if key == 's':
        temp_dict = current_angles_dict

        #checking for strange values
        iterator = iter(temp_dict.items())
        key,value = next(iterator)
        if key == "r_gripper_l_finger_joint":
            #prints red
            print('\033[91m'+"ERROR: Encountered issue when measuring joint_states. Please Try Again"+'\033[0m')
        else:
            #appends angle if angles are found
            #if no gripper action has been sent, it defaults to open
            angles.append(temp_dict)
            print("Saved Position")
            gripper_actions.append(gripper_actions[-1]) if gripper_actions else gripper_actions.append(default_gripper_action)
            numButtons += 1
    elif key == 'c':
        #appends gripper action 'close'
        angles.append(angles[-1] if angles else  None)
        print("Saved Close")
        gripper_actions.append("close")
        numButtons += 1
    elif key == 'o':
        #appends gripper action 'open'
        angles.append(angles[-1] if angles else  None)
        print("Saved Open")
        gripper_actions.append("open")
        numButtons += 1
    elif key == 'q':
        #saves arrays into file
        file_name = raw_input("Enter the name of the demo: ")
        subdirectory = "src/baxter_demo_maker/demos/"
        file_path = os.path.join(subdirectory, file_name)
        if not os.path.exists(subdirectory):
        os.makedirs(subdirectory)
        rospy.signal_shutdown("Done capturing")
    else:
        print("Invalid Input")

def save_data():
    with open(file_path, 'w') as f:
        for i in range(numButtons):
            f.write(str(angles[i]) + ";" + str(gripper_actions[i]))
            f.write('\n\n')

def main():
    #creates ROS nodes and enables Baxter robot
    rospy.init_node('waypoints')
    robot = baxter_interface.RobotEnable()
    robot.enable()
    rospy.Subscriber("/robot/joint_states", JointState, callback)

    #continously repeats functions
    while not rospy.is_shutdown():
        keyboard_input_callback()
        save_data()

if __name__ == "__main__":
    main()
