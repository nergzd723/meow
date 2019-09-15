.SILENT all:
all: do clean copy
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
	mv meowshell/msh.bin bin/msh
do:
	make -C bark 
	make -C cpy
	make -C dip 
	make -C dutils 
	make -C exo
	make -C goblin 
	make -C lt
	make -C meow
	make -C mkdip
	make -C no
	make -C tap
	make -C yedd
	make -C aname
	make -C forker
	make -C meowshell
clean:
	rm -rf bin/
