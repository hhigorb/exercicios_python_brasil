"""
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

vogais = 'aeiou'
letra = str(input('Digite uma letra: ')).lower()
if letra.isalpha():
    if letra in vogais:
        print('É uma vogal!')
    else:
        print('É uma consoante!')
else:
    print('Você deve digitar uma letra!')