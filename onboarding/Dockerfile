# Base image with ROS 2 Humble preinstalled
FROM osrf/ros:humble-desktop

# Avoid timezone/config prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install ROS 2 + MAVROS + dev tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    ros-humble-mavros \
    ros-humble-mavros-extras \
    geographiclib-tools \
    git \
    wget \
    curl \
    nano \
    sudo \
    bash-completion \
    default-jre \
    tzdata \
 && rm -rf /var/lib/apt/lists/*

# Install MAVROS GeographicLib datasets
RUN /usr/share/mavros/install_geographiclib_datasets.sh || true

# Setup ROS 2 environment
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc
