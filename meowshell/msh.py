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

def lexer(comm, args):
    availmblecomms = ['cd']
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
        return
    for l in range(lenght):
        if l == 0:
            continue
        arg = comms[l]
    comd = comms[0]
    lexer(comd, arg)
if __name__ == "__main__":
    while True:
        mainstream()
