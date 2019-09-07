copy:
	mkdir -p bin
	cp bark/bark.exe bin/barkcs
	cp bark/bark++ bin/bark++
	cp bark/bark.bin bin/barkpy
	cp cpy/cpy++ bin/cpy++
	cp cpy/cpy.bin bin/cpypy
	cp dip/dip.bin bin/dip
	cp dutils/filer bin/filer
	cp dutils/gendir.bin bin/gendir
	cp dutils/stenc.bin dutils/stenc
	cp exo/exo++ bin/exo++
	cp exo/exo.bin bin/exopy
	cp goblin/goblingo bin/goblingo
	cp goblin/goblin.bin bin/goblin.py
	cp lt/lt.bin bin/lt
	cp meow/meow.exe bin/meowcs
	cp bark/bark++ bin/meow++
	cp mkdip/mkdip.bin bin/mkdip
	cp no/no.bin bin/no
	cp tap/tap.bin bin/tap
	cp yedd/yedd bin/yedd
all: do
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
clean:
	rm -rf bin/
