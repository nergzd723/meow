.SILENT all:
targets = bark cpy dip dutils exo goblin lt meow mkdip no tap yedd aname forker
all: $(targets)
bark: bark/bark.cpp
	make -C bark
cpy: cpy/cpy.py
	make -C cpy
dip: dip.py
	make -C dip
dutils: dutils
	make -C dutils
exo: exo.py exo.cpp exo.cs
	make -C exo
goblin: goblin.go goblin.py
	make -C goblin
lt: lt.py
	make -C lt
meow: meow.cpp meow.cs
	make -C meow
mkdip: mkdip.py
	make -C mkdip
no: no.go no.py no.cpp
	make -C no
tap: tap.py
	make -C tap
yedd: yedd.cpp
	make -C yedd
aname: aname.py aname.cpp
	make -C aname
forker: forker.cpp
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
