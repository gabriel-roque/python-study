lista = [1,2,3,4,5]

print(lista, 'NORMAL\n')

lista += [6,7]

print(lista, 'ADICIONANDO no final...\n')

lista = [0] + lista

print(lista, 'ADICIONANDO no início...\n')

#podemos adicionar com a função .append
lista.append(8)
print(lista, 'ADICIONANDO com .append\n')

#para excluirmos basta utiluzar a função del

del(lista[-1])

print(lista, 'EXCLUINDO ITEM  com del')

