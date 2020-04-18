cmake_minimum_required(VERSION 2.8.3)
project(roscontrol_sot_talos)

find_package(PkgConfig REQUIRED)

set(bullet_FOUND 0)
pkg_check_modules(bullet REQUIRED bullet)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  control_msgs
  sensor_msgs
  realtime_tools
  controller_interface
)

include_directories(include ${bullet_INCLUDE_DIRS} ${catkin_INCLUDE_DIRS})

link_directories(${bullet_LIBRARY_DIRS})

catkin_package()

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

## Mark executables and/or libraries for installation
foreach(dir config launch)
  install(DIRECTORY ${dir}
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  )
endforeach()

catkin_install_python(PROGRAMS
  scripts/republish
  scripts/start_talos_gazebo.py
  scripts/start_talos_gazebo_16_04.py

  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
