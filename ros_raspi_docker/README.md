# raspberry pi で Docker 環境の構築

```
nmap -sn 192.168.1.0/24
```

https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker <user name>
```

```
docker pull ros:kinetic
docker run -it --rm ros:kinetic
roscore
```

```
docker exec -it <container name> bash
rostopic list

エラーが出る

source /opt/ros/$ROS_DISTRO/setup.bash
rostopic list
....
....
....

```

http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup
apt-get update
apt-get install ros-kinetic-rosserial-arduino
apt-get install ros-kinetic-rosserial

rosrun rosserial_arduino make_libraries.py .
ros_libがカレントディレクトリに作成される


docker cp <container name>:/<directory where ros_lib exists>/ros_lib ./ros_lib

ros_libをArduinoのsketchbook/libralary/へ移動

Ardunoでros_libのサンプルをコンパイルできるか確認する
