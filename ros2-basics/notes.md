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

# ROS 2 Basics Notes

## What I learned
- ROS 2 programs are called **nodes**.
- A **talker** node can publish messages on a topic (like "Hello ROS2").
- A **listener** node subscribes to that topic and prints what it receives.
- Both together show how data flows in ROS 2.

## Basic workflow
1. Create a ROS 2 workspace (`colcon_ws/`).
2. Inside it, put your packages in `src/`.
3. Each package has:
   - `package.xml` → metadata
   - `setup.py` + `setup.cfg` → tells ROS it’s Python code
   - `talker_listener/` folder with Python files
4. Build with:
cd colcon_ws
colcon build
source install/setup.bash
5. Run nodes with:
ros2 run talker_listener talker
ros2 run talker_listener listener

## Commands to remember
- `ros2 pkg list` → see all packages
- `ros2 node list` → see all running nodes
- `ros2 topic list` → see topics
- `ros2 topic echo /chatter` → see messages from talker
