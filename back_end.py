import numpy as np
from tkinter import *
from calculSimplex import calculSimplex


def Valider(a,b):
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
    # Deamndes
    b_eq_temp = []
    for i in range(1, b + 1):
        entry = Entry(level1)
        entry.grid(row=a + 1, column=i)
        b_eq_temp.append(entry)
    # Disponibilte
    b_ub_temp = []
    for i in range(1, a + 1):
        entry = Entry(level1)
        entry.grid(row=i, column=b + 1)
        b_ub_temp.append(entry)

    def jj():    
        entry_list1 = []
        for entries in c_temp:
            entry_list1.append(int(entries.get()))
        c = np.array([entry_list1])
        return c
    def kk():
        entry_list2 = []
        for entries in b_eq_temp:
            entry_list2.append(entries.get())
        b_eq = np.array([entry_list2]).transpose()
        return b_eq

    def mm():
        entry_list3 = []
        for entries in b_ub_temp:
            entry_list3.append(entries.get())
        b_ub = np.array([entry_list3]).transpose()    
        return b_ub

    def idk():
        c = jj()
        b_eq = kk()
        b_ub = mm()
        calculSimplex(a,b,c,b_ub,b_eq)    
            
    ValButt = Button(level1, text="Valider", command=idk)
    ValButt.grid(row=a + 1, column=b + 1)
    level1.mainloop()   

    

            

