import os 
import sys
art = sys.argv[1:]
if '>' in art:
  if os.path.exists(at):
    try:
      o = open(art[2], "w+")
      o.write(art[0])
    except:
      print("exo: no such file or directory!")
else:
  print(art[0])
      
    
