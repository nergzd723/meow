cc=clang++
currentdir = $(shell pwd)/
SILENT all:
all-filer:
		$(cc) filer.cpp -o filer -I$(currentdir)include  -lboost_filesystem
		echo [CC] filer
		python3 -m nuitka --follow-imports gendir.py
		echo [CC] gendir
		python3 -m nuitka --follow-imports stenc.py
		echo [CC] stenc
		