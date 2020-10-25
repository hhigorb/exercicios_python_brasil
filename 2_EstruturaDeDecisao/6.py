"""
6. Faça um Programa que leia três números e mostre o maior deles.
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

maior = n1

if n1 == n2 == n3:
    print('Os 3 números são iguais.')
elif maior:
    print(f'{maior} é o maior número!')
elif n2 > maior:
    maior = n2
    print(f'{maior} é o maior número!')
elif n3 > maior:
    print(f'{maior} é o maior número!')