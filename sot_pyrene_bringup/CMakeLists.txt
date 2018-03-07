cmake_minimum_required(VERSION 2.6)

project(sot_pyrene_bringup)

find_package(catkin REQUIRED)
catkin_package()

#set(PROJECT_NAME sot_talos_bringup)
#set(PROJECT_DESCRIPTION ROS package for Stack of Tasks on Talos)
#set(PROJECT_URL "")

#setup_project()

INSTALL(
  FILES 
  DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME}/config
)

INSTALL(
  FILES
  launch/geometric-simu.launch
  DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME}/launch
)


INSTALL(
  FILES
  package.xml
  DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME}/
)

#setup_project_finalize()

