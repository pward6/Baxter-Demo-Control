cmake_minimum_required(VERSION 2.8.3)
project(unity_baxter_msg)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

add_message_files(
  FILES
  gripperBool.msg
  controllerPos.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(

)
include_directories(
# include
  ${catkin_INCLUDE_DIRS}

)