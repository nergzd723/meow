#charmander crypting util for patrat
#use char -char to test

CHAR_ARGS = sys.argv[1:]
CHAR_CHAR = '.char/'
CHAR_FILES = [ f for f in os.listdir('.') if os.path.isfile(os.path.join('.',f)) ]
CHAR_BLOB = CHAR_CHAR+'obj/'
#encrypt to blob
def charenc(filen, passc, pathto):
    syscall("gpg --output {} --symmetric --passphrase {} --batch -c {}".format(pathto, passc, filen))

#decrypt blob
def chardec(filen, passc, pathto):
    syscall("gpg --output {} --passphrase {} --batch {}".format(pathto, passc, filen))

