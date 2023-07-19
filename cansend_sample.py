# Created by Dr. Jim Marquardson
# Initial commit: 7/18/2023
# Last updated: 7/19/2023
# License: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication (https://creativecommons.org/publicdomain/zero/1.0/)
# Use, modify, and distribute this code as you see fit.
#
# This is a simple python program that runs cansend  on 
# the vcan0 network. It sends a CAN message with the
# arbitration ID 244 and data 0000005A12 10 times per second.
from subprocess import call
import time
print("Press control+c to stop")
while True:
        time.sleep(0.1)
        call(["cansend", "vcan0", "244#0000005A12"])
