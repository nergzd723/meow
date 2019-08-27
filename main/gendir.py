import os
import sys
art = sys.argv[1:]
a = int(input())
ap = os.getcwd()
os.mkdir('ndir')
dirp = ap+'/'+'ndir'+'/'

for i in range(a):  
  f = open(dirp+i,"w+")
  f.close()
  print(i)
