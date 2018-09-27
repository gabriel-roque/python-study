# criar uma funcao para idiomas em ingles e portugues - ok
# corrigir erros ortograficos -
# melhorar visual com emojis -

from random import *

#LAYOUT DE ENTRADA
def Info():
    print('•=' * 20)
    print('{:>30}'.format('| PASSWORD ENCRYPTION V.1.0 |'))
    print('•=' * 20)

# Ira entrar no modo de seleção de idioma
def Idioma():
    # opção para usuário
    Selecionar_idioma = int(input("1 ► [PT-BR]\n"
                                  "2 ► [EUA-US]\n"
                                  "ESCOLHA O IDIOMA // CHOOSE THE LANGUAGE: "))

    # ============================== IDIOMA PT-BR ==============================
    if (Selecionar_idioma == 1):
        def Modo_desejavel():
            print('Selecione o Nivel de dificuldade:')
            print(' 1 ► PERSONALIZADO\n '
            '2 ► ALPHA\n '
            '3 ► NUMERO\n '
            '4 ► ALPHANUMERICO\n '
            '5 ► ALPHANUMERICO + CARACTERES ESPECIAIS\n')

# SESSÃO DE ESTILOS DE TIPOS DE SENHAS

        #O User escolhe com que base de digitos sera a nova senha
        def Personalizado():
            dados = str(input('Insira os dados para a senha: '))  # recebe os dados
            senha = (' '.join(dados))  # add um espaco na string
            dividido = senha.split()  # fatia toda a string
            shuffle(dividido)  # embaralha a string
            novaSenha = (''.join(dividido))  # retira os espacos da string
            print('Sua nova senha: {}'.format(novaSenha))  # exibe nova senha

        #O User so pode gerar senha com LETRAS
        def Alpha():
            listaAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                          'T',
                          'U', 'V', 'W', 'X', 'Y', 'Z',
                          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't',
                          'u', 'v', 'w', 'x', 'y', 'z'] * 5
            # lista de caracteres para sorteio (a lista se duplica 5 vezes para embaralhar mais)

            caractare = int(input('Quantos caracteres deseja: '))  # quantos caracteres o user deseja
            shuffle(listaAlpha)  # embaralhar string
            novaSenha = (''.join(listaAlpha))  # retira os espacos da string
            print('Sua nova senha: {}'.format((novaSenha)[0:caractare]))

        #O User so pode gerar senha com NUMEROS
        def Numero():
            listaNum = ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                        '9'] * 5  # lista dos digitos (a lista se duplica 5 vezes para embaralhar mais)
            digitos = int(input('Quantos digitos deseja: '))  # quantos digitos o user deseja
            shuffle(listaNum)  # embaralha digitos
            novaSenha = (''.join(listaNum))  # retira os espacos
            print('Sua nova senha: {}'.format((novaSenha)[0:digitos]))  # exibe nova senha

        #O User so pode gerar senha com LETRAS + NUMEROS
        def Alphanumerico():
            listaAlphaNum = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7',
                             '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            caractare = int(input('Quantos caracteres deseja: '))  # quantos carcatres o user deseja
            shuffle(listaAlphaNum)  # embaralha senha
            novaSenha = (''.join(listaAlphaNum))  # retira os espacos
            print('Sua nova senha: {}'.format((novaSenha)[0:caractare]))  # exibi nova senha

        #O User so pode gerar senha com LETRAS + NUMEROS + ESPECIAIS
        def Alpha_numerico_caracteres():
            listaPassword = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T',
                             'U', 'V', 'W', 'X', 'Y', 'Z',
                             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't',
                             'u', 'v', 'w', 'x', 'y', 'z',
                             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7',
                             '8', '9',
                             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                             '+', '-', '*', '/', '!', '@', '#', '$', '%', '^', '&', '(', ')', '{', '}', '[', '}', '.',
                             '>', '<',
                             '?', '|', ',', ';', ':']

            caractare = int(
                input('Quantos caractes deseja: '))  # filtra quantos carcteres sera entregue para nova password
            shuffle(listaPassword)
            novaSenha = (''.join(listaPassword))
            print('Sua nova senha: {}'.format((novaSenha)[0:caractare]))

# FIM DA SESSÃO DE ESTILOS DE TIPOS DE SENHAS

        # CENTRAL DAS FUNÇÕES (Escolha do User vem para esta função)
        def Password():
            Modo_desejavel()
            opcao = int(input('Qual formato deseja: '))  # opcao menu

            if opcao == 1:  # Opcão Personalizada pelo user
                Personalizado()

            elif opcao == 2:  # Opção Alpha
                Alpha()

            elif opcao == 3:  # Opção Numerico
                Numero()

            elif opcao == 4:  # Opção alphanumerico
                Alphanumerico()

            elif opcao == 5:  # Opção AlhaNumerico + Especiais
                Alpha_numerico_caracteres()

            else:
                print('OPCAO INVALIDA, TENTE NOVAMENTE.')

            print('\nby: Gabriel Roque and Anderson Andrade - 2017')

        #Chama a Função 'Password' para executar a escolha do user
        Password()

    #  ============================== IDIOMA EUA-US ==============================
    elif (Selecionar_idioma == 2):
        def Modo_desejavel():
            print('Select Level of difficulty:')
            print(' 1 ► CUSTOM\n '
                  '2 ► ALPHA\n '
                  '3 ► NUMERIC\n '
                  '4 ► ALPHANUMERIC\n '
                  '5 ► ALPHANUMERIC + SPECIAL CHARACTERS\n')

# SESSÃO DE ESTILOS DE TIPOS DE SENHAS

        # O User escolhe com que base de digitos sera a nova senha
        def Personalizado():
            dados = str(input('Enter the data for password: '))  # recebe os dados
            senha = (' '.join(dados))  # add um espaco na string
            dividido = senha.split()  # fatia toda a string
            shuffle(dividido)  # embaralha a string
            novaSenha = (''.join(dividido))  # retira os espacos da string
            print('Your new password: {}'.format(novaSenha))  # exibe nova senha

        # O User so pode gerar senha com LETRAS
        def Alpha():
            listaAlpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                          'T',
                          'U', 'V', 'W', 'X', 'Y', 'Z',
                          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't',
                          'u', 'v', 'w', 'x', 'y', 'z'] * 5
            # lista de caracteres para sorteio (a lista se duplica 5 vezes para embaralhar mais)

            caractare = int(input('How many characters do you want: '))  # quantos caracteres o user deseja
            shuffle(listaAlpha)  # embaralhar string
            novaSenha = (''.join(listaAlpha))  # retira os espacos da string
            print('Your new password: {}'.format((novaSenha)[0:caractare]))

        # O User so pode gerar senha com NUMEROS
        def Numero():
            listaNum = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9'] * 5
            # lista dos digitos (a lista se duplica 5 vezes para embaralhar mais)
            digitos = int(input('How many digits do you want: '))  # quantos digitos o user deseja
            shuffle(listaNum)  # embaralha digitos
            novaSenha = (''.join(listaNum))  # retira os espacos
            print('Your new password: {}'.format((novaSenha)[0:digitos]))  # exibe nova senha

        # O User so pode gerar senha com LETRAS + NUMEROS
        def Alphanumerico():
            listaAlphaNum = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7',
                             '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            caractare = int(input('How many characters do you want: '))  # quantos carcatres o user deseja
            shuffle(listaAlphaNum)  # embaralha senha
            novaSenha = (''.join(listaAlphaNum))  # retira os espacos
            print('Your new password: {}'.format((novaSenha)[0:caractare]))  # exibi nova senha

        # O User so pode gerar senha com LETRAS + NUMEROS + ESPECIAIS
        def Alpha_numerico_caracteres():
            listaPassword = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T',
                             'U', 'V', 'W', 'X', 'Y', 'Z',
                             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't',
                             'u', 'v', 'w', 'x', 'y', 'z',
                             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7',
                             '8', '9',
                             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                             '+', '-', '*', '/', '!', '@', '#', '$', '%', '^', '&', '(', ')', '{', '}', '[', '}', '.',
                             '>', '<',
                             '?', '|', ',', ';', ':']
            caractare = int(input('How many characters do you want: '))  # filtra quantos carcteres sera entregue para nova password
            shuffle(listaPassword)
            novaSenha = (''.join(listaPassword))
            print('Your new password: {}'.format((novaSenha)[0:caractare]))

            # FIM DA SESSÃO DE ESTILOS DE TIPOS DE SENHAS

        # CENTRAL DAS FUNÇÕES (Escolha do User vem para esta função)
        def Password():
            Modo_desejavel()
            opcao = int(input('Which format do you want: '))  # opcao menu

            if opcao == 1:  # Opcão Personalizada pelo user
                Personalizado()

            elif opcao == 2:  # Opção Alpha
                Alpha()

            elif opcao == 3:  # Opção Numerico
                Numero()

            elif opcao == 4:  # Opção alphanumerico
                Alphanumerico()

            elif opcao == 5:  # Opção AlhaNumerico + Especiais
                Alpha_numerico_caracteres()

            else:
                print('INVALID OPTION, TRY AGAIN.')

            print('\nby: Gabriel Roque and Anderson Andrade - 2017')

        # Chama a Função 'Password' para executar a escolha do user
        Password()

Info()
Idioma()
