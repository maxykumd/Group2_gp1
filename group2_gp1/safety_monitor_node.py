# Name: Yossaphat Kulvatunyou
# UID: 112362550
# Module: safety_monitor_node.py

from std_msgs.msg import Int64, String
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup

class SafetyMonitor(Node):
    def __init__(self, node_name: str):
        super().__init__(node_name)



        # Publisher for alert
        self._publishers = self.create_publisher(
            String, '/perception/alerts', 10)

        # intentional mismatch subscriber 
        self._test_sub = self.create_subscription(
            String, '/sensors/camera', self.test_callback,
            QoSProfile( depth=10,
                        reliability=ReliabilityPolicy.RELIABLE)
        )

        self._config_sub = self.create_subscription(
            String, '/system/config', self.config_callback,
            QoSProfile( depth=1, #only the most recent message is buffered
                       durability=DurabilityPolicy.TRANSIENT_LOCAL) #nodes starting after the config publisher still receive the config message.
        ) 

        
        self._group = MutuallyExclusiveCallbackGroup()
        # Subscriber
        self._subscriptions = self.create_subscription(
            String, '/perception/fused', self.callback, 10, callback_group=self._group)

        # Threshold : Lidar dist < 2.0m (obstacle to close)
        self._threshold = 2.0


    def callback(self, msg) -> None:
        
        # data test ( camera: frame_0001, lidar: 15.3 m)
        msg = ["ID-01", 99.0]
        data = msg.data
        infos = data.split(',')
        lidar_info = infos[1]

        # Get lidar dist from string
        distance = float(lidar_info.split(':')[1].split(' ')[0])
        if distance < self._threshold:
            # Log warning
            self.get_logger().warn(f"Obstacle at {distance} m (threshold: {self._threshold} m)")

            # Publish alert
            alert_msg = String()
            alert_msg.data = "Obstacle is too close"
            self._publishers.publish(alert_msg)
        
        else: # normal situation
            self.get_logger().info(data)


    def test_callback(self, msg):
        self.get_logger().info("This should NEVER print cause of mismatch fail")

    def config_callback(self, msg):
        pass