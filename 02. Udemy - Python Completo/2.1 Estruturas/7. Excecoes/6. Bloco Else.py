def erro (x):
    try:
        eval(x)
    except (TypeError, NameError):
        print('NameError ou TypeError')
    else: #bloco else so ocorre quando nao é encontrado o erro algum
        print('Nenhuma exceção ocorreu.')

print('►', end=" ")
erro(input())