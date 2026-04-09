from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy
from std_msgs.msg import String

class LoggerNode(Node):
    def __init__(self, node_name: str ):
        super().__init__(node_name)

        self.enable = False

        self._subscription = self.create_subscription(
            String, '/perception/fused', self.callback, 10
        )

        self._config_sub = self.create_subscription(
            String, '/system/config', self.config_callback,
            QoSProfile( depth=1, #only the most recent message is buffered
                       durability=DurabilityPolicy.TRANSIENT_LOCAL) #nodes starting after the config publisher still receive the config message.
        ) 


    def callback(self, msg) -> None:
        if not self._enable:
            return
        
        # Get current time
        current = self.get_clock().now().to_msg()

        self.get_logger().info(f"[{current.sec}] {msg.data}")