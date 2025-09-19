hiiiiiiii

I swear this is (probably) the last setup we will do before we start doing real work!!

Steps:
    **setup**
    Install Docker(which has humble and MAVROS)
    ## Onboarding: ROS 2 (Humble) + MAVROS in Docker

    Welcome! This document walks you through a quick local setup using Docker so you can run ROS 2 (Humble) and try out the Turtlesim demo.

    ### Prerequisites

    - An X11-compatible display (this guide uses X11 forwarding so GUI apps like Turtlesim can display)

    ### Install Docker (Ubuntu / Debian)

    Below are step-by-step commands to install the official Docker Engine on Ubuntu/Debian. Run these on the host.

    1) Remove old or conflicting packages (optional but recommended):

    ```bash
    for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do
      sudo apt-get remove -y $pkg
    done
    ```

    ## Onboarding: ROS 2 (Humble) + MAVROS in Docker

    This guide helps you set up a local Docker-based environment for ROS 2 (Humble) with MAVROS and try the Turtlesim demo.

    ### Prerequisites

    - An X11-compatible display (this guide uses X11 forwarding so GUI apps like Turtlesim can display)

    ### Install Docker (Ubuntu / Debian)

    Below are step-by-step commands to install the official Docker Engine on Ubuntu/Debian. Run these on the host.

    1) Remove old or conflicting packages (optional but recommended):

    ```bash
    for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do
      sudo apt-get remove -y $pkg
    done
    ```

    2) Install prerequisites and add Docker's GPG key:

    ```bash
    sudo apt-get update
    sudo apt-get install -y ca-certificates curl gnupg lsb-release
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
    ```

    3) Add Docker's repository and update apt index:

    ```bash
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    ```

    4) Install Docker Engine and related packages:

    ```bash
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

    5) Verify Docker is running:

    ```bash
    sudo systemctl status docker --no-pager
    ```

    Notes:
    - If a command fails on a specific distribution (for example, older Ubuntu versions), consult the official Docker install docs: https://docs.docker.com/engine/install/ubuntu/
    - If you prefer not to use sudo for Docker, add your user to the `docker` group:

    ```bash
    sudo usermod -aG docker $USER
    # then logout/login or run: newgrp docker
    ```

    ### Quick steps

    1. Build the Docker image

    ```bash
    docker build -t ros2-mavros .
    ```
    Note: if it says you don't have permission run newgrp docker or run docker with sudo preceding it
    2. Allow local root to access the X server (run on host)

    ```bash
    xhost +local:root
    ```

    3. Run the container (uses your host DISPLAY so GUI windows appear)

    ```bash
    docker run -it \
        --env="DISPLAY=$DISPLAY" \
        --env="QT_X11_NO_MITSHM=1" \
        --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
        -v $(pwd):/root/workspace \
        --name ros2-mavros \
        ros2-mavros
    ```

    4. Inside the container

    ```bash
    cd /root/workspace/
    chmod +x setup.sh
    ./setup.sh
    # Start the turtlesim node
    ros2 run turtlesim turtlesim_node
    ```

    5. In another terminal (by running: docker exec -it ros2-mavros bash), run the teleop node
    ```bash
    ros2 run turtlesim turtle_teleop_key
    ```
    Note, you may need to run newgrp docker or run docker with sudo preceding it
    If both windows appear, you're all set — explore ROS 2 and the turtlesim tutorial next.

    From now on if you want to start the docker container you need to first
    ```bash
    docker start -ai ros2-mavros
    ```
    and then for any subsequent terminals run:
    ```bash
    docker exec -it ros2-mavros bash
    ```

    ### Helpful links

    - ROS 2 Turtlesim tutorial: https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Introducing-Turtlesim/Introducing-Turtlesim.html

    ### Troubleshooting

    - If GUI windows don't appear: make sure `xhost +local:root` was run on the host and that `DISPLAY` is exported.
    - If Docker commands require sudo, either run them with `sudo` or add your user to the `docker` group.
    - If the container cannot access the X socket, check that `/tmp/.X11-unix` is mounted correctly.

    Enjoy — once this is working, explore MAVROS examples or other ROS 2 tutorials and tell me what you find!