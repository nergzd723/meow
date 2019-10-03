import os
import platform
import subprocess
lastcomm = ""
lastarg = ""
availmblecomms = ['cd', 'rabbid', '^[[A']
class Vars:
    cwd = os.getcwd()
    pcname = platform.node()
    usrbincomm = os.listdir(cwd)
    localcomm = os.listdir(cwd)
    fullpath = localcomm+usrbincomm
def arrowp(void):
    if lastcomm[-1:] == ')':
        exec(lastcomm+"({})".format('"'+lastarg+'"'))
        return
    else:
        subprocess.call(lastcomm+" "+lastargs, shell=False)
def cd(comm):
    try:
        os.chdir(comm)
    except:
        try:
            os.chdir(Vars.cwd+comm)
        except:
            print("No such file or directory", comm)
def ls(void):
    m = Vars
    lt = os.listdir(m.cwd)
    for entry in lt:
        print(entry)
    return
def rabbid(void):
    print("Yay! You find an easter egg!\nmsh brought to you by Mark Hargreaves, 19 years old blue haired MGU student from Moscow. Enjoy!")
    return
def lexer(comm, args):
    if comm not in availmblecomms:
        try:
            subprocess.call(comm+" "+args, shell=False)
        except:
            print("No such file or directory or command name")
    
    else:
        i = availmblecomms.index(comm)
        if comm == '^[[A':
            availmblecomms[i] = 'arrowp'
        exec(availmblecomms[i]+"({})".format('"'+args+'"'))
        lastcomm = availmblecomms[i]
        return
    lastcomm = comm
    lastarg = args
    return
