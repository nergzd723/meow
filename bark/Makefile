cc=clang++
currentdir = $(shell pwd)/
SILENT all:
all-bark:
	$(cc) bark.cpp -o bark++ -I$(currentdir)include  -lboost_filesystem
	echo [CC] bark++
	python3 -m nuitka --follow-imports --clang bark.py
	echo [CC] barkpy
	mcs bark.cs