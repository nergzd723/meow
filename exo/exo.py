# Python target module for MEOW.
# Copyright Nergzd723
# GNU LGPL v3
import os 
import sys
art = sys.argv[1:]
if '>' in art:
  if os.path.exists(art[2]):
    try:
      o = open(art[2], "w+")
      o.write(art[0])
    except:
      print("exo: no such file or directory!")
else:
  print(art[0])
      
    
