import os 
import sys
art = sys.argv[1:]
if '>' in art:
  ar = art[0]
  at = art[2]
  if os.path.exists(at):
    try:
      o = open(at, "w+")
      o.write(ar)
    except:
      print("exo: no write permissions!")
else:
  print(art)
      
    
