#!/bin/bash
#$ a1= "python test3.py"
#$ a2=  "g++ -ggdb `pkg-config --cflags opencv` -o `basename rect.cpp .cpp` rect.cpp `pkg-config --libs opencv` -std=c++0x"
#$ a3=  "python d.py"
eval "python image_color_segementation.py"
eval "g++ -ggdb `pkg-config --cflags opencv` -o `basename rect.cpp .cpp` rect.cpp `pkg-config --libs opencv` -std=c++0x"
eval "./rect"
eval 'python d.py'

