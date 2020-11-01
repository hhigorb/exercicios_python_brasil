"""10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores."""

lista1 = []
lista2 = []
lista3 = []

for i in range(1, 11):
    x = int(input(f'Digite o {i}º número: '))
    lista1.append(x)

for i in range(1, 11):
    x = int(input(f'Digite o {i}º número: '))
    lista2.append(x)


for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista3)