nome = str(input('Qual seu nome? '))

#CENTRALIZADO
print('Prazer em te conhecer {:^20}!'.format(nome))
#ALINHADO A DIREITA
print('Prazer em te conhecer {:>20}!'.format(nome))
#ALINHADO A ESQUERDA
print('Prazer em te conhecer {:<20}!'.format(nome))