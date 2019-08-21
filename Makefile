maindir=main/
moduledir=modules/
outdir=out/
outname=meow
currentdir = $(shell pwd)/
currentmeowdir = $(currentdir)$(outname)
moduletarget = loop.cpp checkenvar.cpp isdir.cpp
target = meow.cpp
pdir = pytarget/
ptarget = bark.py cpy.py
pcp = bark.bin cpy.bin
pflags = -m nuitka --follow-imports
pcomp = python3
cc=g++
.SILENT all:
all:
	mkdir -p out
	cp $(maindir)$(target) $(outdir)$(target)
	cp -r $(moduledir)* $(outdir)
	cp -r $(maindir)$(pdir)* $(outdir)
	cd out && $(cc) $(target) $(moduletarget) -o $(outname) -I$(currentdir)include --std=c++17
	echo Target and modules compiled!
	cd out && $(pcomp) $(pflags) $(ptarget) && cp $(pcp) ../bark
	echo Warning! Bark has compiled in non-standalone mode.
	echo Target Python modules OK!
clean:	
	rm -rf out/
install:
	echo installing...
	cp $(currentdir)meow /usr/bin/meow
        cp $(currentdir)bark /usr/bin/bark
	echo done!
soft_install:
	export PATH=$PATH:$(currentdir)
	echo soft-installed!
uninstall:
	rm /usr/bin/meow
        rm /usr/bin/bark
target-py:
	cd out && $(pcomp) $(pflags) --standalone $(ptarget) && cd bark.dist && cp bark ../../bark
	echo Target Python modules OK!
