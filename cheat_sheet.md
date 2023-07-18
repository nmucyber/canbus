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
sudo sh setup_vcan.sh   # Create the vcan0 network
                        # If there is no output, the command likely worked fine.
                        # A message, "RTNETLINK answers: File exists" likely means
                        # that the vcan0 network was already created.
                        # Use ifconfig to verify if vcan0 exists
ifconfig                # If the setup_vcan.sh command was successful,
                        # a vcan0 network device should appear
./icsim vcan0 &         # Launches the virtual car
                        # The & at the end lets you run more commands in the terminal after this command.
                        # You may need to press [enter] after seeing the message like, "Using CAN interface vcan0"
./controls vcan0 &      # Launches the game-like controller that sends messages on the vcan0 network
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
cangen vcan0 -I 445                  # Generate random CAN data with the arbitration ID 445 only
cansequence vcan0                    # Sends CAN messages with the payload constantly increasing (i.e., not random)
canplayer -I candump-2023-07-17.log  # Replay network traffic 
cansend vcan0 188#01                 # Sends the blinker signal to the ICSim vehicle
```


# Starting ICSim with Different Seeds

By default, ICSim uses the same arbitration IDs every time it starts. These arbitration IDs can be randomized to add challenges.

Before running these commands, close the ICSim and controls windows to stop the programs.

````sh
./icsim -s 42 vcan0 &     # Starts ICSim using the seed number 42 (the number can be any number)
./controls -s 42 vcan0 &  # Starts the controls using the same seed
````
