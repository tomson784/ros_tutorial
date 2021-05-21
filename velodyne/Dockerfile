FROM ros:melodic

SHELL ["/bin/bash", "-c"]

RUN apt-get update -y && \
    mkdir -p ~/catkin_ws/src && \
    source /opt/ros/melodic/setup.bash && \
    cd ~/catkin_ws && catkin_make && \
    apt-get install ros-melodic-velodyne -y && \ 
    cd ~/catkin_ws/src/ && \
    git clone https://github.com/ros-drivers/velodyne.git && \
    rosdep install --from-paths src --ignore-src --rosdistro melodic -y 
