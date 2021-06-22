from data_entry2 import Valider
from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import numpy as np

class Entries:
    def __init__(self,root):
        self.root = root
        blank_space ="  "
        self.root.title(80*blank_space+"Data Entry")
        self.root.geometry("1000x350")

        self.left = ImageTk.PhotoImage(file="images/fside.jpg")
        left = Label(self.root,image=self.left).place(x=0,y=0,width=250,height=350)
        
        l1=Label(self.root,text="Transportation Problem using ",fg='white',bg='#249794')
        lst1=('Calibri (Body)',12,'bold')
        l1.configure(font=lst1)
        l1.place(x=0,y=60)

        l2=Label(self.root,text="Simplex Method ",fg='white',bg='#249794')
        lst2=('Calibri',12,'bold')
        l2.configure(font=lst2)
        l2.place(x=46,y=80)

        label1 = Label(self.root, text="Number of sources:",font=('Calibri (Body)',10,"bold"),fg="gray32")
        label1.place(x=300,y=40)
        label2 = Label(self.root, text="Number of destinations:",font=('Calibri (Body)',10,"bold"),fg="gray32")
        label2.place(x=300,y=80)

        x = IntVar()
        e = ttk.Entry(self.root, textvariable=x,justify = CENTER)
        e.place(x=500,y=40)
       
        y = IntVar()
        f = ttk.Entry(self.root, textvariable=y,justify = CENTER)
        f.place(x=500,y=80)
        def bb():
            self.root.destroy()
            Valider(x.get(), y.get())

        myButton1 = Button(self.root, text="Reset",bd=0,cursor="hand2",font=('Calibri (Body)',10,"bold"),fg="white",bg="#249794", command=quit)
        myButton1.place(x=800,y=120)

        myButton2 = Button(self.root, text="Continue",bd=0,cursor="hand2",font=('Calibri (Body)',10,"bold"),fg="white",bg="#249794", command=bb)
        myButton2.place(x=700,y=120)

root = Tk()
obj = Entries(root)
root.mainloop()  

    
      
