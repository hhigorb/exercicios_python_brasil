"""19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""

quantidade = int(input('Quantos valores você deseja digitar? '))
while quantidade > 1000:
    print('Permitido somente números entre 0 a 1000!')
    quantidade = int(input('Quantos valores você deseja digitar? '))
menor = 1
maior = 0
soma = 0

for valor in range(quantidade):
    numero = int(input('Digite um número: '))
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    soma += numero

print(f'O menor número é: {menor}, o maior é: {maior} e a soma de todos os valores é de: {soma}')