"""
Desafio 67

Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
O programa sera interrompido quando o numero for negativo.
"""

valor = cont = 0

while True:
    valor = int(input('Qual tabuada deseja: '))
    print('=' * 20)
    cont = 0 # recebe 0 para resetar o procedimento da tabuada

    if valor < 0: # para encerramento do programa
        print('Fim do programa...')
        break

    for cont in range(0,11):
        print(f'{valor} X {cont} = {valor*cont}') #utilizando F - String
        cont += 1
    print('=' * 20)

