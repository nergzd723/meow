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
    print(os.listdir(m.cwd))
def lexer(comm, args):
    availmblecomms = ['cd', 'ls']
    if comm not in availmblecomms:
        print("No such file or directory or command name")
    else:
        i = availmblecomms.index(comm)
        print(availmblecomms[i]+"({})".format(args))
        exec(availmblecomms[i]+"({})".format('"'+args+'"'))
        return
    return

def mainstream():
    reload(mshh)
    v = mshh.Vars()
    comm = input(v.pcname+' $ '+v.cwd+" ")
    comms = comm.split(' ')
    lenght = len(comms)
    if lenght == 1:
        lexer(comms[0], "")
    for l in range(lenght):
        if l == 0:
            continue
        arg = comms[l]+arg
    comd = comms[0]
    lexer(comd, arg)
if __name__ == "__main__":
    while True:
        mainstream()
