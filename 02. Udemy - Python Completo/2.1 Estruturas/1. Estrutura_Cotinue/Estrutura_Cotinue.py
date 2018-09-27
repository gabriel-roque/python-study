'''
A estrutura continue ela finaliza apenas UM UNICO CICLO e continua com os proximos ate finalizar.
'''

print('Inicio')
cont = 0

while cont <= 10:
    cont += 1
    if (cont%2 == 1):
        continue
    print(cont)
print('Fim')
