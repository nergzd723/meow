# meow
# Multiple C++ and Python utils

`bark` for removing,`meow` for reading from file, `lt` for showing file list in directory and `tap` to create new file or to change its access date to newer one

# How to install?
Do `make` to build all supported modules and targets. Then `make install` to install to /usr/bin and `make uninstall` to delete binaries from it.
# Troubleshooting
## Target Python modules have compiled in non-standalone mode. 
It means that Python modules cannot be run on systems with no Python installed. Do `make target-py` to compile in standalone mode. No guarantees it will work, but it's worth trying.
