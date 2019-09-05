import sys
artg = sys.argv[1]
try:
  while True:
    print(artg)
except Keyboard_Interrupt:
  print("Got interrupted")
