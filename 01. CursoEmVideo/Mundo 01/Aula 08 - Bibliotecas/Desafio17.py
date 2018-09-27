from math import hypot
catO = float(input('Cateto Oposto: '))
catA = float(input('Cateto Adjacente: '))

print('O comprimento da Hipotenusa é igual a: {:.2f} '.format((hypot(catO, catA))))