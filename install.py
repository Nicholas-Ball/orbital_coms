# this file will install the necessary components for orbital_coms to work

# os version check
from sys import *
import os

# for running commands on the os because i'm lazy
def run(input):
    os.system(input)

print("------------------------------------------------------------------------")
print("Checking os platform...")
print("------------------------------------------------------------------------")

if platform == "linux" or platform == "linux2": # linux
    print("------------------------------------------------------------------------")
    print("Setting up for GNU/Linux...")
    print("------------------------------------------------------------------------")

    # Ensure that we have elevated permissions
    if not os.geteuid() == 0:
        exit("\nRequires elevated permissions\n")

    # install cmake cross platform
    run("sudo apt install cmake g++ make libpcre3 libpcre3-dev python3-dbg -y || sudo dnf install cmake gcc-c++ python3-dbg make libpcre3 libpcre3-dev swig -y || pacman -Syu cmake g++ make python3-dbg libpcre3 libpcre3-dev swig")

    # download swig from source
    run("git clone https://github.com/swig/swig.git")

    # build swig from source
    run("cd swig && ./autogen.sh && ./configure && make && make install")

    # download SoapySDR
    run("git clone https://github.com/pothosware/SoapySDR.git")

    # build from source if the last bit errors out, it is okay
    run("cd SoapySDR && mkdir build && cd build && cmake .. && make -j4 && sudo make install && sudo ldconfig && SoapySDRUtil --info")

elif platform == "darwin": # OS X
    print("------------------------------------------------------------------------")
    print("Setting up for Mac...")
    print("------------------------------------------------------------------------")

elif platform == "win32": # Windows
    print("------------------------------------------------------------------------")
    print("Setting up for Windows...")
    print("------------------------------------------------------------------------")
