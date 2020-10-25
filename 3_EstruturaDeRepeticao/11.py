"""11. Altere o programa anterior para mostrar no final a soma dos números."""

n1 = int(input('Digite o número inicial: '))
n2 = int(input('Digite o número final: '))
soma = 0

for valor in range(n1+1, n2):
    print(valor)
    soma += valor

print(f'A soma total dos valores é de: {soma}')