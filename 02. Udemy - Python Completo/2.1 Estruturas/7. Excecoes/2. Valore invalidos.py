def erro(msg):
    while True: #enquanto o usuario nao inserir um valor que seja floar ira repetir
        try:
            return float(input(msg)) #puxa como parametro a mensagenm
        except ValueError: #erro ao inserir caractere
            print('Valor invalido. Digite novamente.')


n1 = erro('Insira o 1 valor: ') #parametros de mensagem
n2 = erro('Insira o 2 valor: ') #paramentros de mensagem

if n1 and n2 != 0:
    print(n1/n2)
else:
    while n2 == 0: #enquanto o usuario nao inserir um valor diferente de 0 nao prossegue.
        try:
            print(n1 / n2)
        except ZeroDivisionError: #erro ao dividir por 0
            print('Digite um valor maior que 0.')
            n2 = erro('Insira o 2 valor: ')
        if n1 and n2 != 0:
            print(n1 / n2)
