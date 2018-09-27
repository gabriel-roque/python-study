# pode-se colocar listar contido dentro de sub listas

lista = [['a', 'b', 'c'], [1, 6, 8, 12], [True, False]]

print(lista) # ele imprimi toda a lista contida

print(lista[0]) # exibi apenas o primeiro item da lista raiz ou seja um lista é o 1 elemento

print(lista[0][1]) # exibi o elemento contigo dentro da sublista e assim por diante

print(len(lista[1])) #exibi a quantidade de itens existentes na lista

# para acessar o ultimo elemento de uma lista basta adicionar o -1, e recorrente ter que acessar o 1º e o Ultimo item
# de uma lista

print(lista[1][-1])