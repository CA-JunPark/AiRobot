# Jacobus Burger (May 2024)
FROM ros:humble


# insall base packages
RUN apt-get update
RUN apt-get upgrade -y
#   enable universe and multiverse repositories
RUN apt-get install software-properties-common -y
RUN add-apt-repository universe multiverse -y

# install ROS2 packages
RUN apt-get update
RUN apt-get install ros-humble-desktop -y
RUN apt-get install ros-humble-rplidar-ros -y
RUN apt-get install ros-humble-cartographer -y

# install build tools
RUN apt-get update
RUN apt-get install build-essential libcap* libcamera* build-essential meson ninja-build libyaml-dev python3-yaml python3-ply python3-jinja2 libssl-dev openssl git -y
# install libcamera for picamera2



# install python packages
#   install system dependencies
RUN apt-get update
RUN apt-get install python3 python3-pip python3-venv python3-dev python3-rpi.gpio -y
#   install pip packages
RUN pip install rpi-lgpio gpiozero rplidar-roboticia ultralytics picamera2


# create a non-root user so volume files are accessible outside container
RUN groupadd --gid 1000 ros
RUN useradd -s /bin/bash --uid 1000 --gid 1000 -m ros
RUN mkdir -p /home/ros/
RUN chown 1000:1000 /home/ros/


# setup root
RUN apt-get update
RUN apt-get install sudo -y
RUN echo ros ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/ros
RUN chmod 0440 /etc/sudoers.d/ros


# setup user in working directory
WORKDIR /home/ros/
ENTRYPOINT ["/bin/bash", "/ros_entrypoint.sh"]
CMD ["bash"]
USER ros
