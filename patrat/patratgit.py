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
PATRAT_HEAD = PATRAT_PATRAT+"HEADofGIT"

#main part

#enables patrat-git via empty files
def patratgitenable():
    patrat.patlogger("patrat-git enable: init")
    if os.path.exists(PATRAT_GITFILE):
        patrat.reporterr("patrat-git support is present")
    os.mkdir(PATRAT_GIT)
    os.mkdir(PATRAT_PATMIT+"PGIT/")
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
    o = open(PATRAT_HEAD, "w+")
    o.write(PATRAT_LIST[0])
    o.close()
    patratgitsetup()
    #patratgitrefresh("HOTB")
    patrat.patlogger("patratgitinit: init git repository")
    #patrat.syscall("cd {} && git init".format(PATRAT_GIT))

#exec git code
def patratgitexec(call):
    patrat.patlogger("patratgitexec: got a call "+call)
    patrat.syscall("cd {} && {}".format(PATRAT_GIT, call))

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

def patratgitcommitpatmit(patmit):
    patrat.patlogger("patratgitcommitpatmit: got a task: push "+patmit+" to git repository and commit")
    patratgitrefresh(patmit)
    patratgitexec('git add . && git commit -m "Automatically created patmit {}"'.format(patmit))
    patrat.patlogger("patratgitcommitpatmit: done for patmit "+patmit)

#patratgit setup: setup repo origin and another
def patratgitsetup():
    print("patratgit setup utility\nYou can always change settings later")
    origin = input("Origin of your repository, it`s remote(e.g. https://github.com/patrat/patrat-repo)")
    patrat.patlogger("patratgitsetup: got from user: "+origin+" repo")
    patratgitexec("git clone {}".format(origin))
    print("Done setup!\nOrigin = "+origin)

def patratgitmerge():
    H = open(PATRAT_HEAD, "r")
    HEAD = H.read()
    H.close()
    r = open(PATRAT_HEAD, "w")
    PATRAT_MERGESTARTPOINT = HEAD
    print("Starting merge to GIT")
    patrat.patlogger("patratgitmerge: Starting merge, starting point: "+PATRAT_MERGESTARTPOINT)
    for patmit in PATRAT_LIST:
        patratgitcommitpatmit(patmit)
        r.write(patmit)
        patrat.patlogger("Merged patmit "+patmit)
    print("Done merging to GIT, current HEAD = "+PATRAT_LPAT)

#doing patmit of current changes, refresh a patratgit, git commit and git push
#def patratgitapply():
  #  patratgitexec("git pull")
 #   patrat.patlogger("patratgitapply: creating tarball of PGIT")
#    patrat.tarball("PGIT")
   # patrat.patlogger("patratgitapply: refresh")
  #  patratgitrefresh("PGIT")
 #   msg = input("Enter git commit message ")
#    patratgitexec("git add .")
    #patrat.patlogger("patratgitapply: creating commit with message "+msg)
   # patratgitexec('git commit -m "{} (patratgit)"'.format(msg))
  #  patratgitexec("git push origin master")
 #   print("Done! If something is wrong, you can always use patratgit shell or watch DLOG for errors")
#    patrat.patlogger("patratgitapply: success")

def lex():
    avcomm = ['enable', 'init', 'refresh', 'shell', 'setup', 'apply', 'merge']
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
        if arg[0] == 'merge':
            patratgitmerge()
if __name__ == "__main__":
    lex()
