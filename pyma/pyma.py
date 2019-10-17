# PYMA - python3 MAN 
# PYMA stores pages in ~/.pyma/
# Like that:
# .pyma/patrat/1
# To register pyma for project - pyma addproj *PROJECTNAME*
# Then, pyma pageadd *PROJECTNAME* page.txt *NAMEOFPAGE*
# Show page - pyma *PROJECTNAME* /PAGENAME/
# Pyma do not support stylization... for now
# Copyright Mark Hargreaves, 2019
# GNU GPLv3

#imports
import sys
import os
import subprocess
import getpass
#/imports

#defines
PYMA_PYMA = "/home/{}/.pyma/".format(getpass.getuser())
PYMA_EXISTS = os.path.exists("/home/{}/.pyma/".format(getpass.getuser()))
PYMA_ARG = sys.argv[1:]
#/defines

#func

#exec something in a shell
def pymaexec(comm):
    subprocess.check_output(comm, shell=True)

#makes directory
def mkdirect(dir):
    pymaexec("mkdir {}".format(dir))

#makes project dir
def addproj(proj):
    mkdirect(PYMA_PYMA+proj+"/")

#adds page to proj
def addpage(proj, page, pagenumber):
    pymaexec("mv {} {}".format(page, PYMA_PYMA+proj+"/"+pagenumber))

#init pyma
def pymainit():
    print("Initializing pyma in ~/.pyma/")
    mkdirect(PYMA_PYMA)
    addproj("pyma")
    addpage("pyma", "../Documentation/pyma.txt", 1)
    print("Pyma is ready-to-fly")

def comm():
    if not PYMA_EXISTS:
        print("Pyma does not exist!")
        exit()
    if "init" in PYMA_ARG:
        pymainit()
    if "addproj" in PYMA_ARG:
        proj = PYMA_ARG[1]
        if os.path.exists(PYMA_PYMA+proj):
            print("Pyma already have this project!")
            exit()
        addproj(proj)
        o = open(PYMA_PYMA+proj+"/main")
        o.write("Automatically created page by PYMA")
        o.close()
    if "pageadd" in PYMA_ARG:
        proj = arg[1]
        page = arg[2]
        nameof = arg[3]
        pymaexec("cp {} {}".format(page, PYMA_PYMA+proj+"/"+nameof))
    else:
        proj = ""
        page = "main"
        try:
            proj = arg[0]
            try:
                page = arg[1]
            except:
                pass
        except:
            print("PYMA: no command")
            exit()
        pymaexec("cat {}".format(PYMA_PYMA+proj+"/"+page))
        
