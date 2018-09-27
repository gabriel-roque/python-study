def erro (x):
    try:
        eval(x)
    except (TypeError, NameError):
        print('NameError ou TypeError')
    finally: #sempre será executado
        print('bloco finally')


print('►', end=" ")
erro(input())
