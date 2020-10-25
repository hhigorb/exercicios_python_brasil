"""17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5! = 5.4.3.2.1=120"""

numero = int(input('Digite n! '))
fatorial = 1

for valor in range(numero, 0, -1):
    fatorial *= valor

print(fatorial)