import random
from time import sleep
print('ADIVINHE!')
player = int(input('Tente adivinhar [0-5]: '))

#usa o ranint para ele escolher um numero inteiro .choice é apenas para escolher itens de listas

cpu = (random.randint(0,5)) #computador escolhe um número
print('PROCESSANDO....')
sleep(1.3)
print('-=-' * 10)
print('O número sorteado foi {}'.format(cpu))
print('-=-' * 10)

if cpu == player:
    print('Parabéns!, você acertou!')
else:
    print('Tente novamente!')