from setuptools import find_packages, setup

package_name = 'group2_gp1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='maxz',
    maintainer_email='maxz@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'lidar_node = group2_gp1.scripts.run_lidar_node:main',
            'publisher_demo = group2_gp1.scripts.run_publisher_demo:main',
            'fusion_node = group2_gp1.scripts.run_fusion_node:main',
        ],
    },
)
# 'lidar_node = group2_gp1.lidar:main'