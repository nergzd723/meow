maindir=main/
moduledir=modules/
outdir=out/
cc=g++
all:
	mkdir -p out
	cp $(maindir)meow.cpp $(outdir)meow.cpp
	cp $(moduledir)mew.cpp $(outdir)mew.cpp
	cd out
	$(cc) mew.cpp meow.cpp -o main
clean:	
	rm -rf out/

