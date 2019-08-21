import os
import sys
arg = sys.argv[1:]
if '-r' in arg:
  ar = arg[1:]
  recursive = TRUE;
else:
  ar = arg
for x in ar:
  if os.path.exists(ar[x]):
    os.remove(ar[x])
  else:
    print("No such file or directory -", ar[x]) 
