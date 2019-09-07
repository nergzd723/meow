import sys
try:
  artg = sys.argv[1]
except:
  artg = 'n'
try:
  while True:
    print(artg)
except KeyboardInterrupt:
  print("Got interrupted")
