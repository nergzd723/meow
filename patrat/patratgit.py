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
    patratgitrefresh("HOTB")
    patrat.patlogger("patratgitinit: init git repository")
    patrat.syscall("cd {} && git init".format(PATRAT_GIT))
    print("patrat-git ready")

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

#patratgit setup: setup repo origin and another
def patratgitsetup():
    print("patratgit setup utility\nYou can always change settings later")
    origin = input("Origin of your repository, it`s remote(e.g. https://github.com/patrat/patrat-repo)")
    branch = input("Branch where to push to repo")
    patrat.patlogger("patratgitsetup: got from user: "+origin+" repo and "+branch+" branch")
    patratgitexec("git checkout -b {}".format(branch))
    patratgitexec("git remote add origin {}".format(origin))
    print("Done setup!\nOrigin = "+origin+"\nbranch = "+branch)

#doing patmit of current changes, refresh a patratgit, git commit and git push
def patratgitapply():
    patratgitexec("git pull")
    patrat.patlogger("patratgitapply: creating tarball of PGIT")
    patrat.tarball("PGIT")
    patrat.patlogger("patratgitapply: refresh")
    patratgitrefresh("PGIT")
    msg = input("Enter git commit message ")
    patratgitexec("git add .")
    patrat.patlogger("patratgitapply: creating commit with message "+msg)
    patratgitexec('git commit -m "{} (patratgit)"'.format(msg))
    patratgitexec("git push origin master")
    print("Done! If something is wrong, you can always use patratgit shell or watch DLOG for errors")
    patrat.patlogger("patratgitapply: success")

def lex():
    avcomm = ['enable', 'init', 'refresh', 'shell', 'setup', 'apply']
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
        if arg[0] == 'setup':
            patratgitsetup()
        if arg[0] == 'apply':
            patratgitapply()

if __name__ == "__main__":
    lex()
