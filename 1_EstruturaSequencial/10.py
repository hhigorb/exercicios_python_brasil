"""10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

try:
    celsius = float(input('Digite a temperatura em graus Celsius: '))
    fahrenheit = celsius * 1.8 + 32
    print(f'{celsius} graus celsius correspodem a {fahrenheit:.2f} graus Fahrenheit!')
except ValueError:
    print('Por favor, digite somente valores inteiros ou reais!')