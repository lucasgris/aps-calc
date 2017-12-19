# -*- coding: utf-8 -*-
from odemethods import Euler

def f(x, y):
    return 4 - 2*x

# Cálculo de resultados
res_pvi = Euler(f, 0.125, 0, 2, 40)
res_pvi.calc()
with open("output/ex01-2_h0125.txt", "w") as outputFile:
    print >> outputFile, res_pvi
