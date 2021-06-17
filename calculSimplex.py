from remplirMatriceA import remplirMatriceA
from scipy.optimize import linprog
import numpy as np
from tkinter import *

def calculSimplex(m,n,c,b_ub,b_eq):
    level2 = Tk()
    level2.geometry("1000x350")
    level2.title("Solution")
    B = remplirMatriceA(m,n)
    c_simp = c
    b_ub_simp = b_ub
    A_ub = np.zeros((m,m*n))
    for i in range(m):
        for j in range(m*n):
            A_ub[i][j]=B[i][j]


    b_eq_simp = b_eq

    A_eq = np.zeros((n,m*n))
    for i in range(n):
        for j in range(m*n):
            x=B[i+2][j]
            A_eq[i][j]=x

    method='Simplex'

    res = linprog(c=c_simp, A_ub=A_ub, b_ub=b_ub_simp,A_eq=A_eq,b_eq=b_eq_simp, bounds=(0,None), method=method)
    resultat = res.x
    frame1 = Frame(level2,width=700,height=350)
    frame1.place(x=300,y=0)

    frame2 = Frame(level2,width=300,height=350,bg='#249794')
    frame2.place(x=0,y=0)
    l1=Label(frame2,text="Transportation Problem using ",fg='white',bg='#249794')
    lst1=('Calibri (Body)',12,'bold')
    l1.configure(font=lst1)
    l1.place(x=20,y=60)

    l2=Label(frame2,text="Simplex Method ",fg='white',bg='#249794')
    lst2=('Calibri',12,'bold')
    l2.configure(font=lst2)
    l2.place(x=80,y=80)

    for i in range(m):
        s1 = Label(frame1, text="S" + str(i + 1),font=('Calibri (Body)',10,"bold"),fg="gray32")
        s1.place(x=50, y=(i*20)+40)

    for j in range(n):
        d1 = Label(frame1, text="D" + str(j + 1),font=('Calibri (Body)',10,"bold"),fg="gray32")
        d1.place(x=(j*100)+175, y=20)

    k=0
    for i in range(m):
        for j in range(n):
            e = Label(frame1,text=str(resultat[k]),font=('Calibri (Body)',10,"bold"),fg="green",bd=0)
            e.place(x=(j*100)+50+120,y=(i*20)+20+20 )
            k += 1
    level2.mainloop()





