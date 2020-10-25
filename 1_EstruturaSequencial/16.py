"""16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
e o preço total."""

area_a_pintar = float(input('Digite o tamanho da área a ser pintada em m²: '))
litros_necessarios = area_a_pintar / 3
latas_necessarias = litros_necessarios / 18
preco = latas_necessarias * 80

print(f'Você deverá comprar {latas_necessarias:.2f} latas de tinta e o preço final será de: R${preco:.2f}')