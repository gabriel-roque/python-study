cores = ['azul', 'vermelho', 'verde', 'amarelo', 'preto', 'branco']



while True:
    cor = str(input('Escolha um cor ou 0 para SAIR: ').lower())

    if cor == '0':
        break
    elif cor in cores:
        print('A cor esta contida.')
    else:
        print('A cor nao esta contida.')