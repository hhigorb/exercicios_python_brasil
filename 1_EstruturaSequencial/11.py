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