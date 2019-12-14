# endure - make html MORE easier
import sys
from os import getcwd
from termcolor import cprint
ENDURE_CV = 1
ENDURE_ARGS = sys.argv[1:]
ENDURE_DOC = ""
backslashn = '\n'
whereto = ""
ENDURE_BODYTEMP = ""
ENDURE_BODYBACK = "#FFFFFF"
ticktock = 0
ENDURE_HEADTEMP = ""
ENDURE_OTHERTEMP = ""
def loadf(mod):
    global ticktock
    with open(mod) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    for command in content:
        ticktock+=1
        exec(command)
def cc_err(error):
    cprint("error: "+error+" at line "+str(ticktock), 'red')
    exit(1)
def write_doc():
    o = open(whereto, "w+")
    o.write(ENDURE_DOC)
    o.close()
def generate():
    global ENDURE_DOC
    ENDURE_DOC = "<!DOCTYPE HTML>\n"
    ENDURE_DOC = ENDURE_DOC+"<html>\n"
    ENDURE_DOC = ENDURE_DOC+"<!--Autogenerated html with endure, DO NOT EDIT -->"+backslashn
    ENDURE_DOC = ENDURE_DOC+"<head>\n"
    ENDURE_DOC = ENDURE_DOC+ENDURE_HEADTEMP
    ENDURE_DOC = ENDURE_DOC+"</head>\n"
    ENDURE_DOC = ENDURE_DOC+'<body bgcolor="{}">\n'.format(ENDURE_BODYBACK)
    ENDURE_DOC = ENDURE_DOC+ENDURE_BODYTEMP
    ENDURE_DOC = ENDURE_DOC+"</body>\n"
    ENDURE_DOC = ENDURE_DOC+ENDURE_OTHERTEMP
    ENDURE_DOC = ENDURE_DOC + "</html>\n"
def header(*arg):
    global ENDURE_BODYTEMP
    arlen = len(arg)
    text = arg[0]
    align = 'left'
    size = "1"
    color = "black"
    if arlen > 1:
        size = arg[1]
    if arlen > 2:
        align = arg[2]
    if arlen > 3:
        color = arg[3]
    if size > 8 or size < 1:
        cc_err("bad <h> size: "+size)
    if align == 'left' or align == 'right' or align == 'center':
        pass
    else:
        cc_err("bad align: "+align)
    ENDURE_BODYTEMP = ENDURE_BODYTEMP + '<h{} align={} style="color:{}">{}</h{}>\n'.format(size, align, color, text, size)
def background(cl):
    global ENDURE_BODYBACK
    ENDURE_BODYBACK = cl
def paragraph(*arg):
    global ENDURE_BODYTEMP
    arlen = len(arg)
    align = "left"
    text = arg[0]
    color = "black"
    print(arlen)
    if arlen > 1:
        align = arg[1]
    if arlen > 2:
        align = arg[2]
    ENDURE_BODYTEMP = ENDURE_BODYTEMP + '<p align={} style="color:{}">'.format(align, color)+text+"</p>"+backslashn
def title(hdr):
    global ENDURE_HEADTEMP
    ENDURE_HEADTEMP = ENDURE_HEADTEMP + "<title>"+hdr+"</title>\n"
def dino():
    global whereto
    if "-o" in ENDURE_ARGS:
        whereto = getcwd()+"/"+ENDURE_ARGS[ENDURE_ARGS.index("-o")+1]
        endfile = getcwd()+"/"+ENDURE_ARGS[0]
        loadf(endfile)
        generate()
        write_doc()
    else:
        whereto = getcwd()+'/'+"a.out"
        endfile = getcwd+"/"+ENDURE_ARGS[0]
        loadf(endfile)
        generate()
        write_doc()
if __name__ == "__main__":
    dino()