#!/bin/bash
set -e

# Clone ArduPilot
if [ ! -d "$HOME/ardupilot" ]; then
  git clone --recurse-submodules https://github.com/ArduPilot/ardupilot.git ~/ardupilot
fi

# Install dependencies
cd ~/ardupilot
Tools/environment_install/install-prereqs-ubuntu.sh -y
. ~/.profile

# Build SITL (plane as example)
./waf configure --board sitl
./waf plane
