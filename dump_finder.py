# Created by Dr. Jim Marquardson
# Initial commit: 7/18/2023
# Last updated: 7/19/2023
# License: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication (https://creativecommons.org/publicdomain/zero/1.0/)
# Use, modify, and distribute this code as you see fit.
from subprocess import call
import sys
import time

SLEEP_TIME = 0.1 # Time between commands

if len(sys.argv) < 2: #0 is script name, 1 is the dump file
	print("Please provide a file name.")
	print("Example:")
	print("python dump_finder.py sample_icsim_candump.txt")
	sys.exit()
else:
	file_path = sys.argv[1]

messages = []
with open(file_path, 'r') as file:
    for line in file:
        timestamp, device, message = line.strip().split(' ',2)
        message = (device, message)
        messages.append(message)

def run_code(message):
    time.sleep(SLEEP_TIME)
    print(f"Running: cansend {message[0]} {message[1]}")
    call(["cansend", message[0], message[1]])

print("Looking for the needle in the haystack.")
trial_size = min(48, len(messages)//2) # Number of packets to try at a time at first
while True:
    trial = messages[-trial_size:]
    for t in trial:
        run_code(t)
    answer = input("Did the event occur? y/n (other key to exit)\n")
    if answer.upper()=="Y" and len(trial)==1:
        print(f"Found: {t[1]}")
        sys.exit()
    elif answer.upper()=="Y":
        messages = trial
        trial_size = len(trial)//2
    elif answer.upper()=="N":
        del messages[-trial_size:]
    else:
        sys.exit()

