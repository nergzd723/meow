#Tap for MEOW utilities
#Copyright Nergzd723
#LGPL v3
import datetime
epoch = datetime.datetime.utcfromtimestamp(0)
import sys
import os
ar = sys.argv[1:]
file = ar[0]
try:  
  f = open(file, "r")
  os.utime(os.path.abspath(file), (epoch, epoch+1))
except:
  print("\n")
  f = open(file, "w+")
try:
  f.close()
except:
  pass
