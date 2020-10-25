"""
8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""

produto1 = float(input('Digite o preço do primeiro produto: '))
produto2 = float(input('Digite o preço do segundo produto: '))
produto3 = float(input('Digite o preço do terceiro produto: '))

mais_barato = produto1

if produto2 < mais_barato:
    mais_barato = produto2
if produto3 < mais_barato:
    mais_barato = produto3

print(f'O produto mais barato custa: R${mais_barato}')