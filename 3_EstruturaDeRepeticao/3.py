"""3. Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

nome = ''
idade = -1
salario = 0
sexo = ''
estado_civil = ''

while len(nome) < 3:
    nome = input('Digite seu nome [Maior que 3 caracteres]: ')
print('Nome validado!')


while idade < 0 or idade > 150:
    idade = int(input('Digite sua idade [Entre 0 e 150]: '))
print('Idade validada!')


while salario <= 0:
    salario = float(input('Entre com seu salário [MAIOR QUE 0]:  '))
print('Salário validado!')


while sexo != 'f' and sexo != 'm':
    sexo = input('Digite seu sexo: ').lower()
print('Sexo validado!')


while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input('Qual seu estado civil? ').lower()
print('Estado civil validado!')