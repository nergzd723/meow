.SILENT all:
all-goblin:
	gccgo goblin.go -o goblingo
	echo [CC] goblingo
	python3 -m nuitka --follow-imports --clang goblin.py
	echo [CC] goblinpy