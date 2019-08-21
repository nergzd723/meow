import os
import sys
import shutil
def getv():
  print('cpy shell utility by nergzd723. Built using Python 3.7 and Nuitka.')
  exit(0)
arg = sys.argv[1:]
recursive = False
if '-r' in arg:
  ar = arg[1:]
  recursive = True
if '-v' in arg:
  getv()
else:
  ar = arg
if os.path.exists(ar[0]) and os.path.exists(ar[1]):
  shutil.copyfile(ar[0], ar[1])
elif os.path.exists(ar[0]):
  print("cpy:", ar[1], "does not exist!")
elif os.path.exists(ar[1]):
  print("cpy:", ar[0], "does not exist!")
  
