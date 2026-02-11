#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pybullet as p
import pybullet_data
class node1(Node):
    def __init__(self):
        super().__init__("subscribing")
        self.sub=self.create_subscription(Twist,"/pub",self.callback,10)
        self.scale1=100
        p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.plane=p.loadURDF("plane.urdf")
        self.robot=p.loadURDF("/home/badassatron/ros2_ws/src/joy_car/urdf/newrobot.urdf",basePosition=[0,0,0.15],useFixedBase=False)
        p.setGravity(0,0,-9.81)
        self.create_timer(1/240,self.load)
        self.dis=0.5
        self.v_left=0
        self.v_right=0
        self.msg_received = False
        self.scale2=200
        


    def callback(self,msg:Twist):
        velocity=msg.linear.x
        angular=msg.angular.z
        self.msg_received = True
        self.v_left=velocity*self.scale1-(angular*self.scale2*self.dis/2)
        self.v_right=velocity*self.scale1+(angular*self.scale2*self.dis/2)
        self.get_logger().info("left"+str(self.v_left))
        self.get_logger().info("right"+str(self.v_right))
    def load(self):
        if not self.msg_received:
           return  # 
        p.setJointMotorControl2(
            self.robot,2,p.VELOCITY_CONTROL,targetVelocity=self.v_left,force=150
        )
        p.setJointMotorControl2(
            self.robot,3,p.VELOCITY_CONTROL,targetVelocity=self.v_right,force=150
        )
        p.stepSimulation()

def main():
    rclpy.init()
    node=node1()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__=="__main__":
    main()