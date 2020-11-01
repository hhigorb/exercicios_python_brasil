"""1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."""

lista_numeros = []

for _ in range(5):
    n = int(input('Digite um número: '))
    lista_numeros.append(n)

print(lista_numeros)