#shuffle para embaralhar
from random import shuffle
n1 = str(input('1 Aluno: '))
n2 = str(input('2 Aluno: '))
n3 = str(input('3 Aluno: '))
n4 = str(input('4 Aluno: '))

lista = [n1, n2 , n3 , n4]
shuffle (lista)

print('A ordem de apresetacao sera: {}'.format(lista))