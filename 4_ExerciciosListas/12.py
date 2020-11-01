"""12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de
13 anos possuem altura inferior à média de altura desses alunos."""

idades = []
alturas = []

for i in range(1, 31):
    idade = int(input(f'Digite a idade do {i}º aluno: '))
    altura = int(input(f'Digite a altura do {i}º aluno [EM CM]: '))
    idades.append(idade)
    alturas.append(altura)


media = sum(alturas) / 30
contador = 0

for i in range(30):
    if idades[i] > 13 and alturas[i] < media:
        contador += 1

print(f'Alunos com mais de 13 anos abaixo da média de altura: {contador}')