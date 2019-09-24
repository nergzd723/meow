cc=clang++
currentdir = $(shell pwd)/
.SILENT all-cpy:
all-cpy:
		$(cc) cpy.cpp -o cpy++ -O3 -lboost_filesystem -lboost_system
		echo [CC] cpy
		python3 -m nuitka cpy.py
		echo [PY] cpy
