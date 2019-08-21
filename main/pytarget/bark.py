import os
import sys
arg = sys.argv[1:]
if '-r' in arg:
  ar = arg[1:]
  recursive = TRUE;
else:
  ar = arg
i = 0
for i in ar:
  if os.path.exists(ar[i]):
    os.remove(ar[i])
  else:
    print("No such file or directory -", ar[i]) 
  i+=1
