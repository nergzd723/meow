maindir=main/
moduledir=modules/
outdir=out/
outname=meow
currentdir = $(PWD)/
cc=g++
.SILENT all:
all:
	mkdir -p out
	cp $(maindir)meow.cpp $(outdir)meow.cpp
	cp $(moduledir)mew.cpp $(outdir)mew.cpp
	$(cc) $(outdir)mew.cpp $(outdir)meow.cpp -o $(outname)
clean:	
	rm -rf out/
install:
	echo installing...
	cp $(currentdir)meow /usr/bin/meow
	echo done!
soft_install:
	export PATH = $PATH:$(currentdir)meow
	echo soft-installed!
uninstall:
	rm /usr/bin/meow
