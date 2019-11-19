#!/usr/bin/env python3
import distutils.spawn
import os
command_for_apt="sudo apt install clang git libboost-all-dev python3 python python3-pip python-pip gccgo && sudo apt install -y python-setuptools python3-setuptools && pip install setuptools && pip3 install nuitka termcolor"
command_for_pacman="sudo pacman -S gcc-go clang mono python-pip base-devel boost python python3 python3-pip g++ git && pip install setuptools && pip3 install nuitka termcolor"
def is_apt():
    return distutils.spawn.find_executable("apt") is not None
def is_pacman():
    return distutils.spawn.find_executable("pacman") is not None
if is_apt():
    os.system(command_for_apt)
if is_pacman():
    os.system(command_for_pacman)