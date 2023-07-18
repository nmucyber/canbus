# CANBUS Cheat Sheet

# ICSim & can-utils setup

These steps can  be run on Kali, Ubuntu, and other Linux platforms.

```sh
cd ~
sudo apt update
sudo apt install libsdl2-dev libsdl2-image-dev can-utils
git clone https://github.com/zombieCraig/ICSim.git
git clone https://github.com/linux-can/can-utils
cd can-utils
make
sudo make install
cp lib.o ~/ICSim
cd ~/ICSim
make clean
make
```

# Start the ICSimulator and controller

ICSim and the can-utils must be installed before these commands will work.

```sh
cd ~/ICSim
sudo sh setup_vcan.sh # Create the vcan0 network device
./icsim vcan0 & # Launches the virtual car
./controls vcan0 & # Launches the controller
```

# Viewing and Capturing CAN Network Traffic

```sh
cansniffer -c vcan0          # Show live network traffic, -c shows colors
candump -l vcan0             # Capture all CAN network traffic to a log file
tail candump-2023-07-17.log  # View the end of the log file
```

# Generating Traffic

```sh
cangen vcan0                         # Generate random CAN messages on the vcan0 network
canplayer -I candump-2023-07-17.log  # Replay network traffic 
cansend vcan0 188#01                 # Sends the blinker signal to the ICSim vehicle
```
