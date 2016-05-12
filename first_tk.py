from tkinter import *
from collections import __main__

class Janela:
    def __init__(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Oi!', background='green')
        self.botao.pack()

def main():
    raiz=Tk()
    Janela(raiz)
    raiz.mainloop()
    
if __name__ == '__main__':
    main()