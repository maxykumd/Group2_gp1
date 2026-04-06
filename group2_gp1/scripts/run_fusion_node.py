import rclpy
from group2_gp1.fusion_node import FusionNode


def main(args=None):
    rclpy.init(args=args)
    node = FusionNode("fusion_node")
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("hihi fusion")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()