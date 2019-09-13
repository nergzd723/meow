import sys
import os
import random

art = sys.argv[1:]
if not art:
  print("createimage utility. Creates empty file with specified size(in bytes) then arguments\n Arguments = -r write with random\n Part of MEOW project")
  exit(0)

cwd = os.getcwd()
fpath = cwd + '/' + art[0]
size = 512
try:
  size = int(art[1])
except:
  pass
f = open(fpath, "w+")
counter = 0
filer = 0
if '-r' in art:
  filer = "r"
  for n in range(size):
    if os.path.size(fpath) == size:
      break
    else:
      pass
    f.write(str(random.randint(0, 1000000)))
    counter += 1
else:
  for n in range(size):
    f.write(str(filer))
    counter += 1
print(counter, "records, writing with", filer)
