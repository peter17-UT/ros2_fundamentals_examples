/*
Description:
    This ROS2 node subscribes to "Hello World" messages
------
Publishing Topic:
    None

Subscription Topic:
    The channel containing the "Hello World!" messages
    /cpp_example_topic - std_msgs::msg::String

------
Author: P.E. Poldervaart
Date: 19-08-2026
*/

// Includes
#include "rclcpp/rclcpp.hpp" // ROS2 C++ client library
#include "std_msgs/msg/string.hpp" // Standard ROS2 message type for strings

using std::placeholders::_1; // Placeholder for callback function

// Node
class MinimalCppSubscriber : public rclcpp::Node {
    public:
        MinimalCppSubscriber() : Node("minimal_cpp_subscriber") {
            // Create subscriber on the topic with a queue size of 10 messages
            subscriber_ = create_subscription<std_msgs::msg::String>(
                "/cpp_example_topic",10,std::bind(&MinimalCppSubscriber::topicCallback, this, _1));
            
    }

    void topicCallback(const std_msgs::msg::String & msg) const {
        RCLCPP_INFO_STREAM(get_logger(),"I heard: " <<msg.data.c_str());
    };

    private:
        rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscriber_; // The subscriber object
};


// Main function to start the ROS2 node upon launch
int main(int argc, char * argv[]){
    // Initialize ROS2 communication
    rclcpp::init(argc, argv);

    // Create an instance of the MinimalCppSubscriber node
    auto minimal_cpp_subscriber = std::make_shared<MinimalCppSubscriber>();

    // 'Spin' (start) the node
    rclcpp::spin(minimal_cpp_subscriber);

    // Shutdown ROS2 communication (at termination)
    rclcpp::shutdown();

    // End program
    return 0;
};