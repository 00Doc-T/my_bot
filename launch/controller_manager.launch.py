import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_path = os.path.join(get_package_share_directory('my_bot'))
    controller_manager_node = Node(
        package='controller_manager',
        executable='ros2_control_node',
        arguments=['--ros-args', '--params-file', os.path.join(pkg_path, 'config', 'my_controllers.yaml')],
        output={
            'stdout': 'screen',
            'stderr': 'screen',
        },
    )
    return LaunchDescription([controller_manager_node])
