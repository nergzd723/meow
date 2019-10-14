# PATRAT module
# Deletes PATRAT repo
# patrat loadmod patrat.py

def PATRAT_USERMODULE_MAGIC():
    return 0xDEFEAD # is the module PATRAT module or not?
# note: do not import patrat! Except you have PATRAT installed as .so file

def defines(): # define your vars here
    return
def prompt(): # do everything here
    import os
    import subprocess
    print("Are you sure to delete patrat?")
    i = input("y/n ")
    if not i == 'y':
        exit()
    subprocess.check_output("rm -rf .patrat/", shell=True) # do not do this ^_^