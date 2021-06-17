import numpy as np
from tkinter import *
from calculSimplex import calculSimplex
from tkinter import ttk,messagebox


def Valider(a,b):
    level1 = Toplevel()
    level1.geometry("1000x350")
    level1.title("Data Entry")
    frame1 = Frame(level1,width=700,height=350)
    frame1.place(x=300,y=0)
    frame2 = Frame(level1,width=300,height=350,bg='#249794')
    frame2.place(x=0,y=0)
    l1=Label(frame2,text="Transportation Problem using ",fg='white',bg='#249794')
    lst1=('Calibri (Body)',12,'bold')
    l1.configure(font=lst1)
    l1.place(x=20,y=60)

    l2=Label(frame2,text="Simplex Method ",fg='white',bg='#249794')
    lst2=('Calibri',12,'bold')
    l2.configure(font=lst2)
    l2.place(x=80,y=80)
    
    for i in range(a):
        s1 = Label(frame1, text="S" + str(i + 1),font=('Calibri (Body)',10,"bold"),fg="gray32")
        s1.place(x=50, y=(i*20)+40)

    for j in range(b):
        d1 = Label(frame1, text="D" + str(j + 1),font=('Calibri (Body)',10,"bold"),fg="gray32")
        d1.place(x=(j*100)+175, y=20)
    
    dispo = Label(frame1, text="Demand",font=('Calibri (Body)',10,"bold"),fg="gray32")
    dispo.place(x=29, y=(a*20) + 48)

    demand = Label(frame1, text="Supply",font=('Calibri (Body)',10,"bold"),fg="gray32")
    demand.place(x=(b*100)+200,y=20)

    c_temp = []
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            entry =ttk.Entry(frame1,justify = CENTER)
            entry.place(x=(j*100)+50,y=(i*20)+20)
            c_temp.append(entry)
    
    # Deamnd
    b_eq_temp = []
    for i in range(1, b + 1):
        entry = ttk.Entry(frame1,justify = CENTER)
        entry.place(x=(i*100)+50, y=(a*20) + 48)
        b_eq_temp.append(entry)
    
    # Supply
    b_ub_temp = []
    for i in range(1, a + 1):
        entry = ttk.Entry(frame1,justify = CENTER)
        entry.place(x=(b*100)+200,y=(i*20)+20)
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
        level1.destroy()
        calculSimplex(a,b,c,b_ub,b_eq)    
            
    ValButt = Button(level1, text="Valider", command=idk,bd=0,cursor="hand2",font=('Calibri (Body)',10,"bold"),fg="white",bg="#249794")
    ValButt.place(x=(b*100)+400, y=(a*20)+48+40)

    myButton1 = Button(level1, text="Annuler",bd=0,cursor="hand2",font=('Calibri (Body)',10,"bold"),fg="white",bg="#249794", command=quit)
    myButton1.place(x=(b*100)+300,y=(a*20)+48+40)

    level1.mainloop()   