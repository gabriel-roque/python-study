"""
Desafio 59

Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior valor
[4] Novos numeros
[5] Sair do programa

Seu programa devera realizar a operacao em cada caso.
"""
from time import sleep

N1 = int(input('Insira o 1° Valor: '))
N2 = int(input('Insira o 2° Valor: '))

print('=-'*10)
print('[1] Somar\n'
      '[2] Multiplicar\n'
      '[3] Maior valor\n'
      '[4] Novos numeros\n'
      '[5] Sair do Programa.')
print('=-'*10 + '\n')

user = 0

while user != 5:
    user = int(input('► '))

    if user == 1: #realizar SOMA
        print('SOMA: {}'.format(N1+N2))
        user = 0
    elif user == 2: #realizar MULTIPLICACAO
        print('MULTIPLICACAO: {}'.format(N1*N2))
        user = 0
    elif user == 3: #analisar qual maior valor
        if N1 > N2:
            print('{} maior valor'.format(N1))
            user = 0
        else:
            print('O {} e o maior valor.'.format(N2))
            user = 0
    elif user == 4:
        N1 = int(input('Insira o 1° Valor: '))
        N2 = int(input('Insira o 2° Valor: '))
        print('=-' * 10)
        print('[1] Somar\n'
              '[2] Multiplicar\n'
              '[3] Maior valor\n'
              '[4] Novos numeros\n'
              '[5] Sair do Programa.')
        print('=-' * 10 + '\n')
        user = 0
    elif user == 5:
        print('Finalizando...')
        sleep(0.8)
        print('-='*10)
        print('Fim de Programa.')
        user = 5