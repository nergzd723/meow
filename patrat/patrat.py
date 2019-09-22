# MEOW targeting module
# Python 3.7
# Version control system
# GNU GPLv3
# Copyright nergzd723, 2019

#imports
import sys
import os
import random
import subprocess

#init
cwd = os.getcwd()
arg = sys.argv[1:]
PATRAT_MAJOR = 0
PATRAT_MINOR = 1
PATRAT_PATRAT = ".patrat/"
PATRAT_PATMIT = "patmit/"
PATRAT_PATCHLEVEL = 1
allowed_patmit_id = list("abcdefghijklmnopqrstuvwxyz1234567890")

#main part
def tarball(patmit):
    os.system("tar -cvzf "+PATRAT_PATRAT+PATRAT_PATMIT+patmit+"/"+patmit+".pat"+" * >/dev/null")
    print("New patrat patmit - patmit", patmit[:5])
def genpatmitname():
    patmit_name = ""
    for i in range(56):
        patmit_name = patmit_name + allowed_patmit_id[random.randint(0, 35)]
    return patmit_name
def patrat_init():
    if os.path.exists(cwd+'/'+PATRAT_PATRAT):
        print("Patrat repository is already init!")
        exit(1)
    os.mkdir(PATRAT_PATRAT)
    initpatmit = genpatmitname()
    os.mkdir(PATRAT_PATRAT+"patmit")
    os.mkdir(PATRAT_PATRAT+PATRAT_PATMIT+initpatmit)
    tarball(initpatmit)
patrat_init()
