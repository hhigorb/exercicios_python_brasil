"""
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite outro número: '))

if n1 < n3:
    n1, n3 = n3, n1
if n1 < n2:
    n1, n2 = n2, n1
if n2 < n3:
    n2, n3 = n3, n2

print(f'A ordem decrescente é: {n1}, {n2} e {n3}')