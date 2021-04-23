FROM tiryoh/ros-desktop-vnc:kinetic

SHELL ["/bin/bash", "-c"]

# RUN apt update -y && \
RUN mkdir -p ~/catkin_ws/src && \
    source /opt/ros/kinetic/setup.bash && \
    cd ~/catkin_ws && catkin_make && \
    cd ~/catkin_ws/src && \
    git clone https://github.com/project-srs/ros_lecture.git && \
    cd ~/catkin_ws/src/ros_lecture && git submodule update --init --recursive && \
    cd ~/catkin_ws && catkin_make 


RUN echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc && \
    echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc && \
    echo "alias cb='catkin_make'" >> ~/.bashrc && \
    echo "alias cb_test='catkin_make run_tests'"  >> ~/.bashrc && \
    echo "alias rosenv='env | grep ROS'" >> ~/.bashrc

