"""
EstruturaSequencial
"""

"""1. Faça um Programa que mostre a mensagem "Alo mundo" na tela."""

print('Hello, World!')

"""2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]."""

numero = int(input('Digite um número: '))
print(f'O número digitado foi: {numero}')

"""3. Faça um Programa que peça dois números e imprima a soma."""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número : '))
print(f'A soma é: {n1 + n2}')

"""4. Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

try:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    n4 = float(input('Digite a quarta nota: '))
    media = (n1 + n2 + n3 + n4) / 4
    print(media)
except (ValueError, NameError):
    print('Por favor, digite um valor inteiro ou real')

"""5. Faça um Programa que converta metros para centímetros."""

try:
    m = float(input('Digite uma quantidade em metros: '))
    print(f'{m} metros em cm são: {m * 100}')
except ValueError:
    print('Por favor, digite um valor inteiro ou real!')


"""6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""

from math import pi

raio = float(input('Digite a o raio do círculo: '))
print(f'A área do círculo é de: {pi * raio ** 2:.2f}')

"""7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário."""

lado = float(input('Digite o valor do lado do quadrado: '))
area_quadrado = lado ** 2
print(f'A área do quadrado é de {area_quadrado} e seu dobro é {area_quadrado * 2}')

"""8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês."""

try:
    ganho_por_hora = float(input('Quanto você ganha por hora? '))  # 10
    horas_mensais = float(input('Quanto você ganha por hora? '))  # 168 horas
    print(f'Seu salário mensal é de {ganho_por_hora * horas_mensais}')
except ValueError:
    print('Por favor, entre com valores inteiros ou reais!')

"""9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""

try:
    fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
    celsius = 5 * ((fahrenheit-32) / 9)
    print(f'{fahrenheit} graus Fahrenheit correspodem a {celsius:.2f} graus celsius!')
except ValueError:
    print('Por favor, digite somente valores inteiros ou reais!')

"""10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

try:
    celsius = float(input('Digite a temperatura em graus Celsius: '))
    fahrenheit = celsius * 1.8 + 32
    print(f'{celsius} graus celsius correspodem a {fahrenheit:.2f} graus Fahrenheit!')
except ValueError:
    print('Por favor, digite somente valores inteiros ou reais!')

"""11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo.
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

try:
    int1 = int(input('Digite um valor inteiro: '))
    int2 = int(input('Digite mais um valor inteiro: '))
    float2 = float(input('Digite um valor real: '))
    print(f'O produto do dobro do primeiro com metade do segundo: {(int1 * 2) * (int2 / 2)}\n'
          f'A soma do triplo do primeiro com o terceiro: {int1 * 3 + float2}\n'
          f'O terceiro elevado ao cubo: {float2 ** 3}')
except ValueError:
    print('Por favor, entre somente com valores inteiros e reais!')

"""12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58"""

altura = float(input('Digite sua altura: '))
peso_ideal = (72.7 * altura) - 58
print(f'Seu peso ideal é: {peso_ideal:.2f}')

"""13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

try:
    altura = float(input('Digite sua altura: '))
    h_ou_m = input('Selecione [H] para homem ou [M] para mulher: ').upper()

    if 'H' in h_ou_m:
        print(f'O peso ideal para um homem da sua altura é de: {(72.7 * altura) - 58:.2f}')
    elif 'M' in h_ou_m:
        print(f'O peso ideal para uma mulher da sua altura é de: {(62.1 * altura) - 44.7:.2f}')
    else:
        print("Você deve digitar 'H' ou 'M'!")
except ValueError:
    print('A altura deve ser um número inteiro ou real!')

"""14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado
de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um
programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade
de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa
com as mensagens adequadas."""

peso = float(input('Digite o peso total dos peixes em KG: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'Você excedeu os 50kg de peixe! Limite excedido: {excesso}, multa a pagar: {multa}')
else:
    print(f'Peso total de: {peso}. O limite não foi excedido.')


"""15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e
mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.
- calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""

ganho_por_hora = float(input('Quanto você ganha por hora? '))
horas_mensais = int(input('Quantas horas mensais você trabalhou? '))

salario_bruto = ganho_por_hora * horas_mensais
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print(f'Seu salário neste mês com os devidos descontos será de: R${salario_liquido}')

"""16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
e o preço total."""

area_a_pintar = float(input('Digite o tamanho da área a ser pintada em m²: '))
litros_necessarios = area_a_pintar / 3
latas_necessarias = litros_necessarios / 18
preco = latas_necessarias * 80

print(f'Você deverá comprar {latas_necessarias:.2f} latas de tinta e o preço final será de: R${preco:.2f}')


"""17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
os valores para cima, isto é, considere latas cheias."""

area_a_pintar = float(input('Digite o tamanho da área a ser pintada em m²: '))  # digitei 30
preco_lata = area_a_pintar / 6 / 18 * 80
preco_galao = area_a_pintar / 6 / 3.6 * 25

print(f'Ao comprar apenas latas de 18L você gastará: R${preco_lata:.2f}')
print(f'Ao comprar apenas galões de 3.6L você gastará: R${preco_galao:.2f}')

"""18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tamanho_arquivo = float(input('Tamanho do arquivo a ser baixado em MB/s: '))
velocidade_internet = float(input('Qual a velocidade da sua internet? '))
tempo_de_download = tamanho_arquivo / velocidade_internet / 60

print(f'Seu arquivo demorará {tempo_de_download:.2f} minutos para ser baixado!')





























