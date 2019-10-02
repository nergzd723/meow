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
PATRAT_PATRAT = '.patrat/'
PATRAT_PATMIT = PATRAT_PATRAT+"patmit/"
PATRAT_GIT = ".patrat/patrat-git/"
PATRAT_GITFILE = PATRAT_PATRAT+"PATRAT-GIT"

#main part

#enables patrat-git via empty files
def patratgitenable():
    patrat.patlogger("patrat-git enable: init")
    if os.path.exists(PATRAT_GITFILE):
        patrat.reporterr("patrat-git support is present")
    os.mkdir(PATRAT_GIT)
    open(PATRAT_GITFILE, "w+")
    patrat.patlogger("done enabling")
    print("patrat-git support enabled")

#moves specifical patmit to PATRAT_GIT
def patratgitrefresh(patmit):
    patrat.patlogger("patrat-git refresh: detarring patmit "+patmit+" to "+PATRAT_GIT)
    patrat.syscall("cp {} {} > /dev/null".format(cwd+"/"+".patrat/patmit/"+patmit+"/"+patmit+".pat", cwd+"/"+PATRAT_GIT+"TEMPD"))
    patrat.syscall("cd {} && tar -xzf TEMPD > /dev/null && rm TEMPD".format(PATRAT_GIT))
    patrat.patlogger("patrat-git refresh: detarred to "+PATRAT_GIT+" patmit "+patmit)
    patrat.patlogger("patrat-git refresh: ---------------------------------------")

#moves HB to the PATRAT_GIT and ready a repository
def patratgitinit():
    if not os.path.exists(patrat.PATRAT_PATRAT):
        patrat.reporterr("Tried to patrat-git init without patrat repository")
    if not os.path.exists(PATRAT_GITFILE):
        patrat.reporterr("Repository init without patrat-git support")
    patratgitrefresh("HOTB")
    patrat.patlogger("patratgitinit: init git repository")
    patrat.syscall("cd {} && git init".format(PATRAT_GIT))
    print("patrat-git ready")

#opens MEOWSHELL seance at PATRAT_GIT folder
def patratgitshell():
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

def lex():
    avcomm = ['enable', 'init', 'refresh', 'shell']
    if arg[0] in avcomm:
        if arg[0] == 'enable':
            patratgitenable()
        if arg[0] == 'init':
            patratgitinit()
        if arg[0] == 'refresh':
            patmit = arg[1]
            patratgitrefresh(patmit)
        if arg[0] == 'shell':
            patratgitshell()

if __name__ == "__main__":
    lex()
