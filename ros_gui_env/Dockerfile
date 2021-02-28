FROM dorowu/ubuntu-desktop-lxde-vnc:bionic

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
    apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654  && \
    apt update -y  && \
    apt install ros-melodic-desktop-full -y && \
    echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc  && \
    source ~/.bashrc  && \
    apt install -y python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential  && \
    rosdep init  && \
    rosdep update

RUN mkdir -p ~/catkin_ws/src  && \
    cd ~/catkin_ws && catkin build  && \
    echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc && \
    source ~/.bashrc && \
    echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc && \
    echo "alias cb='catkin build'" >> ~/.bashrc && \
    echo "alias cb_test='catkin run_tests'"  >> ~/.bashrc && \
    echo "alias rosenv='env | grep ROS'" >> ~/.bashrc

# mkdir -p ~/catkin_ws/src && \
# source /opt/ros/melodic/setup.bash && \
# cd ~/catkin_ws && catkin build && \
# cd ~/catkin_ws/src
