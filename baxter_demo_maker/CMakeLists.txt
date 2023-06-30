cmake_minimum_required(VERSION 2.8.3)
project(baxter_demo_maker)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  sensor_msgs
)

generate_messages(
  DEPENDENCIES
  std_msgs
  sensor_msgs
)

catkin_package(
)
include_directories(
# include
  ${catkin_INCLUDE_DIRS}

)