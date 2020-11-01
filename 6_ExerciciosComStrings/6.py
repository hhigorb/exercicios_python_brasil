"""
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data
com o nome do mês por extenso.
"""

data = input('Digite sua data de nascimento (dd/mm/aaaa): ')
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']

dia = int(data[0:2])
mes = meses[int(data[3:5]) - 1]
ano = int(data[6:])


print(f'Você nasceu em {dia} de {mes} de {ano}')

