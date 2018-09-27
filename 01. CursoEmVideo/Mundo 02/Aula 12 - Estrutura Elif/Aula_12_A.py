nome = str(input('Qual seu nome? '))

if nome == 'Gabriel':
    print('Bom dia {}! Que nome bonito! '.format(nome))
# Usa-se elif quando quer colocar varias condições em uma mesma sequência de condições
# Pode-se usar quantos ELIF necessário
elif nome == 'Jonas' or 'Maria' or 'Rebeca':
    print('Bom dia {}! Que nome bonito! '.format(nome))
elif nome == 'Lucas' or 'Junior' or 'Matheus':
    print('Bom dia {}! Que nome legal!'.format(nome))
else:
    print('Tenha um Bom dia {}!'.format(nome))