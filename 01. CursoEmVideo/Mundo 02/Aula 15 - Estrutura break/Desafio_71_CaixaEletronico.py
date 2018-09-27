"""
Desafio 71

Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual sera o valor a ser sacado e o programa vai informar quantas cedulas de cada valor
serao entregues.

OBS: consideque que o caixa possui cedulas de 50, 20, 10 e 1
"""

print('ƒ'*20)
print('{:>14}'.format('ITAU BANK'))
print('ƒ'*20)

valor = int(input('Quanto deseja sacar R$: '))
nota50 = nota10 = nota1 =  resto = 0
nota20 = 0

while True:

    nota50 = valor // 50
    resto = valor - (nota50 * 50)

    nota20 = resto // 20
    resto = resto - (nota20 * 20)

    nota10 = resto // 10
    resto = resto - (nota10 * 10)

    nota1 = resto // 1
    resto = resto - (nota1 * 1)


    if resto == 0:
        break

print(f'{nota50} de R$ 50.00')
print(f'{nota20} de R$ 20.00')
print(f'{nota10} de R$ 20.00')
print(f'{nota1} de R$ 1.00')
