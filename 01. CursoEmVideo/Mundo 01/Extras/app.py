# -*- coding: UTF-8 -*-

def lista (nomes):
	print ("Listando nomes:")
	for nome in nomes:
			print (nome)

def cadastrar (nomes):
	print ("Digite o nome que deseja cadastrar: ")
	nome = input()
	nomes.append(nome)

def procurar(nomes):
    print ('Digite o nome a procurar:')
    nome = input()
    if(nome in nomes):
        print ("Nome %s está cadastrado" % (nome))
    else:
        print ("Nome %s não está cadastrado" % (nome))

def menu():
	nomes = []
	escolha = ""
	while (escolha != "0"):
		print ("Digite 1 para cadastrar, 2 para ver lista, 3 para procurar nomes, 0 para terminar")
		escolha = input()

		if(escolha == "1"):
			cadastrar(nomes)

		if(escolha == "2"):
			lista(nomes)

		if(escolha == "3"):
			procurar(nomes)

menu()