cc=clang++
currentdir = $(shell pwd)/
.SILENT all-bark:
all-bark:
	$(cc) bark.cpp -o bark++ -O3  -lboost_filesystem -lboost_system
	echo [CC] bark++
	python3 -m nuitka --follow-imports bark.py
	echo [CC] barkpy
	mcs bark.cs