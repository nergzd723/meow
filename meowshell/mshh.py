import os
import platform
class Vars:
    cwd = os.getcwd()
    pcname = platform.node()
    usrbincomm = os.listdir(cwd)
    localcomm = os.listdir(cwd)
    fullpath = localcomm+usrbincomm
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
    availmblecomms = ['cd', 'rabbid']
    if comm not in availmblecomms:
        try:
            os.system(comm+" "+args)
        except:
            print("No such file or directory or command name")
    else:
        i = availmblecomms.index(comm)
        exec(availmblecomms[i]+"({})".format('"'+args+'"'))
        return
    return
