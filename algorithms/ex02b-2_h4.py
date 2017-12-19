# -*- coding: utf-8 -*-
from odemethods import RungeKutta

def f(x, y):
    return -x/y

# Cálculo e exibição de resultados
res_pvi = RungeKutta(f, 4.0, 0, 20, 4)
res_pvi.calc()
with open("output/ex02b-2_h4.txt", "w") as outputFile:
    print >> outputFile, res_pvi
