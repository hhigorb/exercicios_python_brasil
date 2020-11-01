"""4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as
consoantes."""

vetor = []
vogais = 'aeiou'

for _ in range(10):
    letra = input('Digite uma letra: ')
    if letra not in vogais:
        vetor.append(letra)

print(f'Foram digitadas {len(vetor)} consoantes.')