#!/bin/sh
# Jacobus Burger (2024)
# Start up a docker container from the docker file

xhost +local: # this is needed to make graphics work
# note: --rm is to remove containers as ephemeral for the moment
docker run -it --rm \
  --device /dev/video0:/dev/video0 \
  --network=host \
  --ipc=host \
  --privileged \
  -e DISPLAY=$DISPLAY \
  -e GPIOZERO_PIN_FACORY=rpigpio \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v /home/airobot/AiRobot:/home/ros/AiRobot \
  -v /sys/class/gpio:/sys/class/gpio \
  -v /dev:/dev \
  -v /run/udev:/run/udev \
  -v /run/dbus:/run/dbus \
  ros2
