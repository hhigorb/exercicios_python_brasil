"""
3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
M - Masculino, Sexo Inválido.
"""

sexo = input('Digite [F] para feminino ou [M] para masculino: ').upper()

if sexo == 'F':
    print('Sexo selecionado: Feminino')
elif sexo == 'M':
    print('Sexo selecionado: Masculino')
else:
    print('Sexo inválido. Por favor, digite [F] ou [M]!')