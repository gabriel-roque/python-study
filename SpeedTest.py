def erro(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print('Valor invalido. Digite novamente.')


n1 = erro('Insira o 1 valor: ')
n2 = erro('Insira o 2 valor: ')

if n1 and n2 != 0:
    print(n1/n2)
else:
    while n2 == 0:
        try:
            print(n1 / n2)
        except ZeroDivisionError:
            print('Digite um valor maior que 0.')
            n2 = erro('Insira o 2 valor: ')
        if n1 and n2 != 0:
            print(n1 / n2)
