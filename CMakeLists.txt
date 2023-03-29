cmake_minimum_required(VERSION 2.8.3)
project(turtlesim_cleaner)

##The comments were excluded for cleaning purpose
##If you want aditional information check: http://wiki.ros.org/catkin/CMakeLists.txt

#These are the imports used in your code
find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  message_generation)


## Our script uses a setup.py for catkin to use
## For aditional information check: http://wiki.ros.org/rospy_tutorials/Tutorials/Makefile
## catkin_python_setup()

## Generate messages in the 'msg' folder
#add_message_files(
#   FILES
#  moves.msg 
#)

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
#This line guarantees that any .msg file in the msg directory will generate code for use in all supported languages.
#generate_messages(
#  DEPENDENCIES
#  geometry_msgs  
#)

#Since we are using custom messages and packages, we have to declare
#For aditional information: http://wiki.ros.org/ROS/Tutorials/DefiningCustomMessages
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES turtlesim_cleaner
# CATKIN_DEPENDS rospy geometry_msgs message_runtime
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)

## Declare a C++ library
# add_library(turtlesim_cleaner
#   src/${PROJECT_NAME}/turtlesim_cleaner.cpp
# )

## Add cmake target dependencies of the library
## as an example, code may need to be generated before libraries
## either from message generation or dynamic reconfigure
# add_dependencies(turtlesim_cleaner ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Declare a C++ executable
# add_executable(turtlesim_cleaner_node src/turtlesim_cleaner_node.cpp)

## Add cmake target dependencies of the executable
## same as for the library above
# add_dependencies(turtlesim_cleaner_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
# target_link_libraries(turtlesim_cleaner_node
#   ${catkin_LIBRARIES}
# )


include_directories(
  ${catkin_INCLUDE_DIRS}
)


#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
# install(PROGRAMS
#   scripts/my_python_script
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark executables and/or libraries for installation
# install(TARGETS turtlesim_cleaner turtlesim_cleaner_node
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

	catkin_install_python(PROGRAMS src/move.py src/rotate.py src/gotogoal.py src/cleaner.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


