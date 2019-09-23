# MEOW targeting module
# Python 3.7
# Version control system
# GNU GPLv3
# Copyright nergzd723, 2019

#imports
import sys
import os
import random
import time
import shutil

#init
cwd = os.getcwd()
arg = sys.argv[1:]
PATRAT_MAJOR = 0
PATRAT_MINOR = 1
PATRAT_PATRAT = ".patrat/"
PATRAT_PATMIT = "patmit/"
PATRAT_TEMPF = PATRAT_PATRAT+"PATT/"
PATRAT_PATLOG = PATRAT_PATRAT+"PATLOG"
PATRAT_PATCHLEVEL = 1
allowed_patmit_id = list("abcdefghijklmnopqrstuvwxyz1234567890")

#main part

#cleans temporary directory
def cleantempf():
    shutil.rmtree(PATRAT_TEMPF)

#generates a tarball for patmit
def tarball(patmit):
    os.system("tar -czf "+PATRAT_PATRAT+PATRAT_PATMIT+patmit+"/"+patmit+".pat"+" * >/dev/null")

#unzips tar patmit in the tempdir
def detar(patmit):
    os.system("tar -czf "+PATRAT_PATRAT+PATRAT_PATMIT+patmit+"/"+patmit+".pat"+" -C "+PATRAT_TEMPF+" >/dev/null")

#generates name for patmit, 5 symbols
def genpatmitname():
    patmit_name = ""
    for i in range(5):
        patmit_name = patmit_name + allowed_patmit_id[random.randint(0, 35)]
    return patmit_name

#registers patmit in PATLOG, PATLOG is nessesary sometimes
def register(patmit, patmitmsg):
    f = open(PATRAT_PATLOG, "a")
    f.write(str(time.time())+" "+patmit+" "+patmit+"\n"+patmitmsg)#implement md5 hash here
    f.close()
    
#generates PATRAT patmit with specific name
def patmit(patmitmsg):
    patmit = genpatmitname()   
    os.mkdir(PATRAT_PATRAT+PATRAT_PATMIT+patmit)
    tarball(patmit)
    register(patmit, patmitmsg)
    print("New patmit - "+patmit)

#opens PATLOG and reads entities from it
def log():
    f = open(PATRAT_PATLOG, "r")
    for line in f:
        print(line)

#inits PATRAT repository
def patrat_init():
    if os.path.exists(cwd+'/'+PATRAT_PATRAT):
        print("Patrat repository is already init!")
        exit(1)
    os.mkdir(PATRAT_PATRAT)
    os.mkdir(PATRAT_PATRAT+"patmit")
    f = open(PATRAT_PATLOG, "w+")
    f.close()
    patmit("Initial patmit")
    print("Empty PATRAT repository init at "+cwd)

#going to state of specific commit    
def pat(patmitname):
    detar(patmitname)
    os.system('rm -rf !(".patrat") > /dev/null')
    shutil.copytree(cwd+'/'+PATRAT_TEMPF, cwd)
    print("patrat: you are on "+patmit+" patmit now")

#recognizes CLI commands
def lex():
    avcomm = ['patmit', 'init', 'pat', 'log']

    if arg[0] in avcomm:
        if 'log' in arg:
            log()
        elif 'patmit' == arg[0]:
            patmitmsg = ""
            try:
                patmitmsg = arg[1]
            except:
                print("W: No patmit message")
            patmit(patmitmsg)
        elif 'pat' == arg[0]:
            patmitname = ""
            try:
                patmitname = arg[1]
            except:
                print("patrat see no arguments with pat. Do patrat pat _PATMITNAME_")
                exit(1)
            pat(patmitname)
        elif 'init' == arg[0]:
            patrat_init()
    else:
        print("patrat: yet another VCS. Do patrat init to init patrat repository")
#nothing should be there
if __name__ == "__main__":
    lex()
