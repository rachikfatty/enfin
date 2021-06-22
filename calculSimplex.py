from remplirMatriceA import remplirMatriceA
from scipy.optimize import linprog
import numpy as np
from tkinter import *
from tkinter import ttk,messagebox

def calculSimplex(m,n,c,b_ub,b_eq):
    level2 = Tk()
    level2.geometry("1100x350")
    blank_space ="  "
    level2.title(80*blank_space+"Solution")
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
    frame1 = Frame(level2,width=2000,height=700,relief="sunken")
    frame1.place(x=300,y=0)
    
    hscrollbar = ttk.Scrollbar(frame1, orient = HORIZONTAL)
    vscrollbar = ttk.Scrollbar(frame1, orient = VERTICAL)
    canvas = Canvas(frame1,width=760,height=320, bd=0, highlightthickness=0, yscrollcommand = vscrollbar.set, xscrollcommand = hscrollbar.set)
    vscrollbar.config(command = canvas.yview)
    hscrollbar.config(command = canvas.xview)
    
    subframe = Frame(canvas,width=2000,height=700)
    
    subframe.place(x=300,y=0)
    hscrollbar.pack( fill=X, side=BOTTOM, expand=FALSE)
    vscrollbar.pack( fill=Y, side=RIGHT, expand=FALSE)
    canvas.pack(side = LEFT, padx  = 5, pady   = 5, fill = BOTH, expand=TRUE)
    


    canvas.create_window(0,0, window = subframe)
    level2.update_idletasks() # update geometry
    canvas.config(scrollregion = canvas.bbox("all"))
    canvas.xview_moveto(0) 
    canvas.yview_moveto(0)

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

    total=0
    for b in range(len(resultat)):
        if resultat[b] != 0 : 
            total = total + int(c_simp[0][b])*resultat[b]

    tot = Label(subframe, text="The minimum total transportation cost",font=('Calibri (Body)',10,"bold"),fg="gray32")
    tot.place(x=0, y=(m*20)+80)

    tot1 = Label(subframe, text=str(total),font=('Calibri (Body)',10,"bold"),fg="green")
    tot1.place(x=250, y=(m*20)+80)

    for i in range(m):
        s1 = Label(subframe, text="S" + str(i + 1),font=('Calibri (Body)',10,"bold"),fg="gray32")
        s1.place(x=50, y=(i*20)+40)

    for j in range(n):
        d1 = Label(subframe, text="D" + str(j + 1),font=('Calibri (Body)',10,"bold"),fg="gray32")
        d1.place(x=(j*100)+175, y=20)

    k=0
    for i in range(m):
        for j in range(n):
            e = Label(subframe,text=str(resultat[k]),font=('Calibri (Body)',10,"bold"),fg="green",bd=0)
            e.place(x=(j*100)+50+120,y=(i*20)+20+20 )
            k += 1
    def bu():
        level2.destroy()
        import data_entry1
    
    myButton2 = Button(subframe, text="Try Again",bd=0,cursor="hand2",font=('Calibri (Body)',10,"bold"),fg="white",bg="#249794", command=bu)
    myButton2.place(x=(n*100)+175,y=(m*20)+140)
    level2.mainloop()
