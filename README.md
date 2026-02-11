# Joystick-Controlled Differential Drive Car (ROS2 + PyBullet)

A simple ROS2 project demonstrating a **joystick-controlled differential drive robot** using a custom URDF in PyBullet. 
The project uses two ROS2 nodes: one for subscribing to joystick commands and controlling the robot, and one for publishing commands (optional).

---

## Features

- **Differential drive robot** with two wheels.
- **Joystick control** using `geometry_msgs/Twist`.
- **PyBullet simulation** for real-time physics and visualization.
- Two ROS2 nodes:
  - **Subscriber node**: Receives velocity commands and controls the robot.
  - **Publisher node**: Optional node for testing (publishes `/pub` Twist messages).
- **Simple URDF** for the robot structure.

---

## Project Structure

