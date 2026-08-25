/**
 * @file test_publisher.cpp
 * @brief Unit tests for the ROS2 minimal publisher node
 * 
 * This file contains test cases to verify the functionality of our minimal publisher/
 * The main things tested are:
 * 1. Ensuring correct creation of the node
 *      - Correct node name
 *      - Correct topic name
 * 2. Ensuring correct publishing of the "Hello World!" message
 * 
 * Testing Framework:
 *      Google Tests (gtest) for unit testing
 * 
 * Tests:
 *      TestNodeCreation: verifies node and publisher setup
 *      TestMessageConent: verifies published message format
 * 
 * @author percival17
 * @date 25-08-2026
 */

#include <gtest/gtest.h>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class MinimalCppPublisher;

// prevents main from minimal_cpp_publisher.cpp to be included, 
// to ensure we use the main function from this file
#define TESTING_EXCLUDE_MAIN
#include "../../src/minimal_cpp_publisher.cpp"

class TestMinimalCppPublisher : public ::testing::Test{
    protected:
        void SetUp() override{
            rclcpp::init(0,nullptr);
            node = std::make_shared<MinimalCppPublisher>();
            
        }
        void TearDown() override{
            node.reset();
            rclcpp::shutdown();
        }

        std::shared_ptr<MinimalCppPublisher> node;
};

TEST_F(TestMinimalCppPublisher, TestNodeCreation){
    // Check the node name
    EXPECT_EQ(std::string(node->get_name()),std::string("minimal_cpp_publisher"));
    
    // Check that there's only 1 topic
    auto pub_endpoints = node->get_publishers_info_by_topic("/cpp_example_topic");
    EXPECT_EQ(pub_endpoints.size(), 1u); // Only 1 publisher
};

TEST_F(TestMinimalCppPublisher, TestMessageContent){
    std::shared_ptr<std_msgs::msg::String> received_msg;

    auto subscription = node->create_subscription<std_msgs::msg::String>(
        "/cpp_example_topic",10,
        [&received_msg](const std_msgs::msg::String::SharedPtr msg) {
            received_msg = std::make_shared<std_msgs::msg::String>(*msg);
        });

    // Callback function to make publisher send a message
    node->timerCallback();

    rclcpp::spin_some(node);

    // Check if message starts with "Hello World!"
    EXPECT_EQ(received_msg->data.substr(0,12), "Hello World!");
};

int main(int argc, char** argv){
    testing::InitGoogleTest(&argc,argv);
    return RUN_ALL_TESTS();
};