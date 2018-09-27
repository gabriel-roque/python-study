# Criar um algoritmo para a IA jogar Jokenpô
"""
Regra:
Papel ganha de Pedra  ► Pedra perde para Papel     2 ganha de 1 ► 1 perde para 2
Tesoura ganha de Papel ► Papel perde para Tesoura  3 ganha de 2 ► 2 perde para 3
Pedra ganha Tesoura ► Tesoura perde pra Pedra      1 ganha de 3 ► 3 perde para 1
"""
from random import choice
from time import *
from emoji import *
print('-='*8)
print('{:^15}'.format('== JOKENPÔ =='))
print('-='*8)
lista = ['Pedra','Papel','Tesoura']

cpu = choice(lista) # IA realiza sua escolha

print('[1] Pedra\n'
      '[2] Papel\n'
      '[3] Tesoura')
user = int(input('• '))
#tradutor de numeracao para string - alinhamento de resultado
if user == 1:
    user = 'Pedra'
elif user == 2:
    user = 'Papel'
elif user == 3:
    user = 'Tesoura'

print('JO', end=' ')
print(emojize(':hand:', use_aliases=True))
sleep(0.5)
print('KEN', end=' ')
print(emojize(':fist:', use_aliases=True))
sleep(0.5)
print('PÔ!!!', end=' ')
print(emojize(':v:\n', use_aliases=True))
sleep(0.4)

print('IA: Eu escolhi {}'.format(cpu))

if cpu == user:
    print('EMPATE')
#Possibilidade 01 e 02
elif user == 'Papel' and cpu == 'Pedra':
    print('Você Ganhou!')
#Possibilidade 03 e 04
elif user == 'Tesoura' and cpu == 'Papel':
    print('Você Ganhou!')
#Possibilidade 05 e 06
elif user == 'Pedra' and cpu == 'Tesoura':
    print('Você Ganhou!')
else: #caso nenhuma das concidoes execute acima o usuario perde
    print('Voce perdeu!')