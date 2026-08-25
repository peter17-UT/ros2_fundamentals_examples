#! usr/bin/env python3

"""
Test suite for the ROS2 minimal publisher node (python).

This script contains unit tests for verifying the functionality of a minimal ROS2 publisher:
- Node creation
- Message counter increment
- Message content formatting
------
Subscription Topics:
    None

Publishing Topics
    /py_example_topic - std_msgs/msg/String : Example messages with increment counter
---
Author: percival17
Date: 19-08-2025
"""

# IMPORTS
import pytest
import rclpy

from std_msgs.msg import String
from ros2_fundamentals_examples.minimal_py_publisher import MinimalPyPublisher

def test_publisher_creation():
    """Test if the publisher is created correctly
    
    Verifies if:
    1. node name is set correctly;
    2. publisher object exists;
    3. topic name is correct.

    :raises: AssertionError if any test fails
    """

    # Initialize ROS2 communication
    rclpy.init()

    try:
        # Create an instance of publisher node
        node = MinimalPyPublisher()

        # Test 1: verify node name
        assert node.get_name() == "minimal_py_publisher"

        # Test2: verify publisher object existence
        assert hasattr(node, 'publisher_1')

        # Test 3: verify topic name
        assert node.publisher_1.topic_name == "/py_example_topic"

    finally:
        # Clean up ROS2 communication
        rclpy.shutdown()
        
def test_message_counter():
    """Test if the message counter increments correctly
    
    Verifies that counter (node.i) increase by 1 after each timer callback execution.

    :raises: AssertionError if counter doesn't increment properly
    """

    rclpy.init()

    try:
        node = MinimalPyPublisher()
        initial_count = node.i

        # run timer_callback function once
        node.timer_callback()

        # Check if counter (node.i) is incremented by 1
        assert node.i == initial_count + 1
    finally:
        rclpy.shutdown()


def test_message_content():
    """Test if the message content if formatted correctly
    
    Verifies that the message string is properly formatted using an f-string with the current counter value.

    :raises: AssertionError if method format doesn't match the expected output.
    """

    rclpy.init()

    try:
        node = MinimalPyPublisher()

        # Set counter to a known value for testing
        node.i = 5
        msg = String()

        # Using f-string instead of % formatting
        msg.data = f'Hello World! [{node.i}]'

        assert msg.data == 'Hello World! [5]'

    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    # Execute the main function if the script is run directly (from cd, and not imported into other script)
    pytest.main(['-v'])