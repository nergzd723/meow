cc=clang++
currentdir = $(shell pwd)/
.SILENT all-exo:
all-exo:
	$(cc) exo.cpp -o exo++ -O3 
	echo [CC] exo++
	python3 -m nuitka --follow-imports exo.py
	echo [PY] exopy
