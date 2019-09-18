.SILENT build-meow
build-meow:
	rm -rf meowproj_0.10-1
	mkdir -p meowproj_0.10-1
	mkdir -p meowproj_0.10-1/DEBIAN/
	mkdir -p meowproj_0.10-1/DEBIAN/control
	mkdir -p meowproj_0.10-1/usr
	mkdir -p meowproj_0.10-1/usr/local/bin
	cp ./../bin/*.*  meowproj_0.10-1/usr/local/bin
	dpkg-deb --build meowproj_0.10-1
