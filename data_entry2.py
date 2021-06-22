import numpy as np
from tkinter import *
from calculSimplex import calculSimplex
from tkinter import ttk,messagebox


def Valider(a,b):
    b1=b
    level1 = Tk()
    level1.geometry("1100x350")
    blank_space ="  "
    level1.title(80*blank_space+"Data Entry")
    frame1 = Frame(level1,width=2000,height=700,relief="sunken")
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
    level1.update_idletasks() # update geometry
    canvas.config(scrollregion = canvas.bbox("all"))
    canvas.xview_moveto(0) 
    canvas.yview_moveto(0)

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
        s1 = Label(subframe, text="S" + str(i + 1),font=('Calibri (Body)',10,"bold"),fg="gray32")
        s1.place(x=50, y=(i*20)+40)

    for j in range(b):
        d1 = Label(subframe, text="D" + str(j + 1),font=('Calibri (Body)',10,"bold"),fg="gray32")
        d1.place(x=(j*100)+175, y=20)
    
    dispo = Label(subframe, text="Demand",font=('Calibri (Body)',10,"bold"),fg="gray32")
    dispo.place(x=29, y=(a*20) + 48)

    demand = Label(subframe, text="Supply",font=('Calibri (Body)',10,"bold"),fg="gray32")
    demand.place(x=(b*100)+200,y=20)

    c_temp = []
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            entry =ttk.Entry(subframe,justify = CENTER)
            entry.place(x=(j*100)+50,y=(i*20)+20)
            c_temp.append(entry)
    
    # Deamnd
    b_eq_temp = []
    for i in range(1, b + 1):
        entry = ttk.Entry(subframe,justify = CENTER)
        entry.place(x=(i*100)+50, y=(a*20) + 48)
        b_eq_temp.append(entry)
    
    # Supply
    b_ub_temp = []
    for i in range(1, a + 1):
        entry = ttk.Entry(subframe,justify = CENTER)
        entry.place(x=(b*100)+200,y=(i*20)+20)
        b_ub_temp.append(entry)

    
    def get_cost():    
        entry_list1 = []
        for entries in c_temp:
            entry_list1.append(int(entries.get()))
        c1 = np.array([entry_list1])
        return c1

    def get_b_eq():
        entry_list2 = []
        for entries in b_eq_temp:
            entry_list2.append(entries.get())
        b_eq1 = np.array([entry_list2]).transpose()
        return b_eq1

    def get_b_ub():
        entry_list3 = []
        for entries in b_ub_temp:
            entry_list3.append(entries.get())
        b_ub1 = np.array([entry_list3]).transpose()    
        return b_ub1

    def get_All_Entries():
        c = get_cost()
        b_eq = get_b_eq()
        b_ub = get_b_ub()
        total_2=0
        for q in b_eq:
            total_2 = total_2 + int(q)

        total_1=0
        for b in b_ub:
            total_1 = total_1 + int(b)
        
        if int(total_2) >= int(total_1) :
            messagebox.showerror("ERROR","Supply must be greater than demand !",parent=level1)    
        else:  
            level1.destroy()
            calculSimplex(a,b1,c,b_ub,b_eq)    
            
    ValButt = Button(subframe, text="Continue", command=get_All_Entries,bd=0,cursor="hand2",font=('Calibri (Body)',10,"bold"),fg="white",bg="#249794")
    ValButt.place(x=(b*100)+400, y=(a*20)+48+40)
    def back():
        level1.destroy()
        import data_entry1

    myButton1 = Button(subframe, text="Back",bd=0,cursor="hand2",font=('Calibri (Body)',10,"bold"),fg="white",bg="#249794", command=back )
    myButton1.place(x=(b*100)+300,y=(a*20)+48+40)

    level1.mainloop()   
