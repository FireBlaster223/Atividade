print('--------------------REGISTO--------------------')
login = input('Insira Seu Login : ')
senha = input('Insira Sua Senha : ')

while (login == senha):
    print('A senha não pode ser igual o login')
    print('--------------------REGISTO--------------------')
    login = input('Insira Seu Login : ')
    senha = input('Insira Sua Senha : ')
else:
    print('Login realizado com sucesso')

'''
if senha == login:
    print('A senha não pode ser igual o login')
    print('--------------------REGISTO--------------------')
    login = input('Insira Seu Login : ')
    senha = input('Insira Sua Senha : ')
else:
    print('Login criado com sucesso!')
    
'''
