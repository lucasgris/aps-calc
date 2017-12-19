# -*- coding: utf-8 -*-
from odemethods import Taylor

def f(x, y):
    return y*(x**2) - y

functions = [f]
# Cálculo de resultados
res_pvi = Taylor(functions, 0.25, 0, 1, 8)
res_pvi.calc()
with open("output/ex03a-2_h025.txt", "w") as outputFile:
    print >> outputFile, res_pvi
