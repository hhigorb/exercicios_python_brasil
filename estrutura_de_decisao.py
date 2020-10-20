"""
EstruturaDeDecisao
"""

"""
1. Faça um Programa que peça dois números e imprima o maior deles.
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'{n2} é maior que {n1}')
else:
    print('Os números são iguais!')

"""
2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

numero = int(input('Digite um número: '))

if numero < 0:
    print('O número é negativo!')
else:
    print('O número é positivo!')

"""
3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
M - Masculino, Sexo Inválido.
"""

sexo = input('Digite [F] para feminino ou [M] para masculino: ').upper()

if sexo == 'F':
    print('Sexo selecionado: Feminino')
elif sexo == 'M':
    print('Sexo selecionado: Masculino')
else:
    print('Sexo inválido. Por favor, digite [F] ou [M]!')

"""
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

vogais = 'aeiou'
letra = str(input('Digite uma letra: ')).lower()
if letra.isalpha():
    if letra in vogais:
        print('É uma vogal!')
    else:
        print('É uma consoante!')
else:
    print('Você deve digitar uma letra!')

"""
5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média
alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media == 10:
    print('Aprovado com distinção.')
elif 7 <= media < 10:
    print('Aprovado!')
else:
    print('Reprovado!')

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


"""
7. Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

maior = n1
menor = n1

if maior < n2:
    maior = n2
if maior < n3:
    maior = n3
if menor > n2:
    menor = n2
if menor > n3:
    menor = n3

print(f'Maior número: {maior}\n'
      f'Menor número: {menor}')

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

"""
10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino
ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme
o caso.
"""

print('OPÇÕES:\n'
      'M-matutino\n'
      'V-Vespertino\n'
      'N-Noturno')
turno = input('Em que turno você estuda? ').upper()

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print("Inválido! Você deve digitar 'M', 'V' ou 'N'!")
    

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


"""
13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""

dia = int(input('Escolha um dia da semana (1 a 7): '))

if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda')
elif dia == 3:
    print('Terça')
elif dia == 4:
    print('Quarta')
elif dia == 5:
    print('Quinta')
elif dia == 6:
    print('Sexta')
elif dia == 7:
    print('Sábado')
else:
    print('Número inválido!')


"""
14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if 9 <= media <= 10:
    print(f'Aprovado! Você recebeu um conceito A!')

elif 7.5 <= media <= 9:
    print(f'Aprovado! Você recebeu um conceito B!')

elif 6 < media <= 7.5:
    print(f'Aprovado! Você recebeu um conceito C!')

elif 4 <= media <= 6:
    print(f'Reprovado! Você recebeu um conceito D!')

else:
    print(f'Reprovado! Você recebeu um conceito E!')

print(f'Nota 1: {n1}\n'
      f'Nota 2: {n2}\n'
      f'Média: {media}')
      

"""
15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

a = int(input('Digite o primeiro lado do triângulo: '))
b = int(input('Digite o segundo lado do triângulo: '))
c = int(input('Digite o terceiro lado do triângulo: '))


if (a + b < c) or (b + c < a) or (c + a < b):
    print('Não é possível formar um triângulo!')
elif a == b == c:
    print('O triângulo é equilátero!')
elif a == b or a == c or b == c:
    print('Triângulo isósceles!')
else:
    print('Triângulo escaleno!')


"""
16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário
"""

import math

a = int(input('Digite o valor de A: '))
if a == 0:
    print('A equação não é de segundo grau!')
    quit()
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
delta = b*b-4*a*c

if delta < 0:
    print('A equação não tem raízes reais!')
elif delta == 0:
    print(f'A equação tem apenas uma raíz: {-b/2*a}')
else:
    print(f'A equação tem duas raízes\n'
          f'Raiz 1: {(-b-math.sqrt(delta))/2*a}\n'
          f'Raiz 1: {(-b+math.sqrt(delta))/2*a}')


"""
17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se
este ano é ou não bissexto.
"""

ano = int(input('Escolha um ano: '))
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')


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


"""
19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas
e unidades do mesmo.
"""

numero = int(input('Digite um número inteiro positivo: '))

unidade = numero % 10
numero = (numero - unidade) / 10
dezena = numero % 10
numero = (numero - dezena) / 10
centena = numero

