# -*- coding: utf-8 -*-
from odemethods import RungeKutta

def f(x, y):
    return y*(x**2 - 1)

# Cálculo de resultados
res_pvi = RungeKutta(f, 0.25, 0, 1, 8)
res_pvi.calc()
with open("output/ex03c-2_h025.txt", "w") as outputFile:
    print >> outputFile, res_pvi
