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
PATRAT_GIT = patrat.PATRAT_PATRAT+"patrat-git/"
PATRAT_GITFILE = patrat.PATRAT_PATRAT+"PATRAT-GIT"

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
    patrat.syscall("cp {} {} > /dev/null".format(cwd+"/"+patrat.PATRAT_PATRAT+patrat.PATRAT_PATMIT+patmit+"/"+patmit+".pat", cwd+"/"+PATRAT_GIT+"TEMPD"))
    patrat.syscall("cd {} && tar -xzf TEMPD > /dev/null && rm TEMPD".format(PATRAT_GIT))
    patrat.patlogger("patrat-git refresh: detarred to "+PATRAT_GIT+" patmit "+patmit)
    patrat.patlogger("patrat-git refresh: ---------------------------------------")

#moves HB to the PATRAT_GIT and ready a repository
def patratgitinit():
    if not os.path.exists(patrat.PATRAT_PATRAT):
        patrat.reporterr("Tried to patrat-git init without patrat repository")
    if not os.path.exists(PATRAT_GITFILE):
        patrat.reporterr("Repository init without patrat-git support")
    patratgitrefresh()
    print("patrat-git ready")

#opens MEOWSHELL seance at PATRAT_GIT folder
def patratgitshell():
    patrat.patlogger("patratgitshell: start stream")
    while True:
        n = input(termcolor.colored("git $ ", "red"))
        patrat.syscall(n)

def lex():
    avcomm = ['enable', 'init', 'refresh', 'shell']