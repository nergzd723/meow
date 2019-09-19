version = 0.11-1
.SILENT all:
.PHONY: all bark cpy dip dutils exo goblin lt meow mkdip no tap yedd aname forker
targets = bark cpy dip dutils exo goblin lt meow mkdip no tap yedd aname forker
all: clean do copy
do: $(targets)
bark: bark/bark.cpp
	make -C -j1 bark
cpy: cpy/cpy.py
	make -C -j1 cpy
dip: dip/dip.py
	make -C -j1 dip
dutils: dutils/createimage.py
	make -C dutils -j1
exo: exo/exo.py
	make -C exo -j1
goblin: goblin/goblin.go
	make -C goblin -j1
lt: lt/lt.py
	make -C lt -j1
meow: meow/meow.cpp
	make -C meow -j1
mkdip: mkdip/mkdip.py 
	make -C mkdip -j1
no: no/no.go
	make -C no -j1
tap: tap/tap.py
	make -C tap -j1
yedd: yedd/yedd.cpp
	make -C yedd -j1
aname: aname/aname.py #aname.cpp it is not good to cheat!
	make -C aname -j1
forker: forker/forker.cpp
	make -C forker -j1

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
