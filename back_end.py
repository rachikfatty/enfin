import numpy as np
from tkinter import *
import calculSimplex as cal

def Valider(b, a):
    level1 = Tk()
    level1.geometry("800x400")

    for i in range(a):
        s1 = Label(level1, text="S" + str(i + 1))
        s1.grid(row=i + 1, column=0, padx=10, pady=10)
    for j in range(b):
        d1 = Label(level1, text="D" + str(j + 1))
        d1.grid(row=0, column=j + 1, padx=10, pady=10)

    dispo = Label(level1, text="Disponibilite")
    dispo.grid(row=0, column=b + 1, sticky=E, padx=10, pady=10)

    demand = Label(level1, text="Demandes")
    demand.grid(row=a + 1, sticky=W + N, padx=10, pady=10)
    c_temp = []
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            entry = Entry(level1)
            entry.grid(row=i, column=j)
            c_temp.append(entry)
    
    # Disponibilte
    b_ub_temp = []
    for i in range(1, a + 1):
        entry = Entry(level1)
        entry.grid(row=i, column=b + 1)
        b_ub_temp.append(entry)
    b_ub = np.array(b_ub_temp)
    b_ub.reshape(-1, 1) 

    # Deamndes
    b_eq_temp = []
    for i in range(1, b + 1):
        entry = Entry(level1)
        entry.grid(row=a + 1, column=i)
        b_eq_temp.append(entry)
    b_eq = np.array(b_eq_temp) 
    b_uq.reshape(-1, 1)    
            
    ValButt = Button(level1, text="Valider", command=lambda: cal.calculSimplex(b,a,b_ub,b_uq))
    ValButt.grid(row=a + 1, column=b + 1, padx=10, pady=10)
    level1.mainloop()
    

            

