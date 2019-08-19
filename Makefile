maindir=main/
moduledir=modules/
outdir=out/
outname=main.o
cc=g++
.SILENT:

	all:
		mkdir -p out
		cp $(maindir)meow.cpp $(outdir)meow.cpp
		cp $(moduledir)mew.cpp $(outdir)mew.cpp
		$(cc) $(outdir)mew.cpp $(outdir)meow.cpp -o $(outname)
	clean:	
		rm -rf out/

