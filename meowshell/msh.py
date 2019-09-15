import sys
import os
import platform
import mshh
from importlib import reload

def cd(comm):
    try:
        os.chdir(comm)
    except:
        try:
            os.chdir(Vars.cwd+comm)
        except:
            print("No such file or directory", comm)
def ls(void):
    m = mshh.Vars
    lt = os.listdir(m.cwd)
    for entry in lt:
        print(entry)
    return
def lexer(comm, args):
    availmblecomms = ['cd', 'ls']
    if comm not in availmblecomms:
        print("No such file or directory or command name")
    else:
        i = availmblecomms.index(comm)
        exec(availmblecomms[i]+"({})".format('"'+args+'"'))
        return
    return

def mainstream():
    reload(mshh)
    v = mshh.Vars()
    comm = input(v.pcname+' $ '+v.cwd+" ")
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
        arg = comms[l]+arg
    comd = comms[0]
    lexer(comd, arg)
if __name__ == "__main__":
    while True:
        mainstream()
