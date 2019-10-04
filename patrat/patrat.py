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
import subprocess

#searches .patrat directory up to 5 levels down
def searchpokemon():
    p = '.patrat/'
    for i in range(5):
        if os.path.exists(cwd+"/"+p):
            break
        p = '../'+p
    #we found patrat path!
    if os.path.exists(p):
        return p+"/"
    return ".patrat/"

def getpatmitlist():
    r = open(PATRAT_RATTLOG, "r")
    stri = r.read()
    patlist = stri.split(" ")
    patlist = patlist[1:]
    return patlist

def gettimelist():
    r = open(PATRAT_RMLOG, "r")
    stri = r.read()
    patlist = stri.split(" ")
    patlist = patlist[1:]
    return patlist

def getmsglist():
    r = open(PATRAT_TLOG, "r")
    stri = r.read()
    patlist = stri.split(" ")
    patlist = patlist[1:]
    return patlist

#init
cwd = os.getcwd()
arg = sys.argv[1:]
PATRAT_MAJOR = 0
PATRAT_MINOR = 3
PATRAT_PATRAT = searchpokemon()
PATRAT_PATMIT = "patmit/"
PATRAT_TEMPF = PATRAT_PATRAT+"PATT/"
PATRAT_PATLOG = PATRAT_PATRAT+"PATLOG"
PATRAT_PATCHLEVEL = 1
allowed_patmit_id = list("abcdefghijklmnopqrstuvwxyz1234567890")
power = ['PATRAT', 'RATICATE', 'RATTATA', 'PIKACHU', 'CHARIZARD', 'PORYGON', 'EMPOLEON', 'PALKIA']
PATRAT_RATTLOG = PATRAT_PATRAT+"RATLOG"
PATRAT_PATLIST = getpatmitlist()
PATRAT_TIMELIST = gettimelist()
PATRAT_MSGLIST = getmsglist()
PATRAT_DEBUGLOG = PATRAT_PATRAT+'DLOG'
PATRAT_APILEVEL = 1-1
PATRAT_RMLOG = PATRAT_PATRAT+"RMLOG"
PATRAT_TLOG = PATRAT_PATRAT+"TLOG"
PATRAT_API = PATRAT_PATRAT+"APILEVEL"

#main part

#logs ALL the actions. you cant even think what is it doing
def patlogger(rattymessage):
    if os.path.exists(PATRAT_DEBUGLOG):
        pass
    else:
        return
    logg = open(PATRAT_DEBUGLOG, "a+")
    logg.write(str(time.time())+str(" ")+str(rattymessage)+str("\n"))
    logg.close()
    
#tells user to init
def reportnorepo():
    patlogger("reportnorepo init, reporting error")
    reporterr("No PATRAT repository there or 5 levels down")

#throws patrat folder to the disk
def throwpatratstack(nameof):
    patlogger("throwpatratstack init, throwing patrat stack(full) on disk, path = "+nameof)
    syscall("tar -czf "+nameof+" "+PATRAT_PATRAT+" >/dev/null")

#throws logs to the disk
def throwpartstack(nameof):
    patlogger("throwpatratstack init, throwing patrat stack(log) on disk, path = "+nameof)
    syscall("tar -czf"+nameof+" "+PATRAT_DEBUGLOG+" "+PATRAT_PATLOG+" "+PATRAT_RATTLOG)

#prints debuglog to the screen 
def debuglog():
    patlogger("debuglog: printing DLOG to the screen")
    f = open(PATRAT_DEBUGLOG, "r")
    for line in f:
        print(line)

#def returnpokemon():
    #deprecated, use reporterr

#enhanced error handler
def reporterr(mess):
    patlogger("reporterr: ------------------------------------Traceback at {}--------------------".format(str(time.time())))
    patlogger("Reported error = "+mess)
    print("PATRAT: ERROR HANDLER")
    print("Error "+mess)
    l = len(power) -1
    print('Dont worry if something went wrong! Patrat is supported and maintaned by nergzd723. Open issue at GitHub for assistance.\nAnd always remember, PATRAT has a force of', power[random.randint(0, l)])
    print("That`s all I know")
    throwpartstack(cwd+"/"+"callstack")
    print(".patrat directory image dumped on disk")
    pr = input("Proceed with error? Things may crash! ")
    if pr == "y":
        patlogger("-------------------------------------------User chose to proceed-----------------")
        pass
    else:
        patlogger("-------------------------------------------Calming down, EOEXEC----------------------")
        exit(1)
        
