# ►  E uma instrucao que permite acessar mebros nao globais e nao locais, mebros contidos no escopo externo

def func():
    var_local = 10

    def func_interna():
        nonlocal var_local
        var_local += 1
        print(var_local)

    func_interna()

func()
