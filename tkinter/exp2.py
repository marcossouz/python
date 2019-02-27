from tkinter import *
from tkinter.ttk import *

'''
http://effbot.org/tkinterbook/

'''

root = Tk()

label = Label(root, text="text")
label.pack()

button = Button(root, text="button")
button.pack()

canvas = Canvas(root, width=200, height=100)
canvas.pack()
canvas.create_line(0, 0, 200, 100)
canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
canvas.create_rectangle(50, 25, 150, 75, fill="blue")

var = IntVar()
checkbutton = Checkbutton(root, text="Expand", variable=var)
checkbutton.pack()

combobox = Combobox(root, values = ["january", "February", "March", "April"])
combobox.pack()

entry = Entry(root)
entry.pack()

frame = Frame(root, height=2)
frame.pack(fill=X, padx=15, pady=15)

labelFrame = LabelFrame(root, text="Group")
labelFrame.pack()

listbox = Listbox(root)
listbox.pack()

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

mb = Menubutton(root, text='Choose One')
menu = Menu(mb)

message = Message(root, text="this is a message")
message.pack()

root.mainloop()

'''
notebook	optionMenu	panedwindow	progressbar	radiobutton	scale
scrollbar	separator	sizegrip	spinbox	text	treeview

Diálogos disponíveis

chooseColor	chooseDirectory	dialog	getOpenFile
getSaveFile	messageBox	popup	toplevel

Posicionamento dos objetos na tela

place : posicionamento em posições absolutas
grid: posiciona os objetos numa grade virtual na tela
pack: posiciona os objetos acima ou ao lado relativos um ao outro

https://cadernodelaboratorio.com.br/2017/01/17/tkinter-interface-grafica-para-programas-em-python/

'''