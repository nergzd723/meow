maindir=main/
moduledir=modules/
outdir=out/
debugdir=out_debug/
outname=meow
currentdir = $(shell pwd)/
currentmeowdir = $(currentdir)$(outname)
moduletarget = checkenvar.cpp isdir.cpp
target = meow.cpp
cc=clang++
all:
	mkdir -p out
	cp $(maindir)$(target) $(outdir)$(target)
	cp -r $(moduledir)* $(outdir)
	cp -r $(maindir)$(pdir)* $(outdir)
	cd out && $(cc) ~/meow/main/$(target)  ~/meow/modules/$(moduletarget) -o $(outname) -I$(currentdir)include -lboost_filesystem && cp ~/meow/out/meow ../meow
	cd out && $(cc) ~/meow/main/bark.cpp -o bark++ -I$(currentdir)include  -lboost_filesystem && cp ~/meow/out/bark++ ../bark++
	cd out && $(cc) ~/meow/main/exo.cpp -o exo++ -I$(currentdir)include  && cp ~/meow/out/exo++ ../exo++
	cd out && $(cc) ~/meow/main/yedd.cpp -o yedd++ -I$(currentdir)include  -lboost_filesystem && cp ~/meow/out/yedd++ ../yedd++
	echo Target and modules compiled!
debug:
	mkdir -p out_debug
	cp $(maindir)$(target) $(debugdir)$(target)
	cp -r $(moduledir)* $(debugdir)
	cp -r $(maindir)$(pdir)* $(debugdir)
	cd out_debug && $(cc) ~/meow/main/$(target)  ~/meow/modules/$(moduletarget) -o $(outname) -I$(currentdir)include -g -lboost_filesystem && cp ~/meow/out/meow ../meow
	cd out_debug && $(cc) ~/meow/main/bark.cpp -o bark++ -I$(currentdir)include  -g -lboost_filesystem && cp ~/meow/out/bark++ ../bark++
	cd out_debug && $(cc) ~/meow/main/exo.cpp -o exo++ -g -I$(currentdir)include  && cp ~/meow/out/exo++ ../exo++
	cd out_debug && $(cc) ~/meow/main/yedd.cpp -o yedd++ -g -I$(currentdir)include  -lboost_filesystem && cp ~/meow/out/yedd++ ../yedd++
	echo Target and modules compiled!
clean:
	rm -rf out/
install:
	echo installing...
	cp $(currentdir)meow /usr/bin/meow
	cp $(currentdir)bark++ /usr/bin/bark++
	cp $(currentdir)exo++ /usr/bin/exo++
	cp $(currentdir)yedd++ /usr/bin/yedd++
	echo done!
soft_install:
	export PATH=$PATH:$(currentdir)
	echo soft-installed!
uninstall:
	rm /usr/bin/meow
	rm /usr/bin/bark++
	rm /usr/bin/yedd++
	rm /usr/bin/exo++
