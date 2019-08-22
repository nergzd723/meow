#Tap for MEOW utilities
#Copyright Nergzd723
#LGPL v3
import time
epoch = int(time.time())
import sys
import os
ar = sys.argv[1:]
try:
  file = ar[0]
except:
  print('tap: no such file or directory!')
try:  
  try:
    f = open(file, "r")
  except:
    print('tap: is a directory!')
  a = os.getcwd()
  ark = a+'/'+file
  os.utime(ark, (epoch, epoch))
except:
  f = open(file, "w+")
try:
  f.close()
except:
  pass
