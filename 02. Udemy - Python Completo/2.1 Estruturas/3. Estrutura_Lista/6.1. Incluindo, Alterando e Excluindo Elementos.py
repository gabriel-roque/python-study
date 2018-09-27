# por padrão a funcao .pop exclui o ultimo item da lista
l = ['aaa','bbb','ccc','ddd','eee',]
l.pop()
print(l)
#excluindo um item especifíco
l = ['aaa','bbb','ccc','ddd','eee',]
l.pop(2)
print(l)
#excluindo vários itens ao mesmo tempo
l = ['aaa','bbb','ccc','ddd','eee',]
del(l[2:4])
print(l)