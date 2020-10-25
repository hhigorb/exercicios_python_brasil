"""15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de
gerar a série até o n−ésimo termo."""

ultimo_numero = int(input('Até qual número gerar a série de Fibonacci? '))
anterior = 0
proximo = 0

for _ in range(ultimo_numero):
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior

    if proximo == 0:
        proximo += 1