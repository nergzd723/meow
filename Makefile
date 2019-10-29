include Makeheader
.SILENT all:
.PHONY: $(targets) changelog copy
all: $(targets) copy
bark:
	$(MAKE) -C bark
cpy:
	$(MAKE) -C cpy
dip:
	$(MAKE) -C dip
dutils:
	$(MAKE) -C dutils
exo:
	$(MAKE) -C exo
goblin:
	$(MAKE) -C goblin
lt:
	$(MAKE) -C lt
meow:
	$(MAKE) -C meow
mkdip:
	$(MAKE) -C mkdip
no:
	$(MAKE) -C no
tap:
	$(MAKE) -C tap
yedd:
	$(MAKE) -C yedd
aname:
	$(MAKE) -C aname
kid:
	$(MAKE) -C kid
patrat:
	$(MAKE) -C patrat
pyma:
	$(MAKE) -C pyma
copy: $(targets)
	mkdir -p bin
	mv bark/bark.exe bin/barkcs
	cp bark/bark++ bin/bark++
	mv bark/bark.bin bin/bark
	mv cpy/cpy++ bin/cpy++
	mv cpy/cpy.bin bin/cpy
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
	mv meow/meow++ bin/meow
	mv mkdip/mkdip.bin bin/mkdip
	mv no/no.bin bin/no
	mv no/nogo bin/nogo
	mv tap/tap.bin bin/tap
	mv tap/tap++ bin/tap++
	mv yedd/yedd bin/yedd
	mv aname/aname.bin bin/aname
	#mv forker/forker bin/forker
	mv kid/kid.bin bin/kid
	mv kid/pit.bin bin/pit
	mv kid/kid++ bin/kid++
	mv patrat/patrat.bin bin/patrat
	mv aname/aname++ bin/aname++
	mv patrat/patratgit.bin bin/patratgit
	#mv pyma/pyma.bin bin/pyma

clean:
	rm -rf bin/* */*.build/* */*.bin */*.exe

build: all
	$(MAKE) -C build

install: build
	dpkg -i build/meowproj_$(version)

install_legacy:
	cp bin/* $(DESTDIR)/bin

changelog:
	echo 0.12-1 Create kid module. Kills a process. Add pit module. Bugfixes.
	echo 0.13-1 Add patrat module. VCS on Python.
	echo 0.14-1 Finish patrat. Add patrat-branch.
	echo 0.15-1 Add patrat-git(experimental)
	echo 0.16-1 Full patrat-git. Patrat v0.5
