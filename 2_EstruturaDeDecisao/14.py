"""
14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if 9 <= media <= 10:
    print(f'Aprovado! Você recebeu um conceito A!')

elif 7.5 <= media <= 9:
    print(f'Aprovado! Você recebeu um conceito B!')

elif 6 < media <= 7.5:
    print(f'Aprovado! Você recebeu um conceito C!')

elif 4 <= media <= 6:
    print(f'Reprovado! Você recebeu um conceito D!')

else:
    print(f'Reprovado! Você recebeu um conceito E!')

print(f'Nota 1: {n1}\n'
      f'Nota 2: {n2}\n'
      f'Média: {media}')