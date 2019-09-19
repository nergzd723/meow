version = 0.11-1
.SILENT all:
.PHONY: all bark cpy dip dutils exo goblin lt meow mkdip no tap yedd aname forker
targets = bark cpy dip dutils exo goblin lt meow mkdip no tap yedd aname forker
all: do copy
do: $(targets)
bark: bark/bark.cpp
	make -C bark
cpy: cpy/cpy.py
	make -C cpy
dip: dip/dip.py
	make -C dip
dutils: dutils/createimage.py
	make -C dutils
exo: exo/exo.py
	make -C exo
goblin: goblin/goblin.go
	make -C goblin
lt: lt/lt.py
	make -C lt
meow: meow/meow.cpp
	make -C meow
mkdip: mkdip/mkdip.py
	make -C mkdip
no: no/no.go
	make -C no
tap: tap/tap.py
	make -C tap
yedd: yedd/yedd.cpp
	make -C yedd
aname: aname/aname.py #aname.cpp it is not good to cheat!
	make -C aname
forker: forker/forker.cpp
	make -C forker

copy: $(targets)
	mkdir -p bin
	cp bark/bark.exe bin/barkcs
	cp bark/bark++ bin/bark++
	cp bark/bark.bin bin/barkpy
	cp cpy/cpy++ bin/cpy++
	cp cpy/cpy.bin bin/cpypy
	cp dip/dip.bin bin/dip
	#cp dutils/filer bin/filer
	cp dutils/gendir.bin bin/gendir
	cp dutils/stenc.bin bin/stenc
	cp dutils/aexec.bin bin/aexec
	cp exo/exo++ bin/exo++
	cp exo/exo.bin bin/exopy
	cp goblin/goblingo bin/goblingo
	cp goblin/goblin.bin bin/goblinpy
	cp lt/lt.bin bin/lt
	cp meow/meow.exe bin/meowcs
	cp bark/bark++ bin/meow++
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
