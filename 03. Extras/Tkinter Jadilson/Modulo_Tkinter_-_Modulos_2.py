from tkinter import *

def bt_click():

    if(str(ed1.get()).isnumeric() and (str(ed2.get())).isnumeric()):
        n1 = float(ed1.get())
        n2 = float(ed2.get())
        lb["text"] = n1*n2
    else:
        lb['text'] = 'Valores informados são invalidos'

janela = Tk()
janela.title('Janela Principal')
janela["bg"] = "red"
janela["background"] = "blue"
#LxA+E+T
#300x300+100+100
janela.geometry("800x300+100+100")

ed1 = Entry(janela)
ed1.place(x=100, y=100)
ed2 = Entry(janela)
ed2.place(x=100, y=130)

bt = Button(janela, width=20, text='Ok', command=bt_click)
bt.place(x=100, y=150)
lb = Label(janela, text='')
lb.place(x=100, y=200)

janela.mainloop()
