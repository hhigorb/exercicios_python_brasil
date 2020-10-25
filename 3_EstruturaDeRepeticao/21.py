"""21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é
aquele que é divisível somente por ele mesmo e por 1."""

n = int(input('Digite um número inteiro: '))
multiplicador = 0

for contador in range(2, n):
    if n % contador == 0:
        print(f'Múltiplo de: {contador}')
        multiplicador += 1

if multiplicador == 0:
    print('É primo!')
else:
    print('Não é primo!')