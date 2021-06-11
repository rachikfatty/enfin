from remplirMatriceA import remplirMatriceA
from scipy.optimize import linprog
import numpy as np
from tkinter import *

def calculSimplex(m,n,c,b_ub,b_eq):
    level2 = Tk()
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
    for i in range(m):
        s1 = Label(level2, text="S" + str(i + 1))
        s1.grid(row=i + 1, column=0)
    for j in range(n):
        d1 = Label(level2, text="D" + str(j + 1))
        d1.grid(row=0, column=j + 1)
        
    k=0
    for i in range(m):
        for j in range(n):
            e = Label(level2,text=str(resultat[k]))
            e.grid(row =i+1 ,column=j+1 )
            k += 1
    level2.mainloop()
