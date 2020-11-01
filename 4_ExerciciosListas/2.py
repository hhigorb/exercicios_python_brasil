"""2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""

lista_numeros = []

for _ in range(10):
    n = int(input('Digite um número: '))
    lista_numeros.append(n)

print(lista_numeros[::-1])

# ou

lista_numeros.reverse()
print(lista_numeros)