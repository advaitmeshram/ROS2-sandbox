from setuptools import setup

package_name = 'talker_listener'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Advait Meshram',
    maintainer_email='your_email@example.com',
    description='Simple ROS 2 talker/listener package in Python',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = talker_listener.talker:main',
            'listener = talker_listener.listener:main',
        ],
    },
)
