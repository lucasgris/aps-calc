# -*- coding: utf-8 -*-
from odemethods import Euler

def f(x, y):
    return (2 + (x**2)*y)/x

# Cálculo de resultados
res_pvi = Euler(f, 0.1, 1, 3, 5)
res_pvi.calc()
with open("output/ex05-2-euler.txt", "w") as outputFile:
    print >> outputFile, res_pvi
