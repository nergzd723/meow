maindir=main/
moduledir=modules/
cc=g++
all:
	mkdir -p out
	cp $(maindir) meow.cpp meow.cpp
	cp $(moduledir) mew.cpp mew.cpp
	cd out
	$(cc) mew.cpp meow.cpp -o main
clean:	
	rm -rf out/

