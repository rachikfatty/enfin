from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql

class Login:

    def __init__(self,root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")

        #===BgImage===
        self.bg = ImageTk.PhotoImage(file="images/data.jpg")
        bg = Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
        #===side Image===
        self.left = ImageTk.PhotoImage(file="images/fside.jpg")
        left = Label(self.root,image=self.left).place(x=500,y=75,width=480,height=400)

        l1=Label(self.root,text="Hello, Friend!",fg='white',bg='#249794')
        lst1=('Calibri (Body)',18,'bold')
        l1.configure(font=lst1)
        l1.place(x=760,y=185)

        l2=Label(self.root,text="Enter your Personal details",fg='white',bg='#249794')
        lst2=('Calibri',13)
        l2.configure(font=lst2)
        l2.place(x=743,y=240)

        l3=Label(self.root,text=" and start journey with us",fg='white',bg='#249794')
        lst3=('Calibri',13)
        l3.configure(font=lst3)
        l3.place(x=750,y=265)

        #====Login Frame====
        frame1 = Frame(self.root,bg="white")
        frame1.place(x=200,y=75,width=500,height=400)

        #----------TITLE------------------------------------
        title = Label(frame1,text="Sign in ",font=('Calibri (Body)',18,'bold'),bg="white",fg="#249794")
        title.place(x=190,y=30)

        #-----------ROW NUMBER 1----------------------------
        email = Label(frame1,text="Email Adress:",font=("Calibri",16,"bold"),bg="white",fg="grey")
        email.place(x=90,y=100)
        self.txt_email = Entry(frame1,font=("Calibri",10),bg="lightgrey")
        self.txt_email.place(x=90,y=140,width=220,height=25)

        #-------------ROW NUMBER 2---------------------------------------
        passwd = Label(frame1,text="Password:",font=("Calibri",16,"bold"),bg="white",fg="grey")
        passwd.place(x=90,y=180)
        self.txt_passwd = Entry(frame1,font=("Calibri",10),bg="lightgrey")
        self.txt_passwd.place(x=90,y=220,width=220,height=25)

        btn_reg = Button(self.root,text="Register",font=('Calibri (Body)',10,"bold"),command=self.register_window,bg="white",fg='#249794',cursor="hand2",padx=20)
        btn_reg.place(x=788,y=350)
        
        btn_login = Button(frame1,text="Sign In",font=('Calibri (Body)',10,"bold"),bg="white",fg='#249794',cursor="hand2",padx=20,command=self.login)
        btn_login.place(x=130,y=300)

        btn_pass = Button(frame1,text="Forgot Password?",font=('Calibri (Body)',10,"bold"),bd=0,fg="black",bg='white',cursor="hand2")
        btn_pass.place(x=90,y=260)
    def register_window(self):
        self.root.destroy()
        
        
    def login(self):
        if self.txt_email.get()=="" or self.txt_passwd.get()=="" :
            messagebox.showerror("ERROR","All Fields Are Requiered",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="RootUser",database="users")
                cur = con.cursor()
                cur.execute("select * from users where email=%s and passwd=%s",(self.txt_email.get(),self.txt_passwd.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("ERROR","Invalid USERNAME OR PASSWORD",parent=self.root)
                    
                else:
                    messagebox.showinfo("Success","Welcome!",parent=self.root)
                    self.root.destroy()
                    import data_entry1
                con.close()        
                
            except Exception as es:
                messagebox.showerror("ERROR",f"Error Due to: {str(es)}",parent=self.root)        

root = Tk()
obj = Login(root)
root.mainloop()        