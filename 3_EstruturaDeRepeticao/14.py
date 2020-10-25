"""14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade
de números impares."""

impares = 0
pares = 0

for _ in range(1, 11):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Quantidade de pares: {pares}, quantidade de ímpares: {impares}')