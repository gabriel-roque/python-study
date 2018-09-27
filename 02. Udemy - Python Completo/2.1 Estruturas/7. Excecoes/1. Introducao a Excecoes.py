try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print('Nao e possivel divisao por.\nTente novamente!')
