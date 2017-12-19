# -*- coding: utf-8 -*-

from odemethods import Taylor
from math import exp

def f(x, y):
    return -2.0*y
def f1(x, y):
    return 4.0*y
def f2(x, y):
    return -8.0*y

functions = [f, f1, f2]
# print(functions[0](1,1))
res_pvi = Taylor(functions, 0.5, 0.0, 3.0, 4)
res_pvi.calc()
with open("test.txt", "w") as outputFile:
    print >> outputFile, res_pvi
