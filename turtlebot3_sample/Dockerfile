FROM tiryoh/ros-desktop-vnc:melodic

SHELL ["/bin/bash", "-c"]

RUN mkdir -p ~/catkin_ws/src && \
    source /opt/ros/melodic/setup.bash && \
    cd ~/catkin_ws && catkin_make && \
    cd ~/catkin_ws/src && \
    git clone https://github.com/ROBOTIS-GIT/turtlebot3.git && \
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git && \
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git && \
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_gazebo_plugin.git && \
    git clone https://github.com/tomson784/turtlebot3_machine_learning.git && \
    cd ~/catkin_ws && catkin_make 

RUN echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc && \
    echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc && \
    echo "alias cm='cd ~/catkin_ws && catkin_make'" >> ~/.bashrc && \
    echo "alias cm_test='cd ~/catkin_ws && catkin_make run_tests'"  >> ~/.bashrc && \
    echo "alias rosenv='env | grep ROS'" >> ~/.bashrc
    # sudo apt-get install tmux -y && \
    # git clone https://github.com/tomson784/dotfiles.git
