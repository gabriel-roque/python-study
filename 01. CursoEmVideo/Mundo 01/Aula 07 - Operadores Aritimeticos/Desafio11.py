print('=== ORCAMENTO ===')

lar = float(input('LARGURA: '))
comp = float(input('ALTURA: '))

area = (lar*comp)
tinta = (area/2)

print('E necessario para pintar uma area de {} m², {} Lt de tinta'.format(area, tinta))