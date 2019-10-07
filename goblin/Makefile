.SILENT all-goblin:
all-goblin:
	gccgo goblin.go -O3 -o goblingo
	echo [CC] goblingo
	python3 -m nuitka --follow-imports goblin.py
	echo [CC] goblinpy