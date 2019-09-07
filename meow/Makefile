cc=clang++
currentdir = $(shell pwd)/
.SILENT all:
all-meow:
	$(cc) meow.cpp -o meow++ -I$(currentdir)include -lboost_filesystem
	echo [CC] meow++
	mcs meow.cs
	echo [CC] meowcs
