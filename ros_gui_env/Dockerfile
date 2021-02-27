FROM dorowu/ubuntu-desktop-lxde-vnc:bionic

RUN "install ros env"

RUN mkdir -p ~/catkin_ws/src && \
    source /opt/ros/melodic/setup.bash && \
    cd ~/catkin_ws && catkin build && \
    cd ~/catkin_ws/src
