# meow
![alt text] (https://github.com/nergzd723/meow/releases/download/0.001/94373f3b-0849-421a-8383-9461ef50d89e_200x200.png)
# Multiple C++ utils

`bark` for removing,`meow` for reading from file, `lt` for showing file list in directory and `tap` to create new file or to change its access date to newer one

# How to install?
Do `make` to build all supported modules and targets. Then `make install` to install to /usr/bin and `make uninstall` to delete binaries from it.
# Troubleshooting
## Target Python modules have compiled in non-standalone mode. 
It means that Python modules cannot be run on systems with no Python installed. Do `make target-py` to compile in standalone mode. No guarantees it will work, but it's worth trying.
## Something isnt right!
Rewrite of build system might affect it. Checkout another branch.
