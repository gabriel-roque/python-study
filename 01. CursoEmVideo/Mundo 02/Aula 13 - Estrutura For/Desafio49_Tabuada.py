"""
Desafio 49

Tabuada
"""
valor = int(input('Qual tabuada deseja relizar: '))

for c in range(1,11):
    print('{} x {} = {}'.format(valor, c,(valor*c)))
    c += 1