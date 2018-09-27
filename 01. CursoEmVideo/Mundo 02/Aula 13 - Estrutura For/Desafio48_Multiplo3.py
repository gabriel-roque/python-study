"""
Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
"""

totalI = 0
mult = 0
somaI = 0

for c in range(1, 501, 2):
    if c%2 == 1:
        totalI += 1
    if c%3 == 0:  #sempre que quiser saber e um numero e multiplo basta saber se o resto da divisao dele e igual a 0
        mult += 1
        somaI += c

print('Total de numeros impares: {}'.format(totalI))
print('Total de multiplos impares: {}'.format(mult))
print('Soma dos {} números impares que são múltiplos de três: {}'.format(mult, somaI))
