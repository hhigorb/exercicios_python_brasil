"""13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

try:
    altura = float(input('Digite sua altura: '))
    h_ou_m = input('Selecione [H] para homem ou [M] para mulher: ').upper()

    if 'H' in h_ou_m:
        print(f'O peso ideal para um homem da sua altura é de: {(72.7 * altura) - 58:.2f}')
    elif 'M' in h_ou_m:
        print(f'O peso ideal para uma mulher da sua altura é de: {(62.1 * altura) - 44.7:.2f}')
    else:
        print("Você deve digitar 'H' ou 'M'!")
except ValueError:
    print('A altura deve ser um número inteiro ou real!')