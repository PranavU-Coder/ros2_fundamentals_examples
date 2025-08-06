#!/bin/bash

cleanup(){
    echo "restarting ROS2 daemon to cleanup before shutting down ..."
    ros2 daemon stop
    sleep 1
    ros2 daemon start
    echo "terminating all ROS2 processes ..."
    kill 0
    exit 
}

trap 'cleanup' SIGINT

ros2 run ros2_fundamentals_examples minimal_publisher.py &

sleep 2

ros2 run ros2_fundamentals_examples minimal_subscriber.py