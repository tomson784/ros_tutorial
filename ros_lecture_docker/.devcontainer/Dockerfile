FROM tiryoh/ros-desktop-vnc:melodic

SHELL ["/bin/bash", "-c"]

RUN sudo apt update -y && \
    mkdir -p ~/catkin_ws/src && \
    source /opt/ros/melodic/setup.bash && \
    cd ~/catkin_ws && catkin build && \
    sudo apt install ros-melodic-ros-control ros-melodic-ros-controllers && \
    sudo apt install ros-melodic-joint-state-publisher ros-melodic-joint-state-controller && \
    sudo apt install ros-melodic-joint-state-publisher-gui

RUN echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc && \
    echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc && \
    echo "alias cb='catkin build'" >> ~/.bashrc && \
    echo "alias cb_test='catkin run_tests'"  >> ~/.bashrc && \
    echo "alias rosenv='env | grep ROS'" >> ~/.bashrc

