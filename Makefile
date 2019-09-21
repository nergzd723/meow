include Makeheader
.SILENT all:
.PHONY: $(targets) changelog copy
all: $(targets) copy
bark:
	make -C bark
cpy:
	make -C cpy
dip:
	make -C dip
dutils:
	make -C dutils
exo:
	make -C exo
goblin:
	make -C goblin
lt:
	make -C lt
meow:
	make -C meow
mkdip:
	make -C mkdip
no:
	make -C no
tap:
	make -C tap
yedd:
	make -C yedd
aname:
	make -C aname
forker:
	make -C forker
kid:
	make -C kid
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
	mv kid/kid.bin bin/kid
	mv kid/pit.bin bin/pit
clean:
	rm -rf bin/* */*.build/* */*.bin */*.exe

build: all
	make -C build

install: build
	dpkg -i build/meowproj_$(version)

changelog:
	echo 0.12-1 Create kid module. Kills a process. Add pit module. Bugfixes.
