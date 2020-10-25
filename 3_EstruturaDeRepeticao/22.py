"""22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele
é divisível."""

n = int(input('Digite um número inteiro: '))
multiplicador = 0

for contador in range(2, n):
    if n % contador == 0:
        print(f'Divisível por: {contador}')
        multiplicador += 1

if multiplicador == 0:
    print('É primo!')
else:
    print('Não é primo!')