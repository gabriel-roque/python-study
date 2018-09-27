#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

valor = float(input('Insira um valor em METROS: '))
print('{} KM'.format(valor/1000))
print('{} HM'.format(valor/100))
print('{} DM'.format(valor/10))
print('{} M'.format(valor))
print('{} DM'.format(valor*10))
print('{} CM'.format(valor/100))
print('{} MM'.format(valor/1000))