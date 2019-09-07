# Python target module for MEOW.
# Copyright Nergzd723
# GNU LGPL v3
import os
import sys
ext = False
ar = sys.argv[1:]
path = ""
if not ar:
  path = os.getcwd()
else:
  try:
    path = ar[0]
  except:
    print('lt: no such file or directory')
    exit()
try: 
  art = os.listdir(path)
except:
  pw = os.getcwd() + '/' + path
  apt = os.path.isdir(pw)
  if apt:
    path = pw
  else:
    print('lt: no such file or directory')
try:
  print('  '.join(str(x) for x in art))
except:
  pass
