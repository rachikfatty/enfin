import numpy as np
from tkinter import *


def Valider(b, a):
    level1 = Tk()
    level1.geometry("800x400")

    for i in range(a):
        s1 = Label(level1, text="S" + str(i + 1))
        s1.grid(row=i + 1, column=0)
    for j in range(b):
        d1 = Label(level1, text="D" + str(j + 1))
        d1.grid(row=0, column=j + 1)

    dispo = Label(level1, text="Disponibilite")
    dispo.grid(row=0, column=b + 1, sticky=E)

    demand = Label(level1, text="Demandes")
    demand.grid(row=a + 1, sticky=W + N)
    c_temp = []
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            entry = Entry(level1)
            entry.grid(row=i, column=j)
            c_temp.append(entry)

    # Disponibilte
    b_up_temp = []
    for i in range(1, a + 1):
        entry = Entry(level1)
        entry.grid(row=i, column=b + 1)
        b_up_temp.append(entry)

    # Deamndes
    b_eq_temp = []
    for i in range(1, b + 1):
        entry = Entry(level1)
        entry.grid(row=a + 1, column=i)
        b_eq_temp.append(entry)
    
    
    def tester():
        entry_list_c = []
        entry_list_b_eq = []
        entry_list_b_up = []
        for entries in c_temp:
            entry_list_c.append(int(entries.get()))
        for entries in b_eq_temp:
            entry_list_b_eq.append(int(entries.get()))
        for entries in b_up_temp:
            entry_list_b_up.append(int(entries.get()))
        print(entry_list_c)
        print(entry_list_b_eq)
        print(entry_list_b_up)

    ValButt = Button(level1, text="Valider", command=tester)
    ValButt.grid(row=a + 1, column=b + 1)

    level1.mainloop()
