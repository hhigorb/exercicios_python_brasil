"""2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações."""

usuario = input('Digite um usuario: ')
senha = input('Digite uma senha: ')

while usuario == senha:
    print('Usuário e senhas não podem corresponder. Defina uma senha diferente.')
    senha = input('Digite uma senha: ')

print('Cadastro realizado com sucesso!')