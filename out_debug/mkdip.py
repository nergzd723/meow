import os
import sys
art = sys.argv[1:]
parentof = False
if '-p' in art:
  parentof = True
  art = art[1:]
ap = os.getcwd()
try:
  dirp = ap+'/'+art[0]
except:
  print('mkdip: missing operand')
  exit()
try:
  os.mkdir(ap)
except:
  if parentof:
    exit()
  else:
    print('mkdip: can`t create directory', art[0], ': File already exists')

    
