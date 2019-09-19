# DREW meow target module
# Does chemical equations
# Unsure if it works
# Copyright nergzd723, 2019, The MEOW Project
# GNU GPLv3
import sys

knownE = ['H', 'F', 'Li', 'Na', 'K', 'Ag', 'Cl', 'Rb', 'Cs', 'O', 'Be', \
         'Mg', 'Ca', 'Ba', 'Zn', 'SiO3', 'S', 'SO3', 'SO4', 'CO3', 'Ra', \
          'Cd', 'Sr', 'B', 'Al', 'Ga', 'PO4', 'In', 'NO3', 'NO2', 'OH']

class Val:
    no3val = no2val = hval = fval = lival = po3v = naval = ohval = kval = agval = clval = rbval = csval = 1 # chems with 1
    oval = beval = mgval = caval = baval = znval = sio3val = sval = so3val = so4val = co3v = raval = cdval = srval = 2 #chems with 2
    bval = alval = gaval = po4val = inval = 3 #chems with 3

#gets elem in class

def displayV(elem):
    e = elem+'val'
    return getattr(Val, e)

#the first one input formula
if '-h' in sys.argv:
    print('*hint*please split elements with dots like Li.2.O.+.H.F\n Acids must be done like this H2.SO4.+.2Na.OH')
    exit(0)
formula = input("Incert equation here ")
flist = formula.split('.')
print(flist)
finallist = []
for item in flist:
    r = 1
    i = flist.index(item)
    print(i)
    try:
        if str(flist[i+1]).isdigit():
            r = flist[i+1]
            flist.remove(flist[i+1])
    except:
        pass
    if item in knownE:
        i = item.lower()
        finallist.append(displayV(i) + (int(r) - 1))
    print(r)
print(finallist)
