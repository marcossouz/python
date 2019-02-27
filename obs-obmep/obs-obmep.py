from tkinter import *
from datetime import datetime


class Application:
    def __init__(self, master=None):
        self.fontepadrao = ("Arial", "10")

        self.container1 = Frame(master)
        self.container1["padx"] = 5
        self.container1["pady"] = 5
        self.container1.pack()

        self.containerCA = Frame(master)
        self.containerCA["padx"] = 5
        self.containerCA["pady"] = 5
        self.containerCA.pack()

        self.containerMUN = Frame(master)
        self.containerMUN["padx"] = 5
        self.containerMUN["pady"] = 5
        self.containerMUN.pack()

        self.containerSALA = Frame(master)
        self.containerSALA["padx"] = 5
        self.containerSALA["pady"] = 5
        self.containerSALA.pack()

        self.containerALUNO = Frame(master)
        self.containerALUNO["padx"] = 5
        self.containerALUNO["pady"] = 5
        self.containerALUNO.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 5
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 5
        self.container3["pady"] = 5
        self.container3.pack()

        self.titulo = Label(self.container1, text="Observações OBMEP2018")
        self.titulo["font"] = ("Verdana", "14", "bold")
        self.titulo.pack()

        self.loteLabel = Label(self.containerCA, text="Lote: ", font=self.fontepadrao, width="16")
        self.loteLabel.pack(side=LEFT)
        self.loteText = Entry(self.containerCA)
        self.loteText["width"] = 20
        self.loteText["font"] = self.fontepadrao
        self.loteText.pack(side=LEFT)

        self.caLabel = Label(self.containerCA, text="CA: ", font=self.fontepadrao, width="7")
        self.caLabel.pack(side=LEFT)
        self.caText = Entry(self.containerCA)
        self.caText["width"] = 50
        self.caText["font"] = self.fontepadrao
        self.caText.pack(side=LEFT)

        self.munLabel = Label(self.containerMUN, text="Município: ", font=self.fontepadrao, width="16")
        self.munLabel.pack(side=LEFT)
        self.munText = Entry(self.containerMUN)
        self.munText["width"] = 50
        self.munText["font"] = self.fontepadrao
        self.munText.pack(side=LEFT)

        self.salaLabel = Label(self.containerMUN, text="Sala: ", font=self.fontepadrao, width="7")
        self.salaLabel.pack(side=LEFT)
        self.salaText = Entry(self.containerMUN)
        self.salaText["width"] = 20
        self.salaText["font"] = self.fontepadrao
        self.salaText.pack(side=LEFT)

        self.alunoLabel = Label(self.containerALUNO, text="Nome do Aluno: ", font=self.fontepadrao, width="16")
        self.alunoLabel.pack(side=LEFT)
        self.alunoText = Entry(self.containerALUNO)
        self.alunoText["width"] = 50
        self.alunoText["font"] = self.fontepadrao
        self.alunoText.pack(side=LEFT)

        self.codLabel = Label(self.containerALUNO, text="Cod: ", font=self.fontepadrao, width="7")
        self.codLabel.pack(side=LEFT)
        self.codText = Entry(self.containerALUNO)
        self.codText["width"] = 20
        self.codText["font"] = self.fontepadrao
        self.codText.pack(side=LEFT)

        self.textoLabel = Label(self.container2, text="Ocorrencia: ", font=self.fontepadrao, width="16")
        self.textoLabel.pack(side=LEFT)
        self.texto = Entry(self.container2)
        self.texto["width"] = 60
        self.texto["font"] = self.fontepadrao
        self.texto.bind("<Return>", self.inserirDado)
        self.texto.pack(side=LEFT)

        self.btnEnviar = Button(self.container2, text="Inserir", font=self.fontepadrao, width=16)
        self.btnEnviar.bind('<Button-1>', self.inserirDado)
        self.btnEnviar.pack(side=LEFT)

        self.caText.focus()

        self.log = Label(self.container3, text="", font=self.fontepadrao)
        self.log.pack()

    def inserirDado(self, event):
        data = datetime.now()
        data_text = data.strftime('%d/%m/%Y %H:%M')

        content_log = "[" + data_text + "]LOTE: " + self.loteText.get() + "\nCentro de Aplicação: \t" + self.caText.get() + "\nMunicípio: \t\t" + self.munText.get() + "\nSala: \t\t\t" + self.alunoText.get() + "\nNome do Aluno: \t\t" + self.salaText.get() + "\nCódigo do aluno: \t" + self.codText.get() + "\nOcorrência: \t\t" + self.texto.get() + "\n"

        self.log[
            "text"] = "[" + data_text + "]LOTE: " + self.loteText.get() + "\nCentro de Aplicação: \t" + self.caText.get()

        try:
            arquivo = open("OBS_OBMEP2018.txt", "r")
            content = arquivo.readlines()
            content.append(content_log)
            content.append("\n")

            arquivo = open("OBS_OBMEP2018.txt", "w")
            arquivo.writelines(content)
            arquivo.close()

        except FileNotFoundError:
            arquivo = open("OBS_OBMEP2018.txt", "w")
            content = content_log + "\n"
            arquivo.writelines(content)
            arquivo.close()

        self.loteText.delete(0, 'end')
        self.codText.delete(0, 'end')
        self.caText.delete(0, 'end')
        self.munText.delete(0, 'end')
        self.salaText.delete(0, 'end')
        self.alunoText.delete(0, 'end')
        self.texto.delete(0, 'end')


root = Tk()
Application(root)
root.mainloop()