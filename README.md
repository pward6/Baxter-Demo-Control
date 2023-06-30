# Baxter-Virtual-Reality
A robotics project with the Telecommunications Engineering Laboratory at the University of Nebraska - Omaha. I am developing an application to communicate between Unity and ROS in order to control a Baxter Robot with an Oculus Quest 2 VR Headset.

## Setup
This project uses a Baxter robot from Rethink Robotics. The ROS side ran on an Oracle virtual machine with Ubuntu 14.04 and ROS Indigo. On the windows side, I used Unity 2021.3.18f1. Other versions of Unity caused compatability errors. 

## Connecting to Unity
I used ROS TCP Connector from [Unity Robotics Hub](https://github.com/Unity-Technologies/Unity-Robotics-Hub/tree/main), connecting to my VM's IP address on port 9090. Running ``roslaunch ros_tcp_endpoint endpoint.launch ip_port:=192.XXX.XXX.X tcp_port:=9090``
Clone this repository into the /src file in your VM and your local machine. Generate messages using the msg folders and following the tutorials on Unity Robotics Hub. The C# scripts establish a websocket on Unity that publishes to a gripper and controller position topics on the ROS server. 

## Controlling the Robot
This project leverages ROSBridge to communicate between ROS and a windows machine. ROSBridge is a series of programs that allows developers to create websockets. Additionally, I used the Moveit! API to implement an inverse kinematics solver to control the arms. Moveit! is part of Baxter's sdk, which allows for simple development. 

To start the IK solver, run the moveit_start.launch folder ``roslaunch baxter_vr_control moveit_start.launch`` and then run the python script with ``rosrun baxter_vr_control baxterIK.py``
