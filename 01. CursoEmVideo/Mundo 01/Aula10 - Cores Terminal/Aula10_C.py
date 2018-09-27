n1 = float(input('1º Nota: '))
n2 = float(input('2º Nota: '))
m = (n1 + n2)/2

print('Média: {:.1f}'.format(m))

if m >= 7.0:
    print('PARABÉNS!')
if m <= 6.9:
    print('ESTUDE MAIS!')
