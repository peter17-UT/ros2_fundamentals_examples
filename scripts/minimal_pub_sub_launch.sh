#! /bin/bash

# Launch publisher and subscriber nodes with cleanup handeling
cleanup() {
    echo "Restarting ROS 2 daemon to cleanup before shutting down all processes."

    ros2 daemon stop
    sleep 1
    ros2 daemon start
    echo "Terminating all ROS2-related processes..."
    kill 0
    exit
}

# When pressing Ctrl+C, script wil first run cleanup
trap 'cleanup' SIGINT

# Launch publisher node
ros2 run ros2_fundamentals_examples minimal_py_publisher.py &

# Pause for 2 seconds
sleep 2

# Lauch sibscriber node
ros2 run ros2_fundamentals_examples minimal_py_subscriber.py