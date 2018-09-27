n1 = float(input('1º num: '))
n2 = float(input('2º num: '))
n3 = float(input('3º num: '))
n4 = float(input('4º num: '))

if (n2 > n1):
    maior = n2
    menor = n1
else:
    maior = n1
    menor = n2

if (n3 > n2):
    maior = n3
if (n3 < menor):
    menor = n3

if (n4 > maior):
    maior = n4
if (n4 < menor):
    menor = n4

print('MAIOR Número: {}'.format(maior))
print('MENOR Número: {}'.format(menor))
