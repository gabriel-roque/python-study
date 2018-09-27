print('CASO HAJA ANECESSITADADE DE ADIONAR UM ITEM AO FINAL DA LISTA')
lista01 = ['AAA','BBB','CCC',]
lista01.append('EEE') #usa-se .append
print(lista01, '\n')

print('PARA ADICIONAR ITENS EM POSIÇÕES ESPECÍFICA')

l = ['bbb','ddd','eee']
l.insert(0, 'aaa') #usa-se .insert
l.insert(2, 'ccc')
print(l,'\n')

print('ALTERANDO VALORES')
print(l)
l[1] = 'BBBB'
print(l,'\n')

print('LIMPANDO A LISTA')
l.clear()
print(l)