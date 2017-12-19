# -*- coding: utf-8 -*-

from math import factorial

class Euler(object):
    """
    Descrição:
        Classe que representa uma resolução de um P.V.I. atravéz do método de Euler melhorado.

    Args:
        f:      função em termos de x e y da equação diferencial
        step:   passo entre os cálculos das soluções
        x0:     valor inicial do P.V.I.
        y0:     resultado inicial do P.V.I.
        points: quantidade de pontos
    """
    def __init__(self, f, step, x0, y0, points):
        self._f = f
        self._step = step
        self._y0 = y0
        self._x0 = x0
        self._res = dict()
        self._res[x0] = y0
        self._points = points

    def calc(self):
        """
        Descrição
            Resolve o P.V.I.

        Nota:
            O cálculo é realizado a partir do valor inicial (x0, y0) , seguido pelos passos e a quantidade de pontos.
        """
        xi = self._x0
        yi = self._y0
        for n in range(0, self._points):
            k1 = self._f(xi, yi)
            k2 = self._f(xi + self._step, yi + (self._step*k1))
            yn = yi + (self._step / 2)*(k1 + k2)
            self._res[xi + self._step] = yn
            xi += self._step
            yi = yn

    def __str__(self):
        """
        Descrição:
            Representação do objeto, retorna uma string contendo os dados do objeto e a solução do P.V.I.

        Nota:
            Se o método calc() não for chamado, apenas o valor inicial será retornado como resultado.
        """
        str = "Resolução de P.V.I pelo método de Euler melhorado"
        str += "\nValor inicial: y({}) = {}".format(self._x0, self._y0)
        str += "\nTamanho do passo: {}".format(self._step)
        str += "\nResolução:"
        for x in sorted(self._res.iterkeys()):
            str += "\ny({}) = {}".format(x, self._res[x])
        return str

class RungeKutta(object):
    """
    Descrição:
        Classe que representa uma resolução de um P.V.I. atravéz do método de Runge Kutta de quarta ordem.

    Args:
        f:      função em termos de x e y da equação diferencial
        step:   passo entre os cálculos das soluções
        x0:     valor inicial do P.V.I.
        y0:     resultado inicial do P.V.I.
        points: quantidade de pontos
    """
    def __init__(self, f, step, x0, y0, points):
        self._f = f
        self._step = step
        self._y0 = y0
        self._x0 = x0
        self._res = dict()
        self._res[x0] = y0
        self._points = points

    def calc(self):
        """
        Descrição
            Resolve o P.V.I.

        Nota:
            O cálculo é realizado a partir do valor inicial (x0, y0) , seguido pelos passos e a quantidade de pontos.
        """
        xi = self._x0
        yi = self._y0
        for n in range(0, self._points):
            k1 = self._f(xi, yi)
            k2 = self._f(xi + (self._step / 2), yi + ((self._step*k1)/2))
            k3 = self._f(xi + (self._step / 2), yi + ((self._step*k2)/2))
            k4 = self._f(xi + self._step, yi + (self._step*k3))
            yn = yi + (self._step / 6)*(k1 + 2*(k2 + k3) + k4)
            self._res[xi + self._step] = yn
            xi += self._step
            yi = yn

    def __str__(self):
        """
        Descrição:
            Representação do objeto, retorna uma string contendo os dados do objeto e a solução do P.V.I.

        Nota:
            Se o método calc() não for chamado, apenas o valor inicial será retornado como resultado.
        """
        str = "Resolução de P.V.I pelo método de Runge Kutta de quarta ordem"
        str += "\nValor inicial: y({}) = {}".format(self._x0, self._y0)
        str += "\nTamanho do passo: {}".format(self._step)
        str += "\nResolução:"
        for x in sorted(self._res.iterkeys()):
            str += "\ny({}) = {}".format(x, self._res[x])
        return str

class Taylor(object):
    """
    Descrição:
        Classe que representa uma resolução de um P.V.I. atravéz do método de Taylor.

    Args:
        functions:  uma lista contendo a função e suas derivadas até a ordem n
        step:       passo entre os cálculos das soluções
        x0:         valor inicial do P.V.I.
        y0:         resultado inicial do P.V.I.
        points:     quantidade de pontos

    Nota:
        Entre com uma lista contendo a função e suas derivadas para a aplicação do método.
        No caso de uma aplicação do método de segunda ordem por exemplo, teríamos, em functions, as referencias para as funções [f, f', f'']
    """
    def __init__(self, functions, step, x0, y0, points):
        self._functions = functions
        self._step = step
        self._y0 = y0
        self._x0 = x0
        self._res = dict()
        self._res[x0] = y0
        self._points = points

    def calc(self):
        """
        Descrição
            Resolve o P.V.I.

        Nota:
            O cálculo é realizado a partir do valor inicial (x0, y0) , seguido pelos passos e a quantidade de pontos.
        """
        xi = self._x0
        for n in range(0, self._points):
            yn = self._res[xi]
            for i in range(0, len(self._functions)):
                yn += (self._step**((i + 1))/factorial((i + 1)) * self._functions[i](xi, self._res[xi]))
            xi += self._step
            self._res[xi] = yn

    def __str__(self):
        """
        Descrição:
            Representação do objeto, retorna uma string contendo os dados do objeto e a solução do P.V.I.

        Nota:
            Se o método calc() não for chamado, apenas o valor inicial será retornado como resultado.
        """
        str = "Resolução de P.V.I pelo método de Taylor de ordem {}".format(len(self._functions))
        str += "\nValor inicial: y({}) = {}".format(self._x0, self._y0)
        str += "\nTamanho do passo: {}".format(self._step)
        str += "\nResolução:"
        for x in sorted(self._res.iterkeys()):
            str += "\ny({}) = {}".format(x, self._res[x])
        return str
