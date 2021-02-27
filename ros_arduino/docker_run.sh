ls /dev/ttyACM*

envs=($(ls /dev/ttyACM*))

for envs in "${envs[@]}" ; do
  sudo chmod 777 ${envs}
done


# docker run -it --net=host --privileged --device=/dev/ttyACM0:/dev/ttyACM0:rwm -v $PWD/src:/root/catkin_ws/src --rm ros:melodic /bin/bash

docker run \
-it \
--net=host \
--privileged \
--device=/dev/ttyACM0:/dev/ttyACM0:rwm \
--device=/dev/input/:/dev/input/:rwm \
--rm \
ros:melodic \
/bin/bash
