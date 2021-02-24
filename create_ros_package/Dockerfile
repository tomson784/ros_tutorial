FROM ros:melodic

SHELL ["/bin/bash", "-c"]

# RUN useradd -m user
# USER user

RUN apt update -y && apt upgrade -y && \
    mkdir -p /catkin_ws/src && \
    source /opt/ros/melodic/setup.bash && \
    cd /catkin_ws && catkin_make

RUN echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc && \
    echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc && \
    echo "alias cm='cd /catkin_ws/ && catkin_make'" >> ~/.bashrc && \
    echo "alias cm_test='cd /catkin_ws/ && catkin_make run_tests'"  >> ~/.bashrc && \
    echo "alias rosenv='env | grep ROS'" >> ~/.bashrc

WORKDIR /catkin_ws/src
