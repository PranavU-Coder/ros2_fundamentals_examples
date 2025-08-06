#!/usr/bin/env python3 

import rclpy
import pytest 
from std_msgs.msg import String
from ros2_fundamentals_examples.minimal_publisher import Minimal_Publisher

def test_creation():

    rclpy.init()

    try:
        node = Minimal_Publisher()

        assert node.get_name() == 'minimal_publisher'
        assert hasattr(node, 'publisher')
        assert node.publisher.topic_name == '/topic'
    
    finally:

        rclpy.shutdown()


def test_message_counter():

    rclpy.init()

    try:

        node = Minimal_Publisher()
        initial_count = node.i 
        node.timer_callback()
        assert node.i == initial_count + 1
    
    finally:

        rclpy.shutdown()

def test_message_content():

    rclpy.init()

    try:

        node = Minimal_Publisher()
        node.i = 5
        msg = String()

        msg.data = f'Hello World : {node.i}'
        assert msg.data == 'Hello World : 5'
    
    finally:

        rclpy.shutdown()

if __name__ == '__main__':
    pytest.main(['-v'])