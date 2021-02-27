FROM ros:melodic

SHELL ["/bin/bash", "-c"]

# install ros tutorials packages
RUN echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc && \
    apt update -y && \
    apt install -y ros-melodic-rosserial-arduino && \
    apt install -y ros-melodic-rosserial
