nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

while nome == senha:
    print('Sua senha não pode ser seu nome.')
    print('Por favor, digite novamente seu nome e senha.')
    print("-" * 30)
    
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ') 

print(f'Olá, {nome}, sua senha está segura comigo ;)')