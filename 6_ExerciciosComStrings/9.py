"""
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de
formatação.
"""

"""
Verificador de CPF's verdadeiro:

Passo 1:
Em 90% dos casos, esta simples soma dos números do CPF demonstra a veracidade do documento.

Nº: 003.939.708-41

Somando-se os números do documento o resultado é 44. A soma dos números deve resultar sempre em dois números iguais.

Passo 2:

Outra maneira de verificar a veracidade do documento é conferir o último número antes do dígito, de acordo com a
tabela abaixo:

Exemplo: Nº:  003.939.708-41 = Código 8, corresponde ao Estado de São Paulo.

Veja abaixo o código de Identificação por Estado:      

Código 0:  Rio Grande do Sul    

Código 1:  Distrito Federal – Goiás – Mato Grosso – Mato Grosso do Sul – Tocantins    

Código 2:  Pará – Amazonas – Acre – Amapá – Rondônia – Roraima    

Código 3:  Ceará – Maranhão – Piauí    

Código 4:  Pernambuco – Rio Grande do Norte – Paraíba – Alagoas    

Código 5:  Bahia – Sergipe    

Código 6:  Minas Gerais    

Código 7:  Rio de Janeiro – Espírito Santo

Código 8:  São Paulo

Código 9: Paraná – Santa Catarina
"""

cpf = input('Digite seu CPF no formato [XXX.XXX.XXX-XX]: ')
numeracao = []
codigos_validos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for valor in cpf:
    if valor.isdigit():
        numeracao.append(int(valor))

v1 = sum(numeracao)

# separando as casas dos números:
decimal = v1 // 10 % 10
unidade = v1 // 1 % 10

if sum(numeracao) == 0:
    print('INVÁLIDO!')
elif decimal == unidade and numeracao[8] in codigos_validos:
    print(f'{cpf} é VÁLIDO!')
else:
    print(f'O CPF não é válido!')





