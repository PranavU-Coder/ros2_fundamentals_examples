# All Programs I wrote while relearning ros2 from basics

## system requirements :

- Ubuntu 24.04 LTS
- ROS2 Jazzy { compatible for the OS mentioned above }

in case you don't have the specific system requirements mentioned , create a docker container with the following command

- docker pull osrf/ros:jazzy-desktop-full

## Recent Additions :

Integrating with pytest to validate code before it goes into production instead of standard CMake lint packages

to test -> 

- colcon test --packages-select ros2_fundamentals_examples --event-handlers console_direct+
