#charmander crypting util for patrat
#use char -char to test
import sys
import os
import subprocess

#os.system call and log
def syscall(call):
    out = subprocess.check_output(call, shell=True) #shell=False due to security issue

CHAR_ARGS = sys.argv[1:]
CHAR_CHAR = '.char/'
CHAR_FILES = [ f for f in os.listdir('.') if os.path.isfile(os.path.join('.',f)) ]
CHAR_BLOB = CHAR_CHAR+'obj/'
#encrypt to blob
def charenc(filen, passc, pathto):
    syscall("gpg --output {} --symmetric --passphrase {} --batch -c {}".format('"'+pathto+'"', passc, '"'+filen+'"'))

#decrypt blob
def chardec(filen, passc, pathto):
    syscall("gpg --batch --passphrase {} --output {} --decrypt {}".format(passc, '"'+pathto+'"',  '"'+filen+'"'))

