# -*- coding: utf-8 -*-
from odemethods import Euler

def f(x, y):
    return 4 - 2*x

# Cálculo de resultados
res_pvi = Euler(f, 0.5, 0, 2, 10)
res_pvi.calc()
with open("output/ex01-2_h05.txt", "w") as outputFile:
    print >> outputFile, res_pvi
