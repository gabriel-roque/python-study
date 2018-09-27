listaString = ['teste01', 'teste02', 'teste03', 'teste04']

print(listaString) #imprimi todos os itens da lista

print(listaString[2]) #informando o indice da lista para exibir o elemento

listaNumero = [1, 2, 3, 4, 5]

#Uma lista é um aglomerado de variaies entao podemos realizar operações com elas.
print(listaNumero)

print(listaNumero[0] + listaNumero[3])


#=============================================================================
#o interpretador do python ira reconhecer como apenas unico item da lista quando colocado virgula depois
lista = list(('Python'))

print(lista)

lista = list(('Python',))

print(lista)


print(type(lista))