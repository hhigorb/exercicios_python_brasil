"""5. Faça um Programa que converta metros para centímetros."""

try:
    m = float(input('Digite uma quantidade em metros: '))
    print(f'{m} metros em cm são: {m * 100}')
except ValueError:
    print('Por favor, digite um valor inteiro ou real!')