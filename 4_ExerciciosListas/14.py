"""14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3
e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""


perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?",
             "Já trabalhou com a vítima?"]

respostas = []

print('Responda as perguntas com "sim" OU "nao"!')
for i in perguntas:
    resposta = input(f'{i} ').lower()
    print(resposta)
    if resposta == 'sim':
        respostas.append(resposta)

if len(respostas) == 2:
    print('Suspeita')
elif 3 <= len(respostas) <= 4:
    print('Cúmplice')
elif len(respostas) == 5:
    print('Assassino')
else:
    print('Inocente')