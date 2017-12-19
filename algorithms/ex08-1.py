# -*- coding: utf-8 -*-

from integrmethods import Trapezoidal
from math import exp

def f(x):
    """
    Descrição:
        Definição da função a ser integrada.
    """
    return exp(-(x**2))

# Cálculo e exibição de resultados
fun_int_tr = Trapezoidal(f, 1, 0.3333333, 4)
print(fun_int_tr.integr())
