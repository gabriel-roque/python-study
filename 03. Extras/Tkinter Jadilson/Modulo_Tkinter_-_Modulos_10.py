from tkinter import *

janela = Tk()
janela.title('Janela Principal')

lb1 = Label(janela, text='Label 1', width=15, height=6, bg='red')
lb2 = Label(janela, text='Label 2', width=15, height=6, bg='green')
lb3 = Label(janela, text='Label 3', width=15, height=6, bg='blue')
lb4 = Label(janela, text='Label 4', width=15, height=6, bg='yellow')

lb5 = Label(janela, text='Label 4', width=5,  bg='pink')
lb6 = Label(janela, text='Label 4', height=3, bg='black')

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
lb3.grid(row=0, column=1)
lb4.grid(row=1, column=1)

lb5.grid(row=2, column=0, columnspan=2, sticky=W+E)
lb6.grid(row=0, column=2, rowspan=2, sticky=N+S)

janela.geometry("800x300+100+100")
janela.mainloop()
