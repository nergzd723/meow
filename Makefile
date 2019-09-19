version = 0.11-1
.SILENT all:
.PHONY: all bark cpy dip dutils exo goblin lt meow mkdip no tap yedd aname forker
targets = bark cpy dip dutils exo goblin lt meow mkdip no tap yedd aname forker
all: $(targets)
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

copy:
	mkdir -p bin
	mv bark/bark.exe bin/barkcs
	cp bark/bark++ bin/bark++
	mv bark/bark.bin bin/barkpy
	mv cpy/cpy++ bin/cpy++
	mv cpy/cpy.bin bin/cpypy
	mv dip/dip.bin bin/dip
	#mv dutils/filer bin/filer
	mv dutils/gendir.bin bin/gendir
	mv dutils/stenc.bin bin/stenc
	mv dutils/aexec.bin bin/aexec
	mv exo/exo++ bin/exo++
	mv exo/exo.bin bin/exopy
	mv goblin/goblingo bin/goblingo
	mv goblin/goblin.bin bin/goblinpy
	mv lt/lt.bin bin/lt
	mv meow/meow.exe bin/meowcs
	mv bark/bark++ bin/meow++
	mv mkdip/mkdip.bin bin/mkdip
	mv no/no.bin bin/no
	mv no/nogo bin/nogo
	mv tap/tap.bin bin/tap
	mv yedd/yedd bin/yedd
	mv aname/aname.bin bin/aname
	mv forker/forker bin/forker

clean:
	rm -rf bin/* */*.build/* */*.bin */*.exe

build: all
	make -C build

install: build
	dpkg -i build/meowproj_0.11-1