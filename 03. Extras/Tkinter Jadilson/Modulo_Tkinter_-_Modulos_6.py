from tkinter import *

janela = Tk()
janela.title('Janela Principal')

lb1 = Label(janela, text='Label 1', bg='red')
lb2 = Label(janela, text='Label 2', bg='green')
lb3 = Label(janela, text='Label 3', bg='blue')
lb4 = Label(janela, text='Label 4', bg='yellow')

lb2.pack(side=BOTTOM, fill=BOTH, expand=1)
lb1.pack(side=RIGHT, fill=Y,  expand=1)
lb3.pack(side=LEFT, fill=Y,  expand=1)
lb4.pack(side=TOP, fill=X,  expand=1)

janela.geometry("800x300+100+100")
janela.mainloop()
