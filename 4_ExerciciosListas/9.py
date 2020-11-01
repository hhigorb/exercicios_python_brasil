"""9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
elementos do vetor."""

lista = []
soma_dos_quadrados = 0

for i in range(1, 11):
    n = int(input(f'Digite o {i}º número: '))
    lista.append(n)
    soma_dos_quadrados += n ** 2


for valor in lista:
    print(f'{valor} ^ 2 = {valor ** 2}')
print(f'A soma dos quadrados é de: {soma_dos_quadrados}')