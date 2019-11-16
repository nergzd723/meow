#charmander backup and protection util
#use char -char to test
#currently doesnt support directories
import sys
import os
import hashlib
import subprocess

CHAR_ARGS = sys.argv[1:]
CHAR_CHAR = '.char/'
CHAR_FILES = [ f for f in os.listdir('.') if os.path.isfile(os.path.join('.',f)) ]
CHAR_BLOB = CHAR_CHAR+'obj/'

#syscall
def syscall(call):
    subprocess.check_output(call, shell=True)

#encrypt to blob
def charenc(filen, passc, pathto):
    syscall("gpg --output {} --symmetric --passphrase {} --batch -c {}".format(pathto, passc, filen))

#decrypt blob
def chardec(filen, passc, pathto):
    syscall("gpg --output {} --passphrase {} --batch {}".format(pathto, passc, filen))

def charinit():
    syscall("mkdir .char/")
    syscall("mkdir .char/obj/")
    print("charmander: start")
    print("charmander: creating charmander blobs. please wait")
    for filen in CHAR_FILES:
        charenc(filen, "test", CHAR_BLOB+filen+'.bin')
    print("Done")
        
#md5 hexdigest
def hexdigest(filename):
    return hashlib.md5(open(filename,'rb').read()).hexdigest()

def lex():
    if CHAR_ARGS[0] == '-char':
        charinit()
if __name__ == "__main__":
    lex()
