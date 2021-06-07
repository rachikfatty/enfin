import back_end as back
from tkinter import *

root = Tk()

x = IntVar()
y = IntVar()

label1 = Label(root, text="Nombre de fournisseurs")
label1.grid(row=0, sticky=W)

label2 = Label(root, text="Nombre de Clients")
label2.grid(row=1, sticky=W)

e = Entry(root, textvariable=x)
f = Entry(root, textvariable=y)

e.grid(row=0, column=1)
f.grid(row=1, column=1)

myButton1 = Button(root, text="Annuler", command=quit)
myButton1.grid(row=3, column=1)
myButton2 = Button(root, text="Valider", command=lambda: back.Valider(x.get(), y.get()))
myButton2.grid(row=3, column=2)


root.mainloop()
