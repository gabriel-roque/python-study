"""
Desafio 60

Construir um programa que faca o fatorial de um numero.

existe a funcao factorial na biblioteca math
"""


print('MOTO TRADICIONAL')
f = int(input('Informe o valor que deseja o []! '))

fatorial = f
resultado = f

while f > 1:
    f = (f - 1)
    resultado = (resultado * f)
print('Resultado: {}'.format(resultado))

from math import factorial
print('=-='*15)
print('MODO COM A BIBLIOTECA MATH - FACTORIAL')

print('Fatorial: {}'.format(factorial(fatorial)))

