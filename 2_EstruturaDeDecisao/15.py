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