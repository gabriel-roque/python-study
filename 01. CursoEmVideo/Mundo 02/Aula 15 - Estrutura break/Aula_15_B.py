n = soma = 0

while True:
    n = int(input('Insira o valor: '))
    if n == 999:
        break
    soma += n
print('A soma vale: {}'.format(soma))

# novo formato de edicao de string  F - STRINGS
print(f'A soma vale: {soma}')