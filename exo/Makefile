cc=clang++
currentdir = $(shell pwd)/
.SILENT all-exo:
all-exo:
	$(cc) exo.cpp -o exo++ -I$(currentdir)include  -lboost_filesystem -lboost_system
	echo [CC] exo++
	python3 -m nuitka --follow-imports exo.py
	echo [CC] exopy
