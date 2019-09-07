cc=clang++
currentdir = $(shell pwd)/
SILENT all:
all-cpy:
		$(cc) cpy.cpp -o cpy++ -I$(currentdir)include  -lboost_filesystem
		echo [CC] cpy
		python3 -m nuitka --clang cpy.py
