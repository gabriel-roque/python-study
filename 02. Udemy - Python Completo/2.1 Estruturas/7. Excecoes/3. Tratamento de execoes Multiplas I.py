def erro(x):
    try:
        eval(x)
    except TypeError:
        print('TypeError')

erro("int+int")