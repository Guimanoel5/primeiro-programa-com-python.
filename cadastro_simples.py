from getpass import getpass
nome = input('Qual seu nome?  ')
print('Bem vindo', nome)
salario = int(input('Qual seu salario(somente números)? '))
print(salario)
if salario > 5000:
    print('Nossa você é muito rico mesmo.')
else:
    print('pobre kkkkkkkkkkk')
senha = getpass('Qual sua senha?')
print(senha, 'esta é sua senha')
print('deseja confirmar sua senha?')
confirmação = input('digite sim ou nao.')
if confirmação == ('sim'):
    print('Ok, obrigado por se cadastrar.')
else:
    print('digite sua senha novamente')
    senha = getpass('Qual sua senha(ultima tentativa)?')
    pronto = input('Confirma essa senha?')
print('Bem vindo a nossa empresa', (nome))
final = input('diga-me tchau', nome)('!')
