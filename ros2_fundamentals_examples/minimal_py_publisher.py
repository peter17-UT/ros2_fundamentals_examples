#! /usr/bin/env python3

"""
Description:
    This ROS2 node periodically publishes "Hello World!" messages to a topic. 
------
Publishing Topic:
    The channel containing the "Hello World!" messages
    /py_example_topic - std_msgs/msg/String

Subscription Topic:
    None
------
Author: P.E. Poldervaart
Date: 18-08-2026
"""

# IMPORTS
import rclpy # Import the ROS2 client library for Python
from rclpy.node import Node # Import the Node class used for creating nodes

from std_msgs.msg import String # Import the ROS2 String message type

# NODE
class MinimalPyPublisher(Node):
    """Create a minimal publisher node."""

    def __init__(self):
        """ Create a custom node class for publishing messages
        """
        # Initialize node with a name 'minimal_py_publisher'
        super().__init__('minimal_py_publisher')

        # Create a publisher on the topic with a queue size of 10 messages
        self.publisher_1 = self.create_publisher(String, '/py_example_topic', 10)

        # Create a timer to trigger publishing (publish every 0.5 s)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Optional: Initialize counter variable for message content
        self.i = 0

    def timer_callback(self):
        """Callback function executed periodically by the timer
        """
        # Create a new String message object
        msg = String()

        # Set the message data (msg.data) with a counter (defined in the __init__)
        msg.data = 'Hello World! [%d]' % self.i
        self.i += 1 #increment counter

        # Publish the created message to a topic (publisher is defined in the __init__)
        self.publisher_1.publish(msg)

        # Log a message indication that the message has been published
        self.get_logger().info('Publishing: "%s"' % msg.data)

# Main function
def main(args=None):
    """Main function to start the ROS2 node upon launch

    Args:
        args (List, optional): Command-line arguments. Default to none.
    """

    # Initialize ROS2 communication
    rclpy.init(args=args)

    # Create an instance of the MinimalPyPublisher node
    minimal_py_publisher = MinimalPyPublisher()

    # 'Spin' (start) the node
    rclpy.spin(minimal_py_publisher)

    # Destroy the node explicitly when done (optional, but good practice)
    minimal_py_publisher.destroy_node()

    # Shutdown ROS2 communication
    rclpy.shutdown()

if __name__ == '__main__':
    # Execute the main function if the script is run directly (from cd, and not imported into other script)
    main()