
/*
Description:
    This ROS2 node periodically publishes "Hello World!" messages to a topic. 
------
Publishing Topic:
    The channel containing the "Hello World!" messages
    /cpp_example_topic - std_msgs::msg::String

Subscription Topic:
    None
------
Author: P.E. Poldervaart
Date: 18-08-2026
*/

// Includes
#include "rclcpp/rclcpp.hpp" // ROS2 C++ client library
#include "std_msgs/msg/string.hpp" // Standard ROS2 message type for strings

using namespace std::chrono_literals; // Handles time duration

// Node
class MinimalCppPublisher : public rclcpp::Node {
    public:
        MinimalCppPublisher() : Node("minimal_cpp_publisher"), count_(0) {
            // Create publisher on the topic with a queue size of 10 messages
            publisher_ = create_publisher<std_msgs::msg::String>(
                "/cpp_example_topic",10); 

            // Create a timer to trigger publishing (publish every 0.5 s)
            timer_ = create_wall_timer(500ms,
                std::bind(&MinimalCppPublisher::timerCallback, this));

            RCLCPP_INFO(get_logger(),"Publishing at 2Hz");
        }

    // Create timerCallback
    void timerCallback() {
        auto message = std_msgs::msg::String();
        message.data = "Hello World! " + std::to_string(count_++);

        publisher_->publish(message);
    };

    private:
        // Define member variables
        size_t count_; //Keeps track of the number of messages published
        rclcpp::TimerBase::SharedPtr timer_; // Timer
        rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_; // The publisher object
};

// Main function to start the ROS2 node upon launch
int main(int argc, char * argv[]) {
    // Initialize ROS2 communication
    rclcpp::init(argc, argv);

    // Create an instance of the MinimalCppPublisher node
    auto minimal_cpp_publisher = std::make_shared<MinimalCppPublisher>();

    //  'Spin' (start) the node
    rclcpp::spin(minimal_cpp_publisher);

    // Shutdown ROS2 communication (at termination)
    rclcpp::shutdown();

    // End program
    return 0;

};