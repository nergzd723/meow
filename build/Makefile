.SILENT build-meow:
build-meow:
	mkdir -p meowproj_0.11-1
	mkdir -p meowproj_0.11-1/DEBIAN/
	mkdir -p meowproj_0.11-1/usr
	mkdir -p meowproj_0.11-1/usr/local/bin
	cp ./../bin/*  meowproj_0.11-1/usr/local/bin
	dpkg-deb --build meowproj_0.11-1
