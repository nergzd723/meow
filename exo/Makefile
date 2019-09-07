cc=clang++
currentdir = $(shell pwd)/
.SILENT all-exo:
all-exo:
	$(cc) exo.cpp -o exo++ -I$(currentdir)include  -lboost_filesystem
	echo [CC] exo++
	python3 -m nuitka --follow-imports --clang exo.py
	echo [CC] exopy
