"""6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0."""

medias = []
aprovados = 0

for _ in range(10):
    n1 = int(input('Digite a 1ª nota: '))
    n2 = int(input('Digite a 2ª nota: '))
    n3 = int(input('Digite a 3ª nota: '))
    n4 = int(input('Digite a 4ª nota: '))
    media = (n1 + n2 + n3 + n4) / 4
    medias.append(media)

for media in medias:
    if media >= 7:
        aprovados += 1
print(f'O número de alunos aprovados é de: {aprovados}')