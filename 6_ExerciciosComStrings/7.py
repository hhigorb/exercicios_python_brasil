"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.

"""

frase = input('Digite uma frase: ')

vogais = 0
espacos = 0

for letra in frase:
    if letra == ' ':
        espacos += 1
    if letra in 'aeiou':
        vogais += 1

print(f'Espaços em branco: {espacos}, vogais na frase: {vogais}')

