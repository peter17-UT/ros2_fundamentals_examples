#! /usr/bin/env python3


"""
Description:
    This ROS2 node subscribes to "Hello World" messages
------
Publishing Topic:
    None

Subscription Topic:
    The channel containing the "Hello World!" messages
    /py_example_topic - std_msgs/msg/String

------
Author: P.E. Poldervaart
Date: 19-08-2026
"""

# IMPORTS
import rclpy # Import the ROS2 client library for Python
from rclpy.node import Node # Import the Node class used for creating nodes

from std_msgs.msg import String # Import the ROS2 String message type

# NODE
class MinimalPySubscriber(Node):
    """Create a minimal subscriber node."""

    def __init__(self):
        """Create a custom node class for subscribing to messages
        """

        # Initialize node with a name 'minimal_py_subscriber'
        super().__init__('minimal_py_subscriber')

        # Create subscriber on the topic with a que size of 10 messages
        #   with the listerner_callback function called when a message is received
        self.subsciber_1 = self.create_subscription(String, '/py_example_topic',self.listener_callback,10)


    def listener_callback(self,msg):
        """Callback function executed each time a message (msg) is received)
        """
        # Log the message, printing the data field of the String message
        self.get_logger().info(f'I heard: "{msg.data}"')

# Main function
def main(args=None):
    """Main function to start the ROS2 node upon launch

    Args:
        args (List, optional): Command-line arguments. Default to none.
    """

    # Initialize ROS2 communication
    rclpy.init(args=args)

    # Create an instance of the MinimalPySubscriber node
    minimal_py_subscriber = MinimalPySubscriber()

    # 'Spin' (start) the node
    rclpy.spin(minimal_py_subscriber)

    # Destroy the node explicitly when done (optional, but good practice)
    minimal_py_subscriber.destroy_node()

    # Shutdown ROS2 communication
    rclpy.shutdown()

if __name__ == '__main__':
    # Execute the main function if the script is run directly (from cd, an not imported into other script)
    main()
