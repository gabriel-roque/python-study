# iteramento é percorrer todos os itens. #APENAS PERCORRER NÃO FUNCIONA
lista_num = [100, 200, 300, 400]
for item in lista_num:
    print(item)


lista_num = [100, 200, 300, 400, 500, 600, 700, 800]
#processo de adição
for item in range(len(lista_num)): # é necessário um indice para saber qual número o laço de repetição ira percorrer
    lista_num[item] += 1000 # para cada item da lista ele ira acessar e adiconar o valor de 1000
print(lista_num)


# função de nomo enumerate
lista_num = [100, 200, 300, 400, 500, 600, 700, 800]
for idx, item in enumerate(lista_num):
    lista_num[idx] += 1000
print(lista_num)