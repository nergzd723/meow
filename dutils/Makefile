cc=clang++
currentdir = $(shell pwd)/
.SILENT all-util:
all-util:
		#$(cc) filer.cpp -o filer -I$(currentdir)include  -lboost_filesystem -lboost_system
		#echo [CC] filer
		python3 -m nuitka --follow-imports gendir.py
		echo [PY] gendir
		python3 -m nuitka --follow-imports stenc.py
		echo [PY] stenc
		python3 -m nuitka --follow-imports aexec.py
		echo [PY] aexec
		python3 -m nuitka --follow-imports createimage.py
		echo [PY] createimage
		
