"""
Desafio 63

Escreva um programa que leia um numero N inteiro qualquer e mostre na tela os N primeiros
elementos de uma sequencia Fibonacci

Ex: 0 ► 1 ► 1 ► 2 ► 3 ► 5 ► 8
"""
print('=-'*10)
print('{:>14}'.format('FIBONACCI'))
print('=-'*10)

QTA = int(input('Quantos termos deseja exibir: '))

print('0 ► ', end='')

cont = 1
ultimoFBC = 1
proximoFBC = 0
FBC = 0

while cont < QTA:
    proximoFBC = proximoFBC + ultimoFBC
    print(proximoFBC, end=' ► ')
    FBC = proximoFBC - ultimoFBC
    ultimoFBC = FBC
    cont += 1
print('STOP!')
