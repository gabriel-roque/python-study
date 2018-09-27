nome = str(input('Insira seu nome: ')).strip()
dividivo = nome.split()
print('Primeiro nome: {}'.format(dividivo[0]))
print('Ultimo nome: {}'.format(nome.split()[len(dividivo)-1]))