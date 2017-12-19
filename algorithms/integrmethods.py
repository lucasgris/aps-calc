# -*- coding: utf-8 -*-

class Trapezoidal(object):
    """
    Descrição:
        Classe que representa uma integração pela regra do Trapézio.

    Nota:
        O intervalo de integração é definido automaticamente, dados o início do intervalo a, o tamanho da subdivisão e a quantidade de pontos.

        Entre sempre com um valor do tipo float no início do intervalo de integração, caso contrário o resultado poderá ser truncado.

    Args:
        f:      função a ser integrada.
        a:      início do intervalo de integração.
        h:      tamanho da subdivisão do intervalo.
        points: quantidade de pontos utilizados.
    """
    def __init__(self, f, a, h, points):
        self._f = f
        self._a = a
        self._h = h
        self._itr = points - 1

    def integr_partial(self, a):
        """
        Calcula a integral no intervalo de [a, a + h], onde h é o tamanho da subdivisão do intervalo.
        Não utilize esse método, use o método integr(). Esse método não calcula o resultado da integral para todos os pontos.

        Retorna:
            O resultado da integração.
        """
        return (self._h / 2) * (self._f(a) + self._f((a + self._h)))

    def integr(self):
        """
        Implementação da regra generalizada do Trapézio. Efetua o cálculo da integral.

        Retorna:
            O resultado da integração.
        """
        self._sum = 0
        xa = self._a;
        for i in range(0, self._itr):
            self._sum = self._sum + self.integr_partial(xa)
            xa = xa + self._h
        return self._sum

class Simpson(object):
    """
    Descrição:
        Classe que representa uma integração pela regra 1/3 de Simpson.

    Nota:
        O intervalo de integração é definido automaticamente, dados o início do intervalo a, o tamanho da subdivisão e a quantidade de pontos.

        Entre sempre com um valor do tipo float no início do intervalo de integração, caso contrário o resultado poderá ser truncado.

    Args:
        f:      função a ser integrada.
        a:      início do intervalo de integração.
        h:      tamanho da subdivisão do intervalo.
        points: quantidade de pontos utilizados.
    """
    def __init__(self, f, a, h, points):
        self._f = f
        self._a = a
        self._h = h
        self._points = points
        self._values = list()
        for i in range(0, self._points):
            self._values.append(f(self._a + (i * h)))

    def integr(self):
        """
        Integra a função.

        Retorna:
            O resultado da integração.
        """
        sum = 0.0
        sum += self._values[0] + self._values[self._points - 1]
        for i in range(1, self._points - 1):
            if (i % 2 == 0):
                sum += 2 * self._values[i]
            else:
                sum += 4 * self._values[i]
        return (sum * self._h) / 3

class Simpson2(object):
    """
    Descrição:
        Classe que representa uma integração pela regra 3/8 de Simpson.

    Nota:
        O intervalo de integração é definido automaticamente, dados o início do intervalo a, o tamanho da subdivisão e a quantidade de pontos.

        Entre sempre com um valor do tipo float no início do intervalo de integração, caso contrário o resultado poderá ser truncado.

    Args:
        f:      função a ser integrada.
        a:      início do intervalo de integração.
        h:      tamanho da subdivisão do intervalo.
        points: quantidade de pontos utilizados.
    """
    def __init__(self, f, a, h, points):
        self._f = f
        self._a = a
        self._h = h
        self._points = points
        self._values = list()
        for i in range(0, self._points):
            self._values.append(f(self._a + (i * h)))

    def integr(self):
        """
        Integra a função.

        Retorna:
            O resultado da integração.
        """
        sum = 0.0
        sum += self._values[0] + self._values[self._points - 1]
        for i in range(1, self._points - 1):
            if (i % 3 == 0):
                sum += 2 * self._values[i]
            else:
                sum += 3 * self._values[i]
        return (sum * self._h * 3) / 8
