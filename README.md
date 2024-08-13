# Baxter-Demo-Control
This is a multi-stage robotics project with the goal of bring the Baxter robot "back to life." v1 is a hard-coded pick and place, to show Baxter's capability to manipulate small electronics on a breadboard. v1.5 expands on this, adding the capability to easily create demos and save them, allowing for future usage. v2 adds virtual reality to give the user full control and free movement.
Each demo has pros and cons, such as simplicity and precision.

Each demo is stored in the associated git branch.

## Setup
This project uses a Baxter robot from Rethink Robotics. The ROS side ran on an Oracle virtual machine with Ubuntu 14.04 and ROS Indigo. On the windows side, I used Unity 2021.3.18f1 with an Oculus Quest v2 and a Xbox Kinect. Other versions of Unity caused compatability errors, but other VR headsets and Kinect setups would work.

## Running Demos
To run each demo, simply run ``roslaunch baxter_vr_control ik_solver.py`` or ``roslaunch baxter_demo_make demoMaker.py``. Change the python script depending on what you want to run.
