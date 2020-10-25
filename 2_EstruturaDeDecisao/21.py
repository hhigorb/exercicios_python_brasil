"""
21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de
notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota
de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro
notas de 10, uma nota de 5 e quatro notas de 1.
"""

saque = int(input('Digite o valor do saque: '))

if 10 <= saque <= 600:
    notas_100 = int(saque / 100)
    saque = saque % 100

    notas_50 = int(saque / 50)
    saque = saque % 50

    notas_10 = int(saque / 10)
    saque = saque % 10

    notas_5 = int(saque / 5)
    saque = saque % 5

    notas_1 = saque

    print(f'Notas de R$ 100,00: {notas_100}\n'
          f'Notas de R$ 50,00: {notas_50}\n'
          f'Notas de R$ 10,00: {notas_10}\n'
          f'Notas de R$ 5,00: {notas_5}\n'
          f'Notas de R$ 1,00: {notas_1}')
else:
    print('O valor mínimo para saque é de 10 reais. O máximo de 600 reais.')