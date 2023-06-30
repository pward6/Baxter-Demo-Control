# Baxter-Demo-Control
This branch allows the user to quicklt script demos and save them for future use

## Running
To create a demo, run ``roslaunch baxter_demo_maker demoMaker.py`` and press 's' to save joint angles. Once you're done, you can save the joint angles and gripper actions in a .txt file, which you can save for future use.
To run a demo, run ``roslaunch baxter_demo_maker demoListener.py`` and type the name of the file.
Inside the scripts, make sure the subdirectory pathing is updated to where you save this repository. Right now it's coded to "~/ros_ws/src/baxter_demo_maker/demos"

A GUI with TKInter is in the works and will be added soon.
