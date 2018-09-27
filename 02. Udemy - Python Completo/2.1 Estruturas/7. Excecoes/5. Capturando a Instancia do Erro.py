def erro (x):
    try:
        eval(x)
    except NameError as e:
        print(type(e)) #instancia da excecao
        print(e.args) #argumentos as mensagens
        print(e)

erro("a")