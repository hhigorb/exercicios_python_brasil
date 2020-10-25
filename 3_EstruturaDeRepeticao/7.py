"""7. Faça um programa que leia 5 números e informe o maior número."""

maior = 0

for _ in range(5):
    numero = int(input('Digite um número: '))
    if numero > maior:
        maior = numero

print(f'O maior número é: {maior}')