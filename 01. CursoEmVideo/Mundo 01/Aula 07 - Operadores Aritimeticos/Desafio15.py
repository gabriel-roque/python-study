print('CAR`S GEEK_net \n')

QtaDias = int(input('Quantidades de dias alugado: '))
KmPer = float(input('Quantos KM foram percorridos: '))

total = (QtaDias * 60) + (KmPer * 0.15)

print('O total a pagar: R$ {:.2f}'.format(total))