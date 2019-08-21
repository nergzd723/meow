# meow
# Multiple C++ and Python utils

There are only availible two variants now - bark for removing and meow for reading from file

# How to install?
Do `make` to build all supported modules and targets. Then `make install` to install to /usr/bin and `make uninstall` to delete binaries from it.
# Troubleshooting
## Bark has compiled in non-standalone mode. 
It means that Bark cannot be run on systems with no Python installed. Do `make target-py` to compile in standalone mode. No guarantees.
