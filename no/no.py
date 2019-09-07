import sys
artg = sys.argv[1]
try:
  while True:
    print(artg)
except KeyboardInterrupt:
  print("Got interrupted")
