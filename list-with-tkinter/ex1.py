'''
1) A imobiliária Imóbilis vende apenas terrenos retangulares.
Faça um algoritmo para ler as dimensões de um terreno e depois exibir a área do terreno.

Author: Marcos Souza
'''

from tkinter import *

class Application:
    def __init__(self, master=None):
        # master.geometry("400x400") #Define o tamanho da janela
        self.fontepadrao = ("Verdana", "8") #Define uma configuração de fonte padrão para ser usada mais facilmente


        # -- Containers --
        self.containerTitulo= Frame(master)
        self.containerTitulo["padx"] = 5
        self.containerTitulo["pady"] = 10
        self.containerTitulo.pack()

        self.containerLado1 = Frame(master)
        self.containerLado1["padx"] = 5
        self.containerLado1["pady"] = 5
        self.containerLado1.pack()

        self.containerLado2 = Frame(master)
        self.containerLado2["padx"] = 5
        self.containerLado2["pady"] = 5
        self.containerLado2.pack()

        self.containerResult = Frame(master)
        self.containerResult["padx"] = 5
        self.containerResult["pady"] = 5
        self.containerResult.pack()

        self.containerCalcular = Frame(master)
        self.containerCalcular["padx"] = 5
        self.containerCalcular["pady"] = 5
        self.containerCalcular.pack()

        # -- elements --
        self.titulo = Label(self.containerTitulo, text="Exercício 1 - Área de um terreno retangular")
        self.titulo["font"] = ("Calibri", "14", "bold")
        self.titulo.pack()

        self.lblLado1 = Label(self.containerLado1, text="lado1: ")
        self.lblLado1["font"] = self.fontepadrao
        self.lblLado1.pack(side=LEFT)
        self.txtLado1 = Entry(self.containerLado1)
        self.txtLado1["width"] = 30
        self.txtLado1["font"] = self.fontepadrao
        self.txtLado1.pack(side=LEFT)

        self.lblLado2 = Label(self.containerLado2, text="lado1: ")
        self.lblLado2["font"] = self.fontepadrao
        self.lblLado2.pack(side=LEFT)
        self.txtLado2 = Entry(self.containerLado2)
        self.txtLado2["width"] = 30
        self.txtLado2["font"] = self.fontepadrao
        self.txtLado2.pack(side=LEFT)

        self.lblResult = Label(self.containerResult, text="Área: ")
        self.lblResult["font"] = self.fontepadrao
        self.lblResult.pack(side=LEFT)
        self.tlblResult = Label(self.containerResult, text="", font=self.fontepadrao)
        self.tlblResult["width"] = 30
        self.tlblResult["font"] = self.fontepadrao
        self.tlblResult.pack(side=LEFT)

        self.btnCalcular = Button(self.containerCalcular, text="Calcular", font=self.fontepadrao)
        self.btnCalcular.bind('<Button-1>', self.calcularArea)
        self.btnCalcular.pack(side=LEFT)

    def calcularArea(self, event):
        l1 = float(self.txtLado1.get())
        l2 = float(self.txtLado2.get())

        self.tlblResult["text"] = str(l1 * l2)

root = Tk()
Application(root)
root.mainloop()