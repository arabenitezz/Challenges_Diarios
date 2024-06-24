// Escribir un programa que pida al usuario dos números y los sume.

#include <iostream>

using namespace std;

int main() {
  // Declaración de variables
  float num1, num2, resultado;

  // Solicitud de números al usuario
  cout << "Ingrese el primer numero: ";
  cin >> num1;

  cout << "Ingrese el segundo numero: ";
  cin >> num2;

  // Cálculo de la suma
  resultado = num1 + num2;

  // Mostrar el resultado de la suma
  cout << "La suma de los dos numeros es: " << resultado << endl;

  return 0;
}