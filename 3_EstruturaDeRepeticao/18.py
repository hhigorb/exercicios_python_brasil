"""18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos
valores."""

quantidade = int(input('Quantos valores você deseja digitar? '))
menor = 1
maior = 0
soma = 0

for valor in range(quantidade):
    numero = int(input('Digite um número: '))
    if numero > maior:
        maior = numero
    else:
        menor = numero
    soma += numero

print(f'O menor número é: {menor}, o maior é: {maior} e a soma de todos os valores é de: {soma}')