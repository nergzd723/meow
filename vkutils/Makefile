cc=clang++
currentdir = $(shell pwd)/
ccflags = -O3 -lcurl -g
.SILENT .PHONY all-vkutils:
all-vkutils:
	$(cc) $(ccflags) lib/api.cpp lib/attachment.cpp liker.cpp -o liker
	echo [CC] liker
