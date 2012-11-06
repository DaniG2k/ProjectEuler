#! /usr/bin/python
from tools import lcm

print reduce(lambda x, y: lcm(x, y), range(1,21))
