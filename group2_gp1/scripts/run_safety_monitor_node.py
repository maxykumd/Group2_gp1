# Name: Yossaphat Kulvatunyou
# UID: 112362550
# Module: run_safety_monitor_node.py

import rclpy
from group2_gp1.safety_monitor_node import SafetyMonitor


def main(args=None):
    rclpy.init(args=args)
    node = SafetyMonitor("safety_monitor_node")
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("hihi")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()