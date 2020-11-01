"""3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela."""

notas = []

for _ in range(4):
    notas.append(int(float(input('Digite sua nota: '))))

media = sum(notas) / 4
print(f'A média é de: {media}')
