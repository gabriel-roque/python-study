"""
Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
um de seus lados deve ser maior que o valor absoluto (módulo) da
diferença dos outros dois lados e menor que a soma dos outros dois lados.

>> a < (b + c)
>> c < (a + C)
>> b < (c + a)
"""
print('-=-' * 10)
print('== analizador de triangulo =='.upper())
print('-=-' * 10)

r1 = float(input('1º reta: '))
r2 = float(input('2º reta: '))
r3 = float(input('3º reta: '))

if (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
    print('É possível formar um triângulo.'.upper())
else:
    print('Não é possível formar um triângulo'.upper())
