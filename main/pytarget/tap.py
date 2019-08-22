#Tap for MEOW utilities
#Copyright Nergzd723
#LGPL v3
import sys
import os
ar = sys.argv[1:]
file = ar[0]
f = open(file)
try:
  f.close()
except:
  pass
