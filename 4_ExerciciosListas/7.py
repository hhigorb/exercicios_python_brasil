"""7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""

lista = []
soma = 0
multiplicacao = 1

for i in range(1, 6):
    n = int(input(f'Digite o {i}º número: '))
    lista.append(n)
    soma += n
    multiplicacao *= n

print(f'Lista: {lista}\n'
      f'Multiplicação da lista: {multiplicacao}\n'
      f'Soma da lista: {soma}')
