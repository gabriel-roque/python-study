n = input('Digite seu nome completo: ').title()
print('O nome digitado foi: {}'.format(n))
print('Primeiro: {}'.format(n.split()[0]))
print('Último: {}'.format(n.split()[len(n.split())-1]))