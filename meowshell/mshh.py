import os
import platform
class Vars:
    cwd = os.getcwd()
    pcname = platform.node()
    usrbincomm = os.listdir(cwd)
    localcomm = os.listdir(cwd)
    fullpath = localcomm+usrbincomm

