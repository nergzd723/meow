# Python target module for MEOW.
# Copyright nergzd723
# Does provide system info and python info with -d flag
# GNU LGPL v3
import platform
import sys
class Block:
    sysd = platform.system()
    name  = platform.node()
    kmver = platform.release()
    kver = platform.version()
    ma = platform.machine()
    proc = platform.processor()
    cc = platform.python_compiler()
    cdc = platform.python_implementation()
    ver = platform.python_version()
if __name__ == "__main__":
    b = Block()
    print(b.sysd, b.name, b.kmver, "running on", b.ma)
    if '-d' in sys.argv:
        print(b.cc)
        print(b.cdc)
        print(b.ver)
        print(b.kver)
        print("processor:", b.proc)
        print("DEBUGGING INFO. nergzd723")
    