#cleans temporary directory
def cleantempf():
    patlogger("cleantempf: init")
    shutil.rmtree(PATRAT_TEMPF)
    patlogger("removed tree")
    os.mkdir(PATRAT_TEMPF)
    patlogger("recovered tree")

#generates a tarball for patmit
def tarball(patmit):
    patlogger("tarball: generating tarball for patmit "+patmit)
    syscall("tar -czf "+PATRAT_PATRAT+PATRAT_PATMIT+patmit+"/"+patmit+".pat"+" * >/dev/null")

#unzips tar patmit in the tempdir
def detar(patmit):
    patlogger("detar: detarring for patmit "+patmit)
    syscall("cp {} {} > /dev/null".format(cwd+"/"+PATRAT_PATRAT+PATRAT_PATMIT+patmit+"/"+patmit+".pat", cwd+"/"+"RAT"))
    syscall("tar -xzf {} > /dev/null".format(cwd+"/"+"RAT"))

#generates name for patmit, 5 symbols
def genpatmitname():
    patlogger("genpatmitname: init")
    patmit_name = ""
    for i in range(5):
        patmit_name = patmit_name + allowed_patmit_id[random.randint(0, 35)]
    patlogger("genpatmitname: New patmit name "+patmit_name)
    return patmit_name

#registers patmit in PATLOG, PATLOG is nessesary sometimes
def register(patmit, patmitmsg):
    patlogger("register: init")
    f = open(PATRAT_PATLOG, "a")
    f.write("\n")
    f.write(str(time.time())+" "+patmit+"\n"+patmitmsg) #implement md5 hash here
    patlogger("register: writing for "+patmit+" with "+patmitmsg+" message")
    f.close()
    patlogger("register: writing to ratlog")
    ratlog = open(PATRAT_RATTLOG, "a")
    ratlog.write(patmit+" ")
    ratlog.close()
    patlogger("register: writing to rmlog")
    rlog = open(PATRAT_RMLOG, "a")
    rlog.write(patmitmsg+" ")
    rlog.close()
    patlogger("register: saving timestamp")
    tm = open(PATRAT_TLOG, "a")
    tm.write(str(time.time())+" ")
    tm.close()
    patlogger("register: done writing to logs")

#generates PATRAT patmit with specific name
def patmit(patmitmsg):
    hotb()
    patmit = genpatmitname()   
    os.mkdir(PATRAT_PATRAT+PATRAT_PATMIT+patmit)
    tarball(patmit)
    patlogger("patmit: new patmit "+patmit+" with patmitmsg "+patmitmsg)
    register(patmit, patmitmsg)
    print("New patmit - "+patmit)

#hotbackup
def hotb():
    patlogger("hotb: generating hotb")
    patmit = "HOTB" 
    syscall("mkdir -p {} > /dev/null".format(PATRAT_PATRAT+PATRAT_PATMIT+patmit))
    tarball(patmit)

#opens PATLOG and reads entities from it
def log():
    patlogger("log: writing PATLOG to screen")
    f = open(PATRAT_PATLOG, "r")
    for line in f:
        print(line)

#inits PATRAT repository
def patrat_init():
    patlogger("patrat_init: got init command")
    if os.path.exists(cwd+'/'+PATRAT_PATRAT):
        patlogger("patrat_init: repo at "+cwd+'/'+PATRAT_PATRAT+" is already init")
        reporterr("Patrat repository is already init!")
    os.mkdir(PATRAT_PATRAT)
    os.mkdir(PATRAT_PATRAT+"patmit")
    os.mkdir(PATRAT_TEMPF)
    f = open(PATRAT_PATLOG, "w+")
    f.close()
    rat = open(PATRAT_RATTLOG, "w+")
    rat.close()
    l = open(PATRAT_DEBUGLOG, "w+")
    l.close()
    t = open(PATRAT_TLOG, "w+")
    t.close()
    m = open(PATRAT_RMLOG, "w+")
    m.close()
    api = open(PATRAT_API, "w+")
    api.write(PATRAT_APILEVEL)
    api.close()
    patmit("Initial patmit")
    print("Empty PATRAT repository init at "+cwd)
    patlogger("patrat_init: done initing the repository")

