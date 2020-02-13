## How to use:
```bash
c++ -o read_02 `root-config --glibs --cflags` CfgParser.cc LHEF.cc -lm read_02.cpp

./read_02 cfg/mg5_v4.cfg -1

python compare_polar.py
```