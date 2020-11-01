"""11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada."""

lista1 = []
lista2 = []
lista3 = []
lista4 = []

# vetor 1
for i in range(1, 11):
    n = int(input(f'Digite o {i}º valor: '))
    lista1.append(n)


# vetor 2
for i in range(1, 11):
    n = int(input(f'Digite o {i}º valor: '))
    lista2.append(n)

# vetor 3
for i in range(1, 11):
    n = int(input(f'Digite o {i}º valor: '))
    lista3.append(n)


for i in range(10):
    lista4.append(lista1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])


print(lista4)