# -*- coding: utf-8 -*-

from integrmethods import Simpson
from math import exp
from math import cos

def f(x):
    """
    Descrição:
        Definição da função a ser integrada.
    """
    return exp(-x)*cos(x)

# Cálculo e exibição de resultados
fun_int_tr = Simpson(f, 0, 0.112199737629, 15)
print(fun_int_tr.integr())
