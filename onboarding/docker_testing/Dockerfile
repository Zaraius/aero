# -------------------------------
# Base image
# -------------------------------
FROM osrf/ros:humble-desktop

# -------------------------------
# Non-interactive & timezone
# -------------------------------
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# -------------------------------
# Fix GPG issues
# -------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gnupg \
    lsb-release \
    && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
        -o /usr/share/keyrings/ros-archive-keyring.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
        http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" \
        > /etc/apt/sources.list.d/ros2.list

# -------------------------------
# Install dependencies
# -------------------------------
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

# -------------------------------
# MAVProxy
# -------------------------------
RUN pip3 install MAVProxy

# -------------------------------
# GeographicLib datasets for MAVROS
# -------------------------------
RUN /opt/ros/humble/lib/mavros/install_geographiclib_datasets.sh

# -------------------------------
# Clone ArduPilot
# -------------------------------
WORKDIR /root
RUN git clone https://github.com/ArduPilot/ardupilot.git
WORKDIR /root/ardupilot

# Initialize submodules and build for SITL fixed-wing
RUN git submodule update --init --recursive \
    && ./waf configure --board sitl \
    && ./waf plane

# -------------------------------
# Source ROS automatically
# -------------------------------
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

# -------------------------------
# Default workdir & shell
# -------------------------------
WORKDIR /root
CMD ["/bin/bash"]
