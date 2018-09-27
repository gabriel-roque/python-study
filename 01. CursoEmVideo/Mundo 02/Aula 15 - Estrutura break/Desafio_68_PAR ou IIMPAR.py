"""
Desafio 68

Faca um programa que jogue par ou impar com o computador.
O jogo so sera interrompido quando o jogador PERDER, mostrando o total de vitorias
consecutivas que ele conquistou no final do jogo.
"""

from random import randint
from random import choice

lista = ['P', 'I']
cpu_numero = randint(0,10)  #escolha do numero de 0 a 10 pelo CPU
cpu_escolha = choice(lista) #escolha PAR ou IMPAR o CPU

resultado = ''
soma = totalHUM = 0
hum_numero = 0
hum_escolha = ''

print('-='*10)
print('{:>16}'.format('PAR OU IMPAR'))
print('-='*10)

while True:
    hum_numero = int(input('Insira o valor [0/10]: '))
    hum_escolha = str(input('PAR ou IMPAR [P/I]: ')).strip().upper()[0]
    print('=' * 40)

    soma = hum_numero + cpu_numero

    if soma%2 == 0:
        resultado = 'P'
    elif soma%2 == 1:
        resultado = 'I'

    print(f'Voce escolheu {hum_numero} e o CPU {cpu_numero} = {soma}.', end=' ')
    print('► PAR' if soma%2 == 0 else ' ► IMPAR')
    print('=' * 40)

    if resultado == hum_escolha:
        print('Parabens, voce Venceu!')
        print('-'*40)
        totalHUM += 1 #contador das vitorias do jogador
    else:
        print('CPU Venceu!')
        print('-' * 40)
        print(f'Voce venceu {totalHUM} vez(es)')
        break
