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
PATRAT_PATCHLEVEL = 2
allowed_patmit_id = list("abcdefghijklmnopqrstuvwxyz1234567890")
power = ['PATRAT', 'RATICATE', 'RATTATA', 'PIKACHU', 'CHARIZARD', 'PORYGON', 'EMPOLEON', 'PALKIA']
PATRAT_RATTLOG = PATRAT_PATRAT+"RATLOG"
PATRAT_PATLIST = ""

#main part

#tells user to init
def reportnorepo():
    raise Error("No PATRAT repository there or 5 levels down")

#searches .patrat directory up to 5 levels down
def searchpokemon():
    p = './patrat'
    for i in range(5):
        if os.path.exists(p):
            break
        p = '../'+p
    #we found patrat path!
    if os.path.exists(p):
        return p
    else:
        reportnorepo()

#throws patrat folder to the disk
def throwpatratstack(nameof):
    os.system("tar -czf "+nameof+" "+PATRAT_PATRAT+" >/dev/null")

#nice text for nice people
def returnpokemon():
    l = len(power)
    print('Dont worry if something went wrong! Patrat is supported and maintaned by nergzd723. Open issue at GitHub for assistance.\nAnd always remember, PATRAT has a force of', power[random.randint(0, l)])
    
#cleans temporary directory
def cleantempf():
    shutil.rmtree(PATRAT_TEMPF)
    os.mkdir(PATRAT_TEMPF)

#generates a tarball for patmit
def tarball(patmit):
    os.system("tar -czf "+PATRAT_PATRAT+PATRAT_PATMIT+patmit+"/"+patmit+".pat"+" * >/dev/null")

#unzips tar patmit in the tempdir
def detar(patmit):
    os.system("cp {} {} > /dev/null".format(cwd+"/"+PATRAT_PATRAT+PATRAT_PATMIT+patmit+"/"+patmit+".pat", cwd+"/"+"RAT"))
    os.system("tar -xzf {} > /dev/null".format(cwd+"/"+"RAT"))

#generates name for patmit, 5 symbols
def genpatmitname():
    patmit_name = ""
    for i in range(5):
        patmit_name = patmit_name + allowed_patmit_id[random.randint(0, 35)]
    return patmit_name

#registers patmit in PATLOG, PATLOG is nessesary sometimes
def register(patmit, patmitmsg):
    f = open(PATRAT_PATLOG, "a")
    f.write("\n")
    f.write(str(time.time())+" "+patmit+"\n"+patmitmsg)#implement md5 hash here
    f.close()
    ratlog = open(PATRAT_RATTLOG, "a")
    ratlog.write(" "+patmit)
    ratlog.close()

#generates PATRAT patmit with specific name
def patmit(patmitmsg):
    hotb()
    patmit = genpatmitname()   
    os.mkdir(PATRAT_PATRAT+PATRAT_PATMIT+patmit)
    tarball(patmit)
    register(patmit, patmitmsg)
    print("New patmit - "+patmit)

def getpatmitlist():
    r = open(PATRAT_RATTLOG, "r")
    stri = r.read()
    patlist = stri.split(" ")
    patlist = patlist[1:]
    return patlist

#hotbackup
def hotb():
    patmit = "HOTB" 
    os.system("mkdir -p {} > /dev/null".format(PATRAT_PATRAT+PATRAT_PATMIT+patmit))
    tarball(patmit)

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
    os.mkdir(PATRAT_TEMPF)
    f = open(PATRAT_PATLOG, "w+")
    f.close()
    rat = open(PATRAT_RATTLOG, "w+")
    rat.close()
    patmit("Initial patmit")
    print("Empty PATRAT repository init at "+cwd)

#merges patmit into working tree. Overwrites old patmit, but keep entities that werent in patmit
def flow(patmitname):
    hotb()
    detar(patmitname)
    print("patrat: merged patmit "+patmitname+" into current working tree")
    
#restore from latest hotbackup
def em():
    pat("HOTB")
    
#going to state of specific commit    
def pat(patmitname):
    if patmitname not in PATRAT_PATLIST:
        raise Error("No such patmit "+patmitname)
    if patmitname == "HOTB":
        os.system("find . ! -name . -prune ! -name '.*' ! -name '.patrat' -exec rm -rf {} +")
        detar(patmitname)
        print("patrat: recovered HOTB")
    else:    
        hotb()
        os.system("find . ! -name . -prune ! -name '.*' ! -name '.patrat' -exec rm -rf {} +")
        detar(patmitname)
        print("patrat: you are on "+patmitname+" patmit now")

#detars to PATT tempf
def tempdetar(patmit):
    os.system("cp {} {} > /dev/null".format(cwd+"/"+PATRAT_PATRAT+PATRAT_PATMIT+patmit+".pat", cwd+"/"+PATRAT_TEMPF+"RAT"))
    os.system("cd {} && tar -xzf RAT > /dev/null".format(PATRAT_TEMPF))

#does recover file from patmit *now need projfilepath, dunno how to fix
def renew(filen, patmit, projfilepath):
    tempdetar(patmit)
    os.system("cp {} {} > /dev/null".format(PATRAT_TEMPF+filen, projfilepath))
    cleantempf()

#interactive patmit creation. will replace patmit or will be along with it
def senorita(patmit):
    raise Error('Not yet implemented')

#recognizes CLI commands
def lex():
    papath = searchpokemon()
    PATRAT_PATRAT = papath
    PATRAT_PATLIST = getpatmitlist()
    avcomm = ['patmit', 'init', 'pat', 'log', 'flow', 'em', 'backup']
    if not arg:
        print("patrat: no command")
        exit(0)
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
                raise Error("No pat arguments")
                exit(1)
            pat(patmitname)
        elif 'init' == arg[0]:
            patrat_init()
        elif 'flow' == arg[0]:
            patmitname = ""
            try:
                patmitname = arg[1]
            except:
                raise Error("No flow arguments")
                exit(1)
            flow(patmitname) 
        elif 'em' == arg[0]:
            em()
        elif 'renew' == arg[0]:
            patmitname = ""
            filename = ""
            try:
                filename = arg[1]
                try:
                    patmitname = arg[2]
                except:
                    patmitname = "HOTB"
            except:
                raise Error("No renew arguments")
                exit(1)
            if os.path.exists(cwd+'/'+filename):
                renew(filename, patmitname, cwd+'/'+filename)
            else:
                raise Error("Bad renew path")
                exit(1)                
    else:
        print("patrat: no such action, "+arg[0])

#nothing should be there
if __name__ == "__main__":
    lex()
    exit(0)
    
#enhanced error handler
class Error(Exception):
    print("PATRAT: ERROR HANDLER")
    l = len(power)
    print('Dont worry if something went wrong! Patrat is supported and maintaned by nergzd723. Open issue at GitHub for assistance.\nAnd always remember, PATRAT has a force of', power[random.randint(0, l)])
    print("That`s all I know")
    throwpatratstack(cwd+"/"+"callstack")
    print(".patrat directory image dumped on disk")
