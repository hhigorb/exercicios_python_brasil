"""15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada
de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;"""

notas = []

while True:
    nota = int(input('Digite uma nota: '))
    if nota == -1:
        print('Encerrando o programa...')
        break
    notas.append(nota)

soma = sum(notas)
media = soma / len(notas)
acima_media = 0
abaixo_media = 0

for i in notas:
    if i > media:
        acima_media += 1
    if i < media:
        abaixo_media += 1

print(f'Quantidade de valores lidos: {len(notas)}\n'
      f'Soma dos valores: {soma}\n'
      f'Média dos valores: {media}\n'
      f'Valores acima da média: {acima_media}\n'
      f'Valores abaixo da média: {abaixo_media}')

print('Um abaixo do outro em ordem invertida:')
for i in notas[::-1]:
    print(i)