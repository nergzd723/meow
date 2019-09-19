version = 0.11-1
.SILENT all:
.PHONY: all bark cpy dip dutils exo goblin lt meow mkdip no tap yedd aname forker
targets = bark cpy dip dutils exo goblin lt meow mkdip no tap yedd aname forker
all: clean do copy
do: $(targets)
bark: bark/bark.cpp
	make -j1 -C bark
cpy: cpy/cpy.py
	make -j1 -C cpy
dip: dip/dip.py
	make -j1 -C dip
dutils: dutils/createimage.py
	make -j1 -C dutils
exo: exo/exo.py
	make -j1 -C exo
goblin: goblin/goblin.go
	make -j1 -C goblin
lt: lt/lt.py
	make -j1 -C lt
meow: meow/meow.cpp
	make -j1 -C meow
mkdip: mkdip/mkdip.py 
	make -j1 -C mkdip
no: no/no.go
	make -j1 -C no
tap: tap/tap.py
	make -j1 -C tap
yedd: yedd/yedd.cpp
	make -j1 -C yedd
aname: aname/aname.py #aname.cpp it is not good to cheat!
	make -j1 -C aname
forker: forker/forker.cpp
	make -j1 -C forker

copy: $(targets)
	mkdir -p bin
	cp bark/bark.exe bin/barkcs
	cp bark/bark++ bin/bark++
	cp bark/bark.bin bin/bark
	cp cpy/cpy++ bin/cpy++
	cp cpy/cpy.bin bin/cpy
	cp dip/dip.bin bin/dip
	#cp dutils/filer bin/filer
	cp dutils/gendir.bin bin/gendir
	cp dutils/stenc.bin bin/stenc
	cp dutils/aexec.bin bin/aexec
	cp exo/exo++ bin/exo++
	cp exo/exo.bin bin/exo
	cp goblin/goblingo bin/goblin
	cp goblin/goblin.bin bin/goblinpy
	cp lt/lt.bin bin/lt
	cp meow/meow.exe bin/meowcs
	cp meow/meow++ bin/meow
	cp mkdip/mkdip.bin bin/mkdip
	cp no/no.bin bin/no
	cp no/nogo bin/nogo
	cp tap/tap.bin bin/tap
	cp yedd/yedd bin/yedd
	cp aname/aname.bin bin/aname
	#cp forker/forker bin/forker

clean:
	rm -rf bin/* */*.build/* */*.bin */*.exe

build: all
	make -C build

install: build
	dpkg -i build/meowproj_$(version).deb
