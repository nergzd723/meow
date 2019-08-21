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
  f = open(ar[1], "w+")
  f.close()
  try:
    shutil.copyfile(ar[0], ar[1])
  except:
    print('cpy: file already exists!(-f flag will probaply fix this)')
elif os.path.exists(ar[0]):
  f = open(ar[1], "w+")
  f.close()
  try:
    shutil.copyfile(ar[0], ar[1])
  except IsADirectoryError:
    if recursive:
      shutil.copytree(ar[0], ar[1])
    else:
      print("cpy: is a directory!(-r flag will probably fix this)")
elif os.path.exists(ar[1]):
  print("cpy:", ar[0], "does not exist!")

