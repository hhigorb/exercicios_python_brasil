"""
18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

print('Informe uma data no formato dd/mm/aaaa: ')
dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))

if dia > 31 or mes > 12:
    print('A data está incorreta!')

else:
    print(f'A data selecionada foi: {dia}/{mes}/{ano}')