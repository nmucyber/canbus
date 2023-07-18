# This is a simple python progrm that runs cansend  on 
# the vcan0 network. It sends a CAN message with the
# arbitration ID 244 and data 0000005A12 10 times per second.
from subprocess import call
import time
print("Press control+c to stop")
while True:
        time.sleep(0.1)
        call(["cansend", "vcan0", "244#0000005A12"])
