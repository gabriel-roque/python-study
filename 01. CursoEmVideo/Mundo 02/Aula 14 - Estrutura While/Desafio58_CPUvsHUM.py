"""
Desafio 58

Melhore o jogo do Desafio 28 onde o computador vai pensar em um numero de 1 a 10.
So que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios.
"""

from random import randint

cpu = (randint(1,10)) #ira escolhe um numero de 0 a 10

totE = 0
hum = 0
while hum != cpu:
    hum = int(input('Tente adivinhar [1/10]: ')) #entrada do user

    if hum == cpu: #avalia se certou
        print('Parabens, voce acertou')
        print('='*20)
    else: #caso ele erre
        totE += 1
        print('Tente novamente!')
        print('='*20)

print('Voce usou {} tentariva(as).'.format(totE))