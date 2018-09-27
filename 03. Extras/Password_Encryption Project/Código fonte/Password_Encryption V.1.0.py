# criar uma funcao para idiomas em ingles e portugues

from random import *

print('•='*20)
print('{:>30}'.format('| PASSWORD ENCRYPTION V.1.0 |'))
print('•='*20)
print('Selecione o Nivel de dificuldade: ')
print('''1 ► PERSONALIZADO
2 ► ALPHA 
3 ► NUMERO
4 ► ALPHANUMERICO
5 ► ALPHANUMERICO + CARACTERES ESPECIAIS''')

opcao = int(input('Qual formato deseja: ')) #opcao menu

if opcao == 1: #opcao personalzada do user
    dados = str(input('Insira os dados para a senha: ')) #recebe os dados
    senha = (' '.join(dados)) #add um espaco na string
    dividido = senha.split() #fatia toda a string
    shuffle(dividido) #embaralha a string
    novaSenha = (''.join(dividido)) #retira os espacos da string
    print('Sua nova senha: {}'.format(novaSenha)) #exibe nova senha

elif opcao == 2: #opcao personalzada do user
    listaAlpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                  'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']*5
    # lista de caracteres para sorteio (a lista se duplica 5 vezes para embaralhar mais)
    caractare = int(input('Quantos caracteres deseja: ')) #quantos caracteres o user deseja
    shuffle(listaAlpha) #embaralhar string
    novaSenha = (''.join(listaAlpha)) #retira os espacos da string
    print('Sua nova senha: {}'.format((novaSenha)[0:caractare]))

elif opcao == 3: #opcao personalzada do user
    listaNum = ['0','1','2','3','4','5','6','7','8','9']*5 #  lista dos digitos (a lista se duplica 5 vezes para embaralhar mais)
    digitos = int(input('Quantos digitos deseja: ')) #quantos digitos o user deseja
    shuffle(listaNum) #embaralha digitos
    novaSenha = (''.join(listaNum)) #retira os espacos
    print('Sua nova senha: {}'.format((novaSenha)[0:digitos])) #exibe nova senha

elif opcao == 4: #opcao personalzada do user
    listaAlphaNum = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                     'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                     '0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9']
    caractare = int(input('Quantos caracteres deseja: ')) #quantos carcatres o user deseja
    shuffle(listaAlphaNum) #embaralha senha
    novaSenha = (''.join(listaAlphaNum)) #retira os espacos
    print('Sua nova senha: {}'.format((novaSenha)[0:caractare])) #exibi nova senha

elif opcao == 5:
    listaPassword = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                     'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                     '0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9',
                     '+','-','*','/','!','@','#','$','%','^','&','(',')','{','}','[','}','.','>','<','?','|',',',';',':']
    caractare = int(input('Quantos caractes deseja: '))
    shuffle(listaPassword)
    novaSenha = (''.join(listaPassword))
    print('Sua nova senha: {}'.format((novaSenha)[0:caractare]))
else:
    print('OPCAO INVALIDA, TENTE NOVAMENTE.')

print('\nby: Gabriel Roque de M. Silva - 2017')