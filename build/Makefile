import ./../Makefile
.SILENT build-meow:
build-meow:
	mkdir -p meowproj_$(version)
	mkdir -p meowproj_$(version)/DEBIAN/
	mkdir -p meowproj_$(version)/usr
	mkdir -p meowproj_$(version)/usr/local/bin
	cp ./../bin/*  meowproj_$(version)/usr/local/bin
	dpkg-deb --build meowproj_$(version)
