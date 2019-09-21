# Python target module for MEOW.
# Copyright nergzd723
# Kills process by pid or by name
# GNU LGPL v3
import os
import sys
import signal
import psutil
ar = sys.argv[1:]
if not ar:
    print("kid MEOW utility\nKills process by pid(usage - kid (term or kill) pid)\n\
        Or by name(usage - kid -n nameof)")
    exit(1)
if '-n' in ar:
    for proc in psutil.process_iter():
        if proc.name() == ar[1]:
            proc.kill()
            print("Killed", proc.name(), 'with PID', proc.pid())
else:
    if 'term' in ar:
        ar = ar[1:]
        try:
            os.kill(ar[0], signal.SIGTERM)
            print("Killed! pid = {} signal = SIGTERM".format(ar[0]))
        except:
            print("No such process or access denied!")
    else:
        try:
            os.kill(ar[0], signal.SIGKILL)
            print("Killed! pid = {} signal = SIGKILL".format(ar[0]))
        except:
            print("No such process or access denied!")