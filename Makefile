maindir=main/
moduledir=modules/
outdir=out/
outname=meow
currentdir = $(shell pwd)/
currentmeowdir = $(currentdir)$(outname)
cc=g++
.SILENT all:
all:
	mkdir -p out
	cp $(maindir)meow.cpp $(outdir)meow.cpp
	cp $(moduledir)mew.cpp $(outdir)mew.cpp
	$(cc) $(outdir)mew.cpp $(outdir)meow.cpp -o $(outname) -linclude
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