#merges patmit into working tree. Overwrites old patmit, but keep entities that werent in patmit
def flow(patmitname):
    patlogger("flow: flowing patmit "+patmitname)
    hotb()
    patlogger("flow: generating hotb")
    detar(patmitname)
    print("patrat: merged patmit "+patmitname+" into current working tree")
    patlogger("flow: flow of patmit "+patmitname+" complete")

#restore from latest hotbackup
def em():
    patlogger("em: got EM command, recovering tree")
    pat("HOTB")
    
#going to state of specific commit    
def pat(patmitname):
    patlogger("pat: recovering to state "+patmitname+" patmit")
    #if patmitname not in PATRAT_PATLIST:
       # patlogger("pat: no such patmit "+patmitname) do not work, dunno why
        #reporterr("No such patmit "+patmitname)
    if patmitname == "HOTB":
        syscall("find . ! -name . -prune ! -name '.*' ! -name '.patrat' -exec rm -rf {} +")
        detar(patmitname)
        print("patrat: recovered HOTB")
        patlogger("pat: recovered hotb")
    else:
        patlogger("pat: ready-to-fly")
        hotb()
        syscall("find . ! -name . -prune ! -name '.*' ! -name '.patrat' -exec rm -rf {} +")
        detar(patmitname)
        print("patrat: you are on "+patmitname+" patmit now")
        patlogger("pat: done recovering to "+patmitname)

#detars to PATT tempf
def tempdetar(patmit):
    patlogger("tempdetar: detarring to "+PATRAT_TEMPF+" patmit "+patmit)
    syscall("cp {} {} > /dev/null".format(cwd+"/"+PATRAT_PATRAT+PATRAT_PATMIT+patmit+".pat", cwd+"/"+PATRAT_TEMPF+"RAT"))
    syscall("cd {} && tar -xzf RAT > /dev/null".format(PATRAT_TEMPF))

#does recover file from patmit *now need projfilepath, dunno how to fix
def renew(filen, patmit, projfilepath):
    patlogger("renew: got request, recovering "+filen+" with path "+projfilepath+" to state of patmit "+patmit)
    tempdetar(patmit)
    syscall("cp {} {} > /dev/null".format(PATRAT_TEMPF+filen, projfilepath))
    patlogger("renew: done, cleaning tempf")
    cleantempf()

#interactive patmit creation. will replace patmit or will be along with it
def senorita(patmit):
    reporterr('Not yet implemented')

#os.system call and log
def syscall(call):
    patlogger(call)
    out = subprocess.check_output(call, shell=False) #shell=False due to security issue
    patlogger(out)

#recognizes CLI commands
def lex():
    with open(PATRAT_API, "r") as API:
        API.read()
        if API != PATRAT_APILEVEL:
            reporterr("Old api or too new API. Do patrat apiupgrade")
    avcomm = ['patmit', 'init', 'pat', 'log', 'flow', 'em', 'backup', 'dlog', 'apiupgrade']
    if not arg:
        print("patrat: no command")
        exit(0)
    if arg[0] in avcomm:
        if 'log' in arg:
            log()
        if 'dlog' in arg:
            debuglog()    
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
                reporterr("No pat arguments")
                exit(1)
            pat(patmitname)
        elif 'init' == arg[0]:
            patrat_init()
        elif 'flow' == arg[0]:
            patmitname = ""
            try:
                patmitname = arg[1]
            except:
                reporterr("No flow arguments")
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
                reporterr("No renew arguments")
            if os.path.exists(cwd+'/'+filename):
                renew(filename, patmitname, cwd+'/'+filename)
            else:
                reporterr("Bad renew path")
    else:
        print("patrat: no such action, "+arg[0])

#nothing should be there
if __name__ == "__main__":
    lex()
    
