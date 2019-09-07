cc=clang++
currentdir = $(shell pwd)/
.SILENT all-cpy:
all-cpy:
		$(cc) cpy.cpp -o cpy++ -I$(currentdir)include  -lboost_filesystem -lboost_system
		echo [CC] cpy
		python3 -m nuitka --clang cpy.py
