"""
25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no
crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

print("RESPONDA AS PERGUNTAS COM 'SIM' OU 'NÃO'!")
p1 = input('Telefonou para a vítima? ').lower()
p2 = input('Esteve no local do crime? ').lower()
p3 = input('Mora perto da vítima? ').lower()
p4 = input('Devia para a vítima? ').lower()
p5 = input('Já trabalhou com a vítima? ').lower()

somatoria = 0

if p1 == 'sim':
    somatoria = somatoria + 1
if p2 == 'sim':
    somatoria = somatoria + 1
if p3 == 'sim':
    somatoria = somatoria + 1
if p4 == 'sim':
    somatoria = somatoria + 1
if p5 == 'sim':
    somatoria = somatoria + 1

if somatoria == 2:
    print('Classificação: Suspeita!')
elif 3 <= somatoria <= 4:
    print('Classificação: Cúmplice!')
elif somatoria == 5:
    print('Classificação: Assassino!')
else:
    print('Classificação: Inocente!')