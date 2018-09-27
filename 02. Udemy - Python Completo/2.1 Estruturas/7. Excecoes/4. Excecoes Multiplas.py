def erro (x):
    try:
        eval(x)
    except (TypeError, NameError): #posso colocar o dois erros e o mesmo tratamento para os dois.
        print('NameError ou TypeError')

erro('a')