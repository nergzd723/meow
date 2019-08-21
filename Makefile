maindir=main/
moduledir=modules/
outdir=out/
outname=meow
currentdir = $(shell pwd)/
currentmeowdir = $(currentdir)$(outname)
moduletarget = loop.cpp checkenvar.cpp isdir.cpp
target = meow.cpp
ptarget = bark.py
pflags = -m nuitka --standalone --follow-imports
pcomp = python3
cc=g++
.SILENT all:
all:
	mkdir -p out
	cp $(maindir)$(target) $(outdir)$(target)
	cp -r $(moduledir)* $(outdir)
	cd out && $(cc) $(target) $(moduletarget) -o $(outname) -I$(currentdir)include --std=c++17
	echo Target and modules compiled!
	$(pcomp) $(pflags) $(ptarget)
	echo Target Python modules OK!
clean:	
	rm -rf out/
install:
	echo installing...
	cp $(currentdir)meow /usr/bin/meow
	echo done!
soft_install:
	export PATH=$PATH:$(currentdir)
	echo soft-installed!
uninstall:
	rm /usr/bin/meow
