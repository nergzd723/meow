import sys
import os
import platform
from mshh import cd, ls, lexer
import mshh
from importlib import reload
from termcolor import colored

def mainstream():
    reload(mshh)
    v = mshh.Vars()
    comm = input(colored(v.pcname, 'green')+' $ '+colored(v.cwd, 'red')+" ")
    comms = comm.split(' ')
    lenght = len(comms)
    arg = ""
    if lenght == 0:
        return
    for l in range(lenght):
        if lenght == 1:
            arg = ""
        if l == 0:
            continue
        arg = arg+comms[l]
    comd = comms[0]
    lexer(comd, arg)
if __name__ == "__main__":
    while True:
        mainstream()
