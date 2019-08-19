maindir=main/
moduledir=modules/
outdir=out/
outname=meow
currentdir = $(shell pwd)/
currentmeowdir = $(currentdir)$(outname)
moduletarget = mew.cpp, checkforvar.cpp
target = meow.cpp
cc=g++
.SILENT all:
all:
	mkdir -p out
	cp $(maindir)$(target) $(outdir)$(target)
	cp $(moduledir){$(moduletarget)} $(outdir)$(moduletarget)
	$(cc) $(outdir)mew.cpp $(outdir)$(moduletarget) -o $(outname) -I$(currentdir)include
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
