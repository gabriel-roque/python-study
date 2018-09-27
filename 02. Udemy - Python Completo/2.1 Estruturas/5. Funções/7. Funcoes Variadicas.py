def lista_de_argumentos (*args): #para informar qua alista ira conter valores variados basta adicionar o * antes da lista
    print(args)

def lista_de_argumentos_associativos(**kwargs): #utiiza dois ** para informar que e uma lista associativa
    print(kwargs)

lista_de_argumentos(1, 2, 3, 4, 5, 6)
lista_de_argumentos('um', 'dois', 'tres', 'quatro')

lista_de_argumentos_associativos(a = 1, b = 2, c = 3, d = 4)
lista_de_argumentos_associativos(um = 1, dois = 2, tres = 3, quatro = 4)