import random

a1 = str(input('1º Aluno: '))
a2 = str(input('2º Aluno: '))
a3 = str(input('3º Aluno: '))
a4 = str(input('4º Aluno: ' ))
print('')
#O pythob reconhece [LISTA] como lista
lista = [a1, a2, a3, a4]
sorteado = random.choice(lista)

print('O escolhido foi: {}'.format(sorteado))