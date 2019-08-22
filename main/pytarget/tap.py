#Tap for MEOW utilities
#Copyright Nergzd723
#LGPL v3
import sys
import os
ar = sys.argv[1:]
file = ar[0]
try:  
  f = open(file, "r")
except:
  f = open(file, "w+")
try:
  f.close()
except:
  pass
