from subprocess import call
import sys
import time

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
        message = f"{device} {message}"
        messages.append(message)

def run_code(cmd):
    time.sleep(0.1)
    params = ["cansend", cmd.split(" ")[0], cmd.split(" ")[1]]
    call(params)

print("Looking for the needle in the haystack.")
jump =  min(48, len(messages)//2) #Do 48 at a time, or less if the length of messages is short
start = max(len(messages) - jump, 0)
end = len(messages)
while True:
    print(f"Checking list items from index {start} to {end}")
    for code in messages[start:end+1]:
        print(f"Checking {code}")
        run_code(code)
    i = input("Did something happen? y/n/x\n")
    if i == "x":
        exit()
    elif i == "y":
        # Narrow down
        messages = messages[start:end+1]
        if len(messages)==1:
            print(f"Found code: {code}")
            exit()
        jump = len(messages)//2
        end = len(messages)
        start = end - jump
    elif i == "n":
        del messages[start:end+1]
        start -= jump
        end -= jump
        if start < 0:
            start = 0
        if end < 0:
            end = 0
