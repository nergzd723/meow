# Python targeting module for MEOW.
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
    print('dip: no such file or directory')
try: 
  art = os.listdir(path)
except:
  print('dip: no such file or directory')
  exit()
for file in range(len(art)):
  print(art[file])
