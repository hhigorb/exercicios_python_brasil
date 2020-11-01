"""5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR
e os números IMPARES no vetor impar. Imprima os três vetores."""


par = []
impar = []
numeros = []

for valor in range(20):
    valores = int(input('Digite um número: '))
    numeros.append(valores)
    if valores % 2 == 0:
        par.append(valores)
    else:
        impar.append(valores)


print(f'Números: {numeros}')
print(f'Pares: {par}')
print(f'Ímpares: {impar}')
