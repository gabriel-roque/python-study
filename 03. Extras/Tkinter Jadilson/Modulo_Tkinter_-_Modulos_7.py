from tkinter import *

janela = Tk()
janela.title('Janela Principal')

lb1 = Label(janela, text='Label 1', bg='red')
lb2 = Label(janela, text='Label 2', bg='green')
lb3 = Label(janela, text='Label 3', bg='blue')
lb4 = Label(janela, text='Label 4', bg='yellow')

lb2.grid(row=1, column=1)
lb1.grid(row=2, column=2)
lb3.grid(row=3, column=3)
lb4.grid(row=4, column=4)

janela.geometry("800x300+100+100")
janela.mainloop()
