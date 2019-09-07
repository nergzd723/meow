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
i = 0
for x in ar:
  if os.path.exists(ar[i]):
    try:
      os.remove(ar[i])
    except:
      if os.path.isdir(ar[i]) and recursive:
        shutil.rmtree(ar[i])
      else:
        print("bark: Is a directory,", ar[i])
                      
  else:
    print("bark: No such file or directory,", ar[i]) 
  i+=1
