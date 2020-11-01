"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado
pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado
quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m

"""


while True:
    nome = input('Digite o nome do atleta: ')
    if nome == '':
        break
    saltos = []
    for i in range(1, 6):
        saltos.append(int(input(f'Digite o {i}º salto: ')))

    media = sum(saltos) / 5
    print(f'Resultado final:')
    print(f'Nome do atleta: {nome}')
    print(f'Saltos: {saltos[0], saltos[1], saltos[2], saltos[3], saltos[4]}')
    print(f'Média dos saltos: {media}')

