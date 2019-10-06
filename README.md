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
In Arch Linux it's in two commands:
`sudo pacman -S gcc-go mono python-pip base-devel boost python python3 python3-pip` and
`sudo pip install nuitka termcolor`...

In Debian-like systems with apt and dpkg do
` sudo apt install libboost-all-dev python python-pip gccgo &&
  sudo apt install -y python-setuptools python3-setuptools &&
  pip install setuptools &&
  pip3 install nuitka termcolor && `
