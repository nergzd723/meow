# Python target module for MEOW.
# Copyright Nergzd723
# GNU LGPL v3
import os
import shutil
import sys
recursive = False
arg = sys.argv[1:]
if '-r' in arg:
  ar = arg[1:]
  recursive = True
else:
  ar = arg
for elem in ar:
  if os.path.exists(elem):
    try:
      os.remove(elem)
    except:
      if os.path.isdir(elem) and recursive:
        shutil.rmtree(elem)
      else:
        print("bark: Is a directory,", elem)
                      
  else:
    print("bark: No such file or directory,", elem) 
    
