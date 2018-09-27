tel = {
    30301122: 'Pericles',
    33547877: 'Menelau',
    33381245: 'Atreu',
    36458889: 'Tieste'
}

print(len(tel)) #quantidade de elementos
del(tel[36458889]) # excluir elementos
print(tel.keys()) # exibi as chaves do dicionario
print(tel.values()) # exibir os valores
print(33381245 in tel) #verifica se esta contido

tel2 = {
    99999999: 'teste01',
    55555555: 'Teste02'
}
tel.update(tel2) # usa-se para mesclar os dicionarios
print(tel)