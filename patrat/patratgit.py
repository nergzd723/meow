# MEOW targeting module
# Python 3.7
# PATRAT module for GIT management
# GNU GPLv3
# Copyright nergzd723, 2019

#imports
import patrat #import the main module to use some functions
import os
import sys
import termcolor
import time

#init
arg = sys.argv[1:]
cwd = os.getcwd()
PATRAT_PATRAT = patrat.searchpokemon()
PATRAT_PATMIT = PATRAT_PATRAT+"patmit/"
PATRAT_GIT = ".patrat/patrat-git/"
PATRAT_GITFILE = PATRAT_PATRAT+"PATRAT-GIT"
PATRAT_LIST = patrat.getpatmitlist()
PATRAT_LPAT = PATRAT_LIST[len(PATRAT_LIST)-1]
PATRAT_MERGESTARTPOINT = PATRAT_LIST[0]
PATRAT_HEAD = PATRAT_PATRAT+"GITHEAD"
PATRAT_PATLIST = patrat.gettimelist()
PATRAT_MSGLIST = patrat.getmsglist()

#main part

#exec git code
def patratgitexec(call):
    patrat.patlogger("patratgitexec: got a call "+call)
    patrat.syscall("cd {} && {}".format(PATRAT_GIT, call))

def updhead(patmit):
    p = open(PATRAT_HEAD, "w")
    p.write(patmit+" ")
    p.close()
    patrat.patlogger("HEAD is now on patmit "+patmit)

#setup patrat-git
def patratgitsetup():
    if os.path.exists(PATRAT_GITFILE):
        patrat.reporterr("patrat-git support present")
    o = open(PATRAT_GITFILE, "w+")
    o.close()
    p = open(PATRAT_HEAD, "w+")
    p.write(PATRAT_LIST[0])
    p.close()
    print("PATRAT-GIT setup util\nThis util is used to merge patmits to already init git repositorys")
    origin = input("Enter origin git repository(e.g https://github.com/meowproj/patrat) ")
    patrat.patlogger("patratgitsetup: Cloning repo "+origin+" to patrat-git folder")
    os.mkdir(PATRAT_GIT)
    patrat.syscall("cd "+PATRAT_PATRAT+" && git clone "+origin+" patrat-git")
    print("Cloned origin to "+PATRAT_GIT)
    print("Patrat-git ready to work")

#opens MEOWSHELL seance at PATRAT_GIT folder
def patratgitshell():
    os.chdir(PATRAT_GIT)
    sep = " "
    patrat.patlogger("patratgitshell: start stream")
    while True:
        n = input(termcolor.colored("git $ ", "red"))
        n = n.split(" ")
        if 'cd' in n:
            os.chdir(cwd+"/"+n[1])
        else:
            patrat.patlogger(sep.join(n))
            os.system(sep.join(n))

def patratgitmergeall():
    for patmit in PATRAT_LIST:
        if patmit == " " or patmit == "":
            break
        i = PATRAT_LIST.index(patmit)
        patrat.syscall("cp {} {} > /dev/null".format(cwd+"/"+PATRAT_PATMIT+patmit+"/"+patmit+".pat", PATRAT_GIT+"GITRAT"))
        print("Copy patmit "+patmit)
        patrat.syscall("cd {} && tar -xzf {} > /dev/null".format(PATRAT_GIT, "GITRAT"))
        print("Detar patmit "+patmit)
        patratgitexec("git add .")
        patratgitexec("git commit -m {}".format(PATRAT_MSGLIST[i]))
        print("Commit patmit "+patmit+" with message "+PATRAT_MSGLIST[i])
        updhead(patmit)

def lex():
    avcomm = ['setup', 'mergeall', 'refresh', 'shell', 'setup', 'apply', 'merge']
    if arg[0] in avcomm:
        if arg[0] == 'setup':
            patratgitsetup()
        if arg[0] == 'shell':
            patratgitshell()
        if arg[0] == 'mergeall':
            patratgitmergeall()
if __name__ == "__main__":
    lex()
