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
  path = ar[0]
try: 
  art = os.listdir(path)
except:
  print('ln: no such file or directory')
print('    '.join(str(x) for x in art))
