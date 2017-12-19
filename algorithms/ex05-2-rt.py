# -*- coding: utf-8 -*-
from odemethods import RungeKutta

def f(x, y):
    return (2 + (x**2)*y)/x

# Cálculo de resultados
res_pvi = RungeKutta(f, 0.1, 1, 3, 5)
res_pvi.calc()
with open("output/ex05-2-rt.txt", "w") as outputFile:
    print >> outputFile, res_pvi
