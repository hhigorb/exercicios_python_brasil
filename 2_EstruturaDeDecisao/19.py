"""
19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas
e unidades do mesmo.
"""

numero = int(input('Digite um número inteiro positivo: '))

unidade = numero % 10
numero = (numero - unidade) / 10
dezena = numero % 10
numero = (numero - dezena) / 10
centena = numero

print(f'Centena: {int(centena)}, dezena: {int(dezena)}, unidade: {unidade}')