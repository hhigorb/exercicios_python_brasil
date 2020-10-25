"""
12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

valor_hora = int(input('Digite o valor da sua hora: '))
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas: '))
salario_bruto = valor_hora * horas_trabalhadas
inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11
ir = 0
total_descontos = 0
porcentagem = '0%'
desconto_percentual = 0

if salario_bruto <= 900:
    total_descontos = inss
    salario_liquido = salario_bruto - total_descontos

elif 901 <= salario_bruto <= 1500:
    total_descontos = inss + salario_bruto * 0.05
    porcentagem = '5%'
    desconto_percentual = salario_bruto * 0.05
    salario_liquido = salario_bruto - total_descontos

elif 1501 <= salario_bruto <= 2500:
    total_descontos = inss + salario_bruto * 0.10
    porcentagem = '10%'
    desconto_percentual = salario_bruto * 0.10
    salario_liquido = salario_bruto - total_descontos

else:
    total_descontos = inss + salario_bruto * 0.20
    porcentagem = '20%'
    desconto_percentual = salario_bruto * 0.20
    salario_liquido = salario_bruto - total_descontos

print('_=_=_=_' * 10)
print()
print(f'Salário Bruto: ({valor_hora} * {horas_trabalhadas})       : R$ {salario_bruto}\n'
      f'(-) IR ({porcentagem})                    : R$ {desconto_percentual}\n'
      f'(-) INSS (10%)                 : R$ {inss}\n'
      f'FGTS (11%)                     : R$ {fgts}\n'
      f'Total de descontos             : R$ {total_descontos}\n'
      f'Salário Liquido                : R$ {salario_liquido}')