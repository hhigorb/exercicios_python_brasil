"""6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""

from math import pi

raio = float(input('Digite a o raio do círculo: '))
print(f'A área do círculo é de: {pi * raio ** 2:.2f}')