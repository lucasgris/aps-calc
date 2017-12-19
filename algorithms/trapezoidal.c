#include <stdio.h>
#include <math.h>

/**
 * Definições de função, intervalo e pontos.
 */
#define   F(x)            exp((x*x)*(-1))
#define   POINTS          352
#define   H               0.002849002849
#define   BEGIN           0

#define   PRINT(result)   printf("%.10f\n", result);

/**
 * Calcula a integral pela regra do Trapézio, em um intervalo [a, a+h], onde h é o tamanho da subdivisão do intervalo.
 */
double integrate(double h, double *a);
/**
 * Calcula a integral de todo o intervalo [a, b], formado pelas subdivisões igualmente espaçadas h.
 */
double integrateAll(int subdivisions, double h, double a);

/**
 * Função principal do programa, calcula a integral de F(x).
 */
int main() {
  PRINT(integrateAll(POINTS - 1, H, BEGIN));
  return 0;
}

double integrate(double h, double *a) {
  return (h / 2) * (F(*a) + F((*a + h)));
}

double integrateAll(int subdivisions, double h, double begin) {
  int i;
  double result = 0;
  double a = begin;
  for (i = 1; i < subdivisions; i++) {
    result += integrate(h, &a);
    a += h;
  }
  return result;
}
