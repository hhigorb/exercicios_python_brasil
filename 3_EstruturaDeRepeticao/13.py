"""13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao
segundo número. Não utilize a função de potência da linguagem."""


base = int(input('Entre com a base: '))
expoente = int(input('Entre com o expoente: '))
potencia = 1

for contador in range(expoente):
    potencia *= base

print(potencia)