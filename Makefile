maindir=main/
moduledir=modules/
outdir=out/
outname=meow
currentdir = $(shell pwd)/
currentmeowdir = $(currentdir)$(outname)
moduletarget = loop.cpp checkenvar.cpp isdir.cpp
target = meow.cpp
pdir = pytarget/
ptarget = bark.py
ptarget2 = cpy.py
ptargetlt = lt.py
ptargettap = tap.py
ptargetdip = dip.py
ptargetexo = exo.py
pcp = bark.bin
pcp2 = cpy.bin
pcp3 = lt.bin
pcp4 = tap.bin
pcp5 = dip.bin
pcp6 = exo.bin
pflags = -m nuitka --follow-imports
pcomp = python3
cc=clang++
pcc = cd out && $(pcomp) $(pflags)
.SILENT all:
all:
	mkdir -p out
	cp $(maindir)$(target) $(outdir)$(target)
	cp -r $(moduledir)* $(outdir)
	cp -r $(maindir)$(pdir)* $(outdir)
	cd out && $(cc) $(target) $(moduletarget) -o $(outname) -I$(currentdir)include --std=c++17
	echo Target and modules compiled!
	$(pcc) $(ptarget) && cp $(pcp) ../bark
	$(pcc) $(ptarget2) && cp $(pcp2) ../cpy
	$(pcc) $(ptargetlt) && cp $(pcp3) ../lt
	$(pcc) $(ptargettap) && cp $(pcp4) ../tap
	$(pcc) $(ptargetdip) && cp $(pcp5) ../dip
	$(pcc) $(ptargetexo) && cp $(pcp6) ../exo
	echo Warning! Python modules has compiled in non-standalone mode.
	echo Target Python modules OK!
clean:	
	rm -rf out/
install:
	echo installing...
	cp $(currentdir)meow /usr/bin/meow
	cp $(currentdir)bark /usr/bin/bark
	cp $(currentdir)cpy /usr/bin/cpy
	cp $(currentdir)lt /usr/bin/lt
	cp $(currentdir)tap /usr/bin/tap
	cp $(currentdir)dip /usr/bin/dip
	cp $(currentdir)exo /usr/bin/exo
	echo done!
soft_install:
	export PATH=$PATH:$(currentdir)
	echo soft-installed!
uninstall:
	rm /usr/bin/meow
	rm /usr/bin/bark
	rm /usr/bin/cpy
	rm /usr/bin/lt
	rm /usr/bin/tap
	rm /usr/bin/dip
	rm /usr/bin/exo
target-py:
	cd out && $(pcomp) $(pflags) --standalone $(ptarget) && cd bark.dist && cp bark ../../bark
	cd out && $(pcomp) $(pflags) --standalone $(ptarget2) && cd cpy.dist && cp cpy ../../cpy
	cd out && $(pcomp) $(pflags) --standalone $(ptargetlt) && cd lt.dist && cp lt ../../lt
	cd out && $(pcomp) $(pflags) --standalone $(ptargettap) && cd tap.dist && cp tap ../../tap
	cd out && $(pcomp) $(pflags) --standalone $(ptargetdip) && cd dip.dist && cp dip ../../dip
	cd out && $(pcomp) $(pflags) --standalone $(ptargetexo) && cd exo.dist && cp exo ../../exo
	echo Target Python modules OK!
