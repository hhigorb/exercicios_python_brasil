"""8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês."""

try:
    ganho_por_hora = float(input('Quanto você ganha por hora? '))  # 10
    horas_mensais = float(input('Quanto você ganha por hora? '))  # 168 horas
    print(f'Seu salário mensal é de {ganho_por_hora * horas_mensais}')
except ValueError:
    print('Por favor, entre com valores inteiros ou reais!')