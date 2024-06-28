#!/bin/sh
# Jacobus Burger (2024)
# Start up a docker container from the docker file

xhost +local: # this is needed to make graphics work
# note: --rm is to remove containers as ephemeral for the moment
docker run -it --rm \
  --network=host \
  --ipc=host \
  --privileged \
  -e DISPLAY=$DISPLAY \
  -e GPIOZERO_PIN_FACORY=rpigpio \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  -v /sys/class/gpio:/sys/class/gpio \
  -v /tmp:/tmp \
  -v /dev:/dev \
  -v /home/airobot/AiRobot:/home/ros/AiRobot \
  ros2
