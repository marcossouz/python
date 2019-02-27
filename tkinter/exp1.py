from tkinter import * #importa a bibioteca gráfica

#cria a aplicação raiz. É uma janela com barra de título, botão para
#fechar,aumentar, etc.. Deve ser sempre o primeiro objeto a ser criado,
# e deve ser único em uma aplicação
root = Tk()

#cria um label com o texto especificado
w = Label(root, text = "tudo bem até aqui!")

#insere na tela
w.pack()

#inicializa o loop
root.mainloop()