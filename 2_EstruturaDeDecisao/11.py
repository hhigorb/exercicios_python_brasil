"""
11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

salario = float(input('Qual o seu salário? '))

if salario < 280:
    novo_salario = salario + salario * 0.20
    print(f'Seu antigo salário era: {salario}\n'
          f'O aumento salarial foi de 20%: {salario * 0.20}\n'
          f'Seu novo salário é: {novo_salario}')

elif 280 <= salario < 700:
    novo_salario = salario + salario * 0.15
    print(f'Seu antigo salário era: {salario}\n'
          f'O aumento salarial foi de 15%: {salario * 0.15}\n'
          f'Seu novo salário é: {novo_salario}')

elif 700 <= salario < 1500:
    novo_salario = salario + salario * 0.10
    print(f'Seu antigo salário era: {salario}\n'
          f'O aumento salarial foi de 10%: {salario * 0.10}\n'
          f'Seu novo salário é: {novo_salario}')

else:
    novo_salario = salario + salario * 0.05
    print(f'Seu antigo salário era: {salario}\n'
          f'O aumento salarial foi de 5%: {salario * 0.05}\n'
          f'Seu novo salário é: {novo_salario}')