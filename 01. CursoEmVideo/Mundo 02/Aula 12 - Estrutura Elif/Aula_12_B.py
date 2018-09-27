print('Olá! eu sou Cortana! ')

nome = str(input('....Qual é seu nome? '))

if nome in ('Gabriel Lucas João Gustavo'):
    print('{} você possue um belo nome Masculino.'.format(nome))
elif nome in ('Maria Rebeca Júlia Camila'):
    print('{} você possue um belo nome Feminino'.format(nome))
else:
    print('Bom dia {}!'.format(nome))