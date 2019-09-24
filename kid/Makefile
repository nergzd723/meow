.SILENT all-kid:
all-kid:
	python3 -m nuitka --nofollow-imports kid.py
	echo [PY] kid
	clang++ -O3 -o kid++ kid.cpp
	echo [CC] kid++
	python3 -m nuitka --nofollow-imports pit.py
	echo [PY] pit
	