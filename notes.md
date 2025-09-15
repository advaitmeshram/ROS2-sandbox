# ROS 2 Basics Notes

## Key Concepts
- **Nodes**: Programs that do one thing (talker, listener).
- **Topics**: Channels that carry messages between nodes.
- **Messages**: Data sent over topics (e.g. String, Int32).
- **Services**: Request/response communication.
- **Actions**: Long-running tasks with feedback.

## Useful Commands
- `ros2 node list` → show running nodes
- `ros2 topic list` → show topics
- `ros2 topic echo /chatter` → print messages
- `ros2 run pkg_name node_name` → run a node
- `ros2 launch pkg_name launch_file.py` → launch multiple nodes

## Workspace Layout
- `colcon_ws/src/` → source code
- `colcon_ws/build/` → build files (ignored by Git)
- `colcon_ws/install/` → installed files
- `colcon_ws/log/` → logs

## My Notes
- Talker publishes `Hello ROS2: N` on topic `/chatter`.
- Listener subscribes to `/chatter` and prints received data.
