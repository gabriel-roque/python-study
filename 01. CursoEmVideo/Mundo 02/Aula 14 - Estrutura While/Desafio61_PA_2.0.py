"""
DESAFIO 61

Reforce o desafio 51 lendo o primeiro termo e a razao de uma PA.
No final, mostre os 10 primeiros termos dessa progressao usando while.
"""

pt = int(input('Informe o 1° termo da PA: '))
r = int(input('Informe sua razao: '))

c = 0

while c < 10:
    c = (c + 1)
    print(pt + (r * c), end=' ► ')
print('FIM!')