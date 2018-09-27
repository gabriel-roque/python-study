print('preços \n'.upper() + ('Ate é 200 km >> 0.50/km \n') + ('Acima de 200 km >> 0.45/km \n'))
distancia = float(input('Informe a distância da sua viagem: '))

if (distancia <= 200.00):
    print('Valor á pagar: R$ {:.2f}'.format(distancia*0.50))
else:
    print('Valor á pagar: R$ {:.2f}'.format(distancia*0.45))