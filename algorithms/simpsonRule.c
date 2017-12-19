#include <math.h>
#include <stdio.h>

/**
 * Definições de função, intervalo e pontos.
 */
#define   F(x)            exp(x*(-1))*cos(x)
#define   POINTS          15
#define   H               0.112199737629
#define   BEGIN           0

#define   PRINT(result)   printf("%.10f\n", result);

/**
 * Configura os valores da função nos pontos em um vetor.
 */
void setValues(double begin, double increment,double values[POINTS]);
/**
 * Integra a função F(x) na regra 1/3 de Simpson.
 */
double integrate(double h, double values[POINTS]);

/**
 * Função principal, calcula e exibe o resultado da integral.
 */
int main() {
  double values[POINTS];
  setValues(BEGIN, H, values);
  PRINT(integrate(H, values));
  return 0;
}

void setValues(double begin, double increment, double values[POINTS]) {
  int i;
  double x = begin;
  for (i = 0; i < POINTS; i++) {
    values[i] = F(x);
    x += increment;
  }
}

double integrate(double h, double values[POINTS]) {
  double sum = 0;
  sum += values[0] + values[POINTS - 1];
  int i;
  for (i = 1; i < POINTS - 1; i++) {
    if (i & 1) {
      sum += 4 * values[i];
    } else {
      sum += 2 * values[i];
    }
  }
  return (sum*h) / 3;
}
