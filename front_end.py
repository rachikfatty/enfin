import back_end as back
from tkinter import *

def main_window():
    root = Tk()
    root.geometry("800x400")

    x = IntVar()
    y = IntVar()

    label1 = Label(root, text="Nombre de fournisseurs")
    label1.grid(row=0, sticky=W, padx=10, pady=10)

    label2 = Label(root, text="Nombre de Clients")
    label2.grid(row=1, sticky=W, padx=10, pady=10)

    e = Entry(root, textvariable=x)
    f = Entry(root, textvariable=y)

    e.grid(row=0, column=1, padx=10, pady=10)
    f.grid(row=1, column=1, padx=10, pady=10)

    myButton1 = Button(root, text="Annuler", command=quit)
    myButton1.grid(row=3, column=1, padx=10, pady=10)

    myButton2 = Button(root, text="Valider", command=lambda: back.Valider(x.get(), y.get()))
    myButton2.grid(row=3, column=2, padx=10, pady=10)



    root.mainloop()
