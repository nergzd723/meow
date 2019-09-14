# Python targeting module for meow
# Does byte-by-byte copy of data
# Usage: yedd -l path to file to read from -d path to file to write to -bs size of block
# Copyright Mark Hargeaves, 2019
# GNU GPLv3

import sys
import os
cwd = os.getcwd()
art = sys.argv[1:]
if "-l" not in art or "-d" not in art:
  print("yedd: arguments not found!")
  exit(1)
ind = art.index("-l") + 1
inn = art.index("-d") + 1

if os.path.exists(art[ind]) and os.path.exists(art[inn]):
  p = art[ind]
  pa = art[inn]
else:
  p = cwd + '/' + art[ind]
  pa = cwd + '/' + art[inn]
  if os.path.exists(p) and os.path.exists(pa):
    pass
  else:
    if !os.path.exists(p):
      print("yedd: path do not exist!")
      exit(1)
    else:
      f = open(pa, "w+")
      f.close()

if "-bs" in art:
  piece_size = art[art.index("-bs") + 1]
else:
  piece_size = 4096 # userdefined block size defaults to 4096

with open(p, "rb") as in_file, open(pa, "wb") as out_file:
    while True:
        piece = in_file.read(piece_size)
        if piece == "":
            break # end of file
        out_file.write(piece)
