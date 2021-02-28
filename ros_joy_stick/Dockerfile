FROM ros:melodic

# install ros tutorials packages
RUN mkdir -p ~/catkin_ws/src && \
    /bin/bash -c '. /opt/ros/kinetic/setup.bash; cd ~/catkin_ws/; catkin_make' && \
    echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc && \
    apt-get update -y && \
    # apt-get install -y bluez && \
    # apt-get install -y python-pip && \
    # pip install ds4drv && \
    apt-get install -y ros-melodic-joy && \
    apt-get install -y ros-melodic-joystick-drivers
