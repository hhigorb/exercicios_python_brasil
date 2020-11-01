"""8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida."""

alturas = []
idades = []

try:
    for _ in range(5):
        idade = int(input('Digite sua idade: '))
        idades.append(idade)
        altura = float(input('Digite sua altura [EM METROS]: '))
        alturas.append(altura)
except ValueError:
    print(f'Favor, digitar somente sua idade e altura em metros.')


print(f'Alturas invertida: {alturas[::-1]}\n'
      f'Idades invertida: {idades[::-1]}')