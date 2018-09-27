from tkinter import *
import parser
raiz = Tk()

raiz.geometry("220x150+10+10")
raiz.title('Calculadora')

i = 0
visor = Entry(raiz)
visor.grid(row = 0, columnspan = 3, sticky = W + E)


def obter_variaveis(num):
    "Obtem a entrada adicionando o numero para variavel solicitada"
    global i
    visor.insert(i, num)
    i += 1
def limpa_visor():
    "Vai limpar todos valores do visor"
    visor.delete(0, END)

def obter_operacao(operador):
    "Obter operações onde será ultilizado pelos usuario que  deseja aplicar nas funções"
    global i
    compimento = len(operador)
    visor.insert(i, operador)
    i += compimento

def calcular():
    trabalha_papai = visor.get()
    try:
        formula = parser.expr(trabalha_papai).compile()
        resultado = eval(formula)
        limpa_visor()
        visor.insert(0, resultado)
    except Exception:
        limpa_visor()
        visor.insert(0, "Deu ruim!")

def factorial():
    """Calcular o factorial do numero sugerido."""
    trabalha_papai = visor.get()
    numero = int(trabalha_papai)
    fact = 1
    conta = numero
    try:
        while conta > 0:
            fact = fact*conta
            conta -= 1
        limpa_visor()
        visor.insert(0, fact)
    except Exception:
        limpa_visor()
        visor.insert(0, "Deu ruim!")
def desfazer():
    "remover os operadores do visor o ultimo digitado"
    trabalha_papai = visor.get()
    if len(trabalha_papai):        ## repeats until
        #Agora descrementa as istring por indice -1
        nova_string = trabalha_papai[:-1]
        print(nova_string)
        limpa_visor()
        visor.insert(0, nova_string)
    else:
        limpa_visor()
        visor.insert(0, "Deu ruim! clica em AC")

bt00 = Button(raiz, text='0', width='5', command = lambda: obter_variaveis(0))
bt01 = Button(raiz, text='1', width='5', command = lambda: obter_variaveis(1))
bt02 = Button(raiz, text='2', width='5', command = lambda: obter_variaveis(2))
bt03 = Button(raiz, text='3', width='5', command = lambda: obter_variaveis(3))
bt04 = Button(raiz, text='4', width='5', command = lambda: obter_variaveis(4))
bt05 = Button(raiz, text='5', width='5', command = lambda: obter_variaveis(5))
bt06 = Button(raiz, text='6', width='5', command = lambda: obter_variaveis(6))
bt07 = Button(raiz, text='7', width='5', command = lambda: obter_variaveis(7))
bt08 = Button(raiz, text='8', width='5', command = lambda: obter_variaveis(8))
bt09 = Button(raiz, text='9', width='5', command = lambda: obter_variaveis(9))
bt10 = Button(raiz, text='-', width='5', command = lambda: obter_operacao('-'))
bt11 = Button(raiz, text='+', width='5', command = lambda: obter_operacao('+'))
bt12 = Button(raiz, text='*', width='5', command = lambda: obter_operacao('*'))
bt13 = Button(raiz, text=',', width='5', command = lambda: obter_variaveis(','))
bt14 = Button(raiz, text='.', width='5', command = lambda: obter_operacao('.'))
bt15 = Button(raiz, text='/', width='5', command = lambda: obter_operacao('/'))
bt16 = Button(raiz, text='AC', width='5', command = limpa_visor, foreground ='red') #bg='red' cor do butão
bt17 = Button(raiz, text='=', width='5', command = calcular)
bt18 = Button(raiz, text='!', width='5', command = factorial)
bt19 = Button(raiz, text='<-', width='5', command = desfazer)
bt20 = Button(raiz, text='(', width='5', command = lambda: obter_operacao('%'))
bt21 = Button(raiz, text=')', width='5', command = lambda: obter_operacao('%'))
bt22 = Button(raiz, text='exp', width='5', command = lambda: obter_operacao('%'))
bt23 = Button(raiz, text='Pi', width='5', command = lambda: obter_operacao('%'))


bt00.grid(row=4, column=1)
bt01.grid(row=3, column=0)
bt02.grid(row=3, column=1)
bt03.grid(row=3, column=2)
bt04.grid(row=2, column=0)
bt05.grid(row=2, column=1)
bt06.grid(row=2, column=2)
bt07.grid(row=1, column=0)
bt08.grid(row=1, column=1)
bt09.grid(row=1, column=2)
bt10.grid(row=2, column=3)
bt11.grid(row=1, column=3)
bt12.grid(row=4, column=3)
bt13.grid(row=4, column=0)
bt14.grid(row=4, column=2)
bt15.grid(row=3, column=3)
bt16.grid(row=0, column=4)
bt17.grid(row=0, column=3)
bt18.grid(row=5, column=2)
bt19.grid(row=5, column=3)
bt20.grid(row=1, column=4)
bt21.grid(row=2, column=4)
bt22.grid(row=3, column=4)
bt23.grid(row=4, column=4)

raiz.mainloop()

