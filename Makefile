maindir=main/
moduledir=modules/
cc=g++
all:
	mkdir -f out
	cd out
	cp $(maindir) meow.cpp meow.cpp
	cp $(moduledir) mew.cpp mew.cpp
	$(cc) mew.cpp meow.cpp -o main
clean:	
	rm -rf out/

