"""9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

try:
    fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
    celsius = 5 * ((fahrenheit-32) / 9)
    print(f'{fahrenheit} graus Fahrenheit correspodem a {celsius:.2f} graus celsius!')
except ValueError:
    print('Por favor, digite somente valores inteiros ou reais!')