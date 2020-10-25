"""5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação."""

pais_a = int(input('Digite a população do país A: '))
pais_b = int(input('Digite a população do país B: '))
porcentagem_a = float(input('Digite a % de crescimento do país A: '))
porcentagem_b = float(input('Digite a % de crescimento do país B: '))
anos = 0

while pais_a <= pais_b:
    pais_a += pais_a * (porcentagem_a / 100)
    pais_b += pais_b * (porcentagem_b / 100)
    anos += 1

print(f'O país A demorou {anos} anos para alcançar o país B\n'
      f'População país A: {int(pais_a)}\n'
      f'População país B: {int(pais_b)}')