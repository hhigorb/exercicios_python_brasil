"""10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
compreendido por eles."""

n1 = int(input('Digite o número inicial: '))
n2 = int(input('Digite o número final: '))

for valor in range(n1+1, n2):
    print(valor)