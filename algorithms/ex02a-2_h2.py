# -*- coding: utf-8 -*-
from odemethods import Euler

def f(x, y):
    return -x/y

# Cálculo e exibição de resultados
res_pvi = Euler(f, 2.0, 0, 20, 8)
res_pvi.calc()
with open("output/ex02a-2_h2.txt", "w") as outputFile:
    print >> outputFile, res_pvi
