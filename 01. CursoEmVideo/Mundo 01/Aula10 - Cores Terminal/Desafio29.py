import emoji
print('SISTEMA DE TRÂNSITO', end=' ')
print(emoji.emojize(':no_entry_sign: \n', use_aliases=True))
velocidade = float(input('Qual a sua velocida Km/h: '))

kmE = (velocidade - 80.0)
Vmulta = (kmE * 7)

if velocidade >= 80.0:
    print('>> Você foi MULTADO \n')
    print('Verifique o valor de sua multa logo abaixo.'.upper())
    print('>> Km excedido {:.2f} km/h'.format(kmE))
    print('>> Valor da MULTA: R$ {:.2f},00'.format(Vmulta))
else:
    print('>> Sem Multas')