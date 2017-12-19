# -*- coding: utf-8 -*-

from odemethods import Taylor
from math import exp

def f(x, y):
    return y/(x+1)

functions = [f]
# print(functions[0](1,1))
res_pvi = Taylor(functions, 0.1, 0.0, 1.0, 4)
res_pvi.calc()
with open("test.txt", "w") as outputFile:
    print >> outputFile, res_pvi
