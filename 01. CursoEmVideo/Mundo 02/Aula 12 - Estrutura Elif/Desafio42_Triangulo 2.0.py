"""
Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
Um de seus lados deve ser maior que o valor absoluto (módulo) da
diferença dos outros dois lados e menor que a soma dos outros dois lados.

>> a < (b + c)
>> c < (a + C)
>> b < (c + a)

► Adiconar verificacao do tipo de triangulo
• Equilatero: todos os lados iguais
• Isosceles: dois lados iguais
• Escaleno: todos os lados diferentes
"""
print('-=-' * 10)
print('== analizador de triangulo =='.upper())
print('-=-' * 10)

r1 = float(input('1º reta: '))
r2 = float(input('2º reta: '))
r3 = float(input('3º reta: '))

if (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2): #vereficao se e possivel construir um triangulo
    print('É possível formar um triângulo.'.upper())

    if (r1 == r2 == r3): #Equilatero: todos os lados iguais
        print('Tringulo Equilatero')
    elif (r1 == r2 or r1 == r3 or r2 == r3): #Isosceles: dois lados iguais
        print('Triangulo Isosceles')
    elif (r1 != r2 and r1 != r3):
        print('Triangulo Escaleno') #Escaleno: todos os lados diferentes
else:
    print('Não é possível formar um triângulo'.upper())
