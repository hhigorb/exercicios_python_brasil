"""
24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
operacao = input('Qual operação você deseja: (+  -  /  * ) ')

if operacao == '+':
    soma = n1 + n2
    if soma % 2 == 0:
        print('É um número par!')
    else:
        print('É um número ímpar!')
    if soma < 0:
        print('O número é negativo!')
    else:
        print('O número é positivo!')
    if soma == round(soma):
        print('É um número inteiro!')
    else:
        print('É um número decimal!')

elif operacao == '-':
    subtracao = n1 - n2
    if subtracao % 2 == 0:
        print('É um número par!')
    else:
        print('É um número ímpar!')
    if subtracao < 0:
        print('O número é negativo!')
    else:
        print('O número é positivo!')
    if subtracao == round(subtracao):
        print('É um número inteiro!')
    else:
        print('É um número decimal!')

elif operacao == '*':
    multiplicacao = n1 * n2
    if multiplicacao % 2 == 0:
        print('É um número par!')
    else:
        print('É um número ímpar!')
    if multiplicacao < 0:
        print('O número é negativo!')
    else:
        print('O número é positivo!')
    if multiplicacao == round(multiplicacao):
        print('É um número inteiro!')
    else:
        print('É um número decimal!')

elif operacao == '/':
    divisao = n1 / n2
    if divisao % 2 == 0:
        print('É um número par!')
    else:
        print('É um número ímpar!')
    if divisao < 0:
        print('O número é negativo!')
    else:
        print('O número é positivo!')
    if divisao == round(divisao):
        print('É um número inteiro!')
    else:
        print('É um número decimal!')

else:
    print('Operação inválida. Escolhe entre +  -  /  * ')