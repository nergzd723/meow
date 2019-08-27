import os
import sys
art = sys.argv[1:]
a = int(input())
ap = os.getcwd()
try:
  os.mkdir('ndir')
except:
  pass
dirp = ap+'/'+'ndir'+'/'

for i in range(a):  
  f = open(dirp+str(i),"w+")
  f.close()
  print(i)
