# Python target module for MEOW.
# Copyright nergzd723
# Get PID of process by it`s name
# GNU GPL v3
import shutil
import sys
import psutil
try:
    ps = sys.argv[1]
except:
    print("pit: usage= pit name_of_process")
    exit(0)
for proc in psutil.process_iter():
        if proc.name() == ps:
            print(proc.name(), '    ', proc.pid)
