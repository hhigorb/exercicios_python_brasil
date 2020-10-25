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