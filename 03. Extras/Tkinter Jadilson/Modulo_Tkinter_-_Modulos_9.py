from tkinter import *

janela = Tk()
janela.title('Janela Principal')

lbvertical = Label(janela, text='Vertical')
lbHorizotal = Label(janela, text='Horizontal', bg='red')
lb = Label(janela, text='Espaço', width=15, height=3, bg='blue')

lb.grid(row=0, column=1)
lbHorizotal.grid(row=1, column=1, sticky=W)
lbvertical.grid(row=2, column=1, sticky=E)


janela.geometry("200x100+100+100")
janela.mainloop()
