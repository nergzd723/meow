import sys
import os
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
  while(os.path.getsize(fpath) < size):
    f.write(random.randint(0, 1000000))
    counter += 1
else:
  while(os.path.getsize(fpath) < size):
    f.write("0")
    counter += 1
print(counter, "records, writing with", filer)