print(f'Centena: {int(centena)}, dezena: {int(dezena)}, unidade: {unidade}')

"""
20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada
por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3

if media == 10:
    print('Aprovado com distinção')
elif media >= 7:
    print(f'Aprovado com a média: {media}')
elif media < 7:
    print(f'Reprovado com a média: {media}')


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


"""
22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).
"""


n = int(input('Entre com um número inteiro: '))

if n % 2 == 0:
    print('Par')
else:
    print('Impar')


"""
23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma
função de arredondamento.
"""

n = float(input('Digite um número: '))
if n == round(n):
    print('É um número inteiro!')
else:
    print('É um decimal!')
    

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
    

"""
25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no
crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

print("RESPONDA AS PERGUNTAS COM 'SIM' OU 'NÃO'!")
p1 = input('Telefonou para a vítima? ').lower()
p2 = input('Esteve no local do crime? ').lower()
p3 = input('Mora perto da vítima? ').lower()
p4 = input('Devia para a vítima? ').lower()
p5 = input('Já trabalhou com a vítima? ').lower()

somatoria = 0

if p1 == 'sim':
    somatoria = somatoria + 1
if p2 == 'sim':
    somatoria = somatoria + 1
if p3 == 'sim':
    somatoria = somatoria + 1
if p4 == 'sim':
    somatoria = somatoria + 1
if p5 == 'sim':
    somatoria = somatoria + 1

if somatoria == 2:
    print('Classificação: Suspeita!')
elif 3 <= somatoria <=4:
    print('Classificação: Cúmplice!')
elif somatoria == 5:
    print('Classificação: Assassino!')
else:
    print('Classificação: Inocente!')


"""
26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser
pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""


litros = int(input('Digite a quantidade de litros de combustível: '))
tipo = input('Tipo de combustível: A-álcool, G-gasolina ').lower()
preco_alcool = 1.90 * litros
preco_gasolina = 2.50 * litros

if tipo == 'a':
    if litros <= 20:
        desconto_3_por_litro = 1.90 * 0.03 * litros
        preco_com_desconto = preco_alcool - desconto_3_por_litro
        print(f'Total: R$ {preco_alcool}, porém foi aplicado 3% de desconto por litro. Então: R${preco_com_desconto}')
    else:
        desconto_5_por_litro = 1.90 * 0.05 * litros
        preco_com_desconto = preco_alcool - desconto_5_por_litro
        print(f'Total: R$ {preco_alcool}, porém foi aplicado 5% de desconto por litro. Então: R${preco_com_desconto}')

elif tipo == 'g':
    if litros <= 20:
        desconto_4_por_litro = 2.50 * 0.04 * litros
        preco_com_desconto = preco_gasolina - desconto_4_por_litro
        print(f'Total: R$ {preco_gasolina}, porém foi aplicado 3% de desconto por litro. Então: R${preco_com_desconto}')
    else:
        desconto_6_por_litro = 2.50 * 0.06 * litros
        preco_com_desconto = preco_gasolina - desconto_6_por_litro
        print(f'Total: R$ {preco_gasolina}, porém foi aplicado 3% de desconto por litro. Então: R${preco_com_desconto}')
        

"""
27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

peso_morangos = int(input('Quantidade de morangos em KG: '))
peso_macas = int(input('Quantidade de maças em KG: '))
peso_total = peso_morangos + peso_macas
preco_morango = 0
preco_maca = 0

if peso_morangos <= 5:
    preco_morango = 2.5
else:
    preco_morango = 2.2

if peso_macas <= 5:
    preco_maca = 1.8
else:
    preco_maca = 1.5

total_morango = peso_morangos * preco_morango
total_maca = peso_macas * preco_maca
valor_total = total_morango + total_maca

if peso_total > 8 or valor_total > 25:
    valor_total = valor_total - (valor_total * 0.10)
    print(f'Morangos: {peso_morangos}KG, maças: {peso_macas}KG\n'
          f'Peso total: {peso_total}KG (desconto de 10% aplicado), preço final: R$ {valor_total:.2f}')
else:
    valor_total = total_morango + total_maca
    print(f'Morangos: {peso_morangos}KG, maças: {peso_macas}KG\n'
          f'Peso total: {peso_total}KG, preço final: R$ {valor_total:.2f}')


