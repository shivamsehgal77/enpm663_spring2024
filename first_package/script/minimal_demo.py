#!/usr/bin/env python3

"""
This script initializes and runs a ROS2 node using rclpy. The node implemented in this script is from rclpy.node.Node class.

Usage:
    This script is intended to be run from the command line. It does not take any command-line arguments.
    To run the script, use the following command:

    $ ros2 run first_package minimal_demo.py
"""

# Import the ROS2 Python client library
import rclpy
# Import the Node class from the rclpy.node module
from rclpy.node import Node 


def main(args=None):
    """
    Main function to initialize a ROS2 node and spin it.

    This function initializes the ROS2 client library, creates a node, logs a greeting message.

    Args:
        args (list, optional): A list of command-line arguments passed to the ROS2 node. Defaults to None.
    """
    # Initialize the ROS2 Python client library
    rclpy.init(args=args)

    # Create a new node with the name 'minimal_py'
    node = Node("minimal_py")

    # Log a greeting message using the node's logger
    # node.get_name() returns the name of the node: minimal_py
    node.get_logger().info(f"Hello from {node.get_name()}")
    
    # Shutdown the ROS2 Python client library to clean up resources
    rclpy.shutdown()


if __name__ == "__main__":
    main()
