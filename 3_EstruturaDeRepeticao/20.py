"""20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando
o fatorial a números inteiros positivos e menores que 16."""

resposta = ''

while resposta != 'nao':
    numero = int(input('Digite n! '))
    if numero > 16:
        print('Somente permitidos números menores que 16')
        continue
    fatorial = 1

    for valor in range(numero, 0, -1):
        fatorial *= valor

    print(fatorial)
    resposta = input('Gostaria de continuar calculando? [SIM] ou [NAO] ')

print('Programa finalizado...')