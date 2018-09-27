pt = int(input('Informe o 1° termo da PA: '))
r = int(input('Informe sua razao: '))

c = 0
resp = 0
qta = 0
mais = 10

while mais != 0:
    qta = qta + mais
    while c <= qta:
        c = (c + 1)
        print(pt + (r * c), end=' ► ')
    print('PAUSA')

    mais = int(input('Quantos termo a mais quer exibir: '))
