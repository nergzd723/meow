.SILENT all-no:
all-no:
	python3 -m nuitka no.py
	echo [PY] no
	gccgo no.go -O3 -o nogo
	echo [CC] nogo
	clang++ -O3 no.cpp -o no++
	echo [CC] no++
