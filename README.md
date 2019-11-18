# meow
[![CodeFactor](https://www.codefactor.io/repository/github/nergzd723/meow/badge)](https://www.codefactor.io/repository/github/nergzd723/meow)
# Multiple C++ utils

`bark` for removing,`meow` for reading from file, `lt` for showing file list in directory and `tap` to create new file or to change its access date to newer one

# How to install?
Do `make` to build all supported modules and targets. Then `make install` to install to /usr/bin and `make uninstall` to delete binaries from it.

# Troubleshooting
## Target Python modules have compiled in non-standalone mode.
It means that Python modules cannot be run on systems with no Python installed. No way to abuse that, binaries size is too high if compile libs.
## Something isnt right!
Rewrite of build system might affect it. Checkout another branch.

# Dependencies
Do `chmod +x configure.py && ./configure.py` to install all dependencies. It will automatically detect your package manager.
