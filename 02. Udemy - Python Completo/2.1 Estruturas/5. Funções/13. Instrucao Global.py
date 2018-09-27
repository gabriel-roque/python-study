num = 10
print(num)

def func():
    global num # para ter acesso a uma variavel global e altera-la para dizer explicitamente
    num = 20

func()
print(num)