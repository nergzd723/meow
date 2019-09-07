cc=clang++
currentdir = $(shell pwd)/
.SILENT all-meow:
all-meow:
	$(cc) meow.cpp -o meow++ -I$(currentdir)include -lboost_filesystem -lboost_system
	echo [CC] meow++
	mcs meow.cs
	echo [CC] meowcs
