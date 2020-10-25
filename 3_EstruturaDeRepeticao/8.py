"""8. Faça um programa que leia 5 números e informe a soma e a média dos números."""

soma = 0

for _ in range(5):
    numero = int(input('Digite um número: '))
    soma += numero

print(f'A soma é: {soma} e a média é: {soma / 5}')