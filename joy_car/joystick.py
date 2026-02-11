import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
class node(Node):
    def __init__(self):
        super().__init__("koshish")
        self.sub=self.create_subscription(Joy,"/joy",self.callback,10)
        self.get_logger().info("getting the data")
        self.pub=self.create_publisher(Twist,"/pub",10)
    def callback(self,msg:Joy):
        twist=Twist()
        twist.linear.x=msg.axes[1]
        twist.angular.z=msg.axes[0]
        self.pub.publish(twist)
        
    
        


def main():
   rclpy.init()
   node1=node()
   rclpy.spin(node1)
   rclpy.shutdown() 

if __name__=="__main__":
    main()