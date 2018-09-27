"""
DESAFIO 51

Desenvolva um programa que leia o primeiro termo e a razao de uma PA.
No final, mostre os 10 primeiros termos dessa progressao.
"""
print('10 TERMOS DE P.A.')
print('='*20)
pt = int(input('Digite o primeiro termo: '))
r = int(input('Insira a razao: '))

for c in range(0,10):
    print(pt+(r*c),end=' ► ')
print('FIM!')