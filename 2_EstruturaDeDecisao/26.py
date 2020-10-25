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