# Python target module for MEOW.
# Copyright Nergzd723
# GNU LGPL v3
import os
import sys
try:
    art = sys.argv[1]
    ark = sys.argv[2]
except:
    print("aexec: invalid args!")
cwd = os.getcwd()
execpath = cwd+art
for i in range(ark):
    os.system(execpath)

print("Done! Executed", execpath, ark,"times")

