from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql

class Register:

    def __init__(self,root):
        self.root = root
        self.root.title("Registeration Window")
        self.root.geometry("1350x700+0+0")
         
        #===BgImage===
        self.bg = ImageTk.PhotoImage(file="images/data.jpg")
        bg = Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
        #===side Image===
        self.left = ImageTk.PhotoImage(file="images/fside.jpg")
        left = Label(self.root,image=self.left).place(x=80,y=75,width=550,height=400)
        l1=Label(self.root,text="Welcome Back!",fg='white',bg='#249794')
        lst1=('Calibri (Body)',18,'bold')
        l1.configure(font=lst1)
        l1.place(x=140,y=185)

        l2=Label(self.root,text="To keep connected with us please",fg='white',bg='#249794')
        lst2=('Calibri',13)
        l2.configure(font=lst2)
        l2.place(x=120,y=240)

        l3=Label(self.root,text="login with your personal info",fg='white',bg='#249794')
        lst3=('Calibri',13)
        l3.configure(font=lst3)
        l3.place(x=135,y=265)
        #====Register Frame====
        frame1 = Frame(self.root,bg="white")
        frame1.place(x=400,y=75,width=600,height=400)
        #----------TITLE------------------------------------
        title = Label(frame1,text="Create Account",font=('Calibri (Body)',18,'bold'),bg="white",fg="#249794")
        title.place(x=150,y=30)
        #-----------ROW NUMBER 1----------------------------
        
        f_name = Label(frame1,text="First Name:",font=("Calibri",12,"bold"),bg="white",fg="grey")
        f_name.place(x=50,y=100)
        self.txt_fname = Entry(frame1,font=("Calibri",10),bg="lightgrey")
        self.txt_fname.place(x=50,y=130,width=150)
        
        l_name = Label(frame1,text="Last Name:",font=("Calibri",12,"bold"),bg="white",fg="grey")
        l_name.place(x=250,y=100)
        self.txt_lname = Entry(frame1,font=("Calibri",10),bg="lightgrey")
        self.txt_lname.place(x=250,y=130,width=150)
        #-------------ROW NUMBER 2---------------------------
        email = Label(frame1,text="Email:",font=("Calibri",12,"bold"),bg="white",fg="grey")
        email.place(x=50,y=150)
        self.txt_email = Entry(frame1,font=("Calibri",10),bg="lightgrey")
        self.txt_email.place(x=50,y=180,width=150)
        
        phone = Label(frame1,text="Phone Number:",font=("Calibri",12,"bold"),bg="white",fg="grey")
        phone.place(x=250,y=150)
        self.txt_phone = Entry(frame1,font=("Calibri",10),bg="lightgrey")
        self.txt_phone.place(x=250,y=180,width=150)

        #-------------ROW NUMBER 3------------------------------
        indus = Label(frame1,text="Industry Type:",font=("Calibri",12,"bold"),bg="white",fg="grey")
        indus.place(x=50,y=200)
        self.txt_indus =ttk.Combobox(frame1,font=("Calibri",8),state='readonly',justify=CENTER)
        self.txt_indus['values']=("Please Select","Transportation/Distribution","Consumer Goods","Manufacturing","Agriculture","Banking","Other")
        self.txt_indus.place(x=50,y=230,width=150)
        self.txt_indus.current() 

        
        user = Label(frame1,text="User Type:",font=("Calibri",12,"bold"),bg="white",fg="grey")
        user.place(x=250,y=200)
        self.txt_user = ttk.Combobox(frame1,font=("Calibri",8),state='readonly',justify=CENTER)
        self.txt_user['values']=("Please Select","Commercial User","Consultant","Corporate Developer","Professor","Student","Other")
        self.txt_user.place(x=250,y=230,width=150)
        self.txt_user.current()

        #-------------ROW NUMBER 4---------------------------------------
        passwd = Label(frame1,text="Password:",font=("Calibri",12,"bold"),bg="white",fg="grey")
        passwd.place(x=50,y=250)
        self.txt_passwd = Entry(frame1,font=("Calibri",10),bg="lightgrey")
        self.txt_passwd.place(x=50,y=280,width=150)
        
        confpass = Label(frame1,text="Confirm Password:",font=("Calibri",12,"bold"),bg="white",fg="grey")
        confpass.place(x=250,y=250)
        self.txt_confpass = Entry(frame1,font=("Calibri",10),bg="lightgrey")
        self.txt_confpass.place(x=250,y=280,width=150)

        #----------------Terms------------------
        self.var_chk=IntVar()
        chk = Checkbutton(frame1,text="I Agree To The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("Calibri",10))
        chk.place(x=50,y=310)

        btn = Button(frame1,text="Register",font=('Calibri (Body)',10,"bold"),bg="white",fg='#249794',cursor="hand2",padx=20,command=self.register_data)
        btn.place(x=182,y=340)
    
        btn_login = Button(self.root,text="Sign In",font=('Calibri (Body)',10,"bold"),command=self.login_window,bg="white",fg='#249794',cursor="hand2",padx=20)
        btn_login.place(x=185,y=350)
        self.root.attributes("-topmost", True)
    def login_window(self):
        self.root.destroy()
        import log

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_email.get()=="" or self.txt_phone.get()=="" or self.txt_indus.get()=="Please Select" or self.txt_user.get()=="Please Select" or self.txt_passwd.get()=="" or self.txt_confpass.get()=="" :
            messagebox.showerror("ERROR","All fields are required !",parent=self.root)
        elif self.txt_passwd.get()!=self.txt_confpass.get():
            messagebox.showerror("ERROR","Password and Confirm Password should be the same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("ERROR","You Should Agree to Our Terms & Conditions",parent=self.root)
        else:
            try:
                con= pymysql.connect(host="localhost",user="root",password="RootUser",database="users")
                cur = con.cursor()
                cur.execute("select * from users where email=%s",self.txt_email.get())
                row = cur.fetchone()
                print(row)
                if row != None:
                    messagebox.showerror("ERROR","Email already used !!, Please try wit another email ",parent=self.root)
                else:
                    cur.execute("insert into Users (f_name,l_name,email,phone,indus,user,passwd) values(%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_fname.get(),
                            self.txt_lname.get(),
                            self.txt_email.get(),
                            self.txt_phone.get(),
                            self.txt_indus.get(),
                            self.txt_user.get(),
                            self.txt_passwd.get()
                            ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Sucess","Register Successful",parent=self.root)
            except Exception as es:
                messagebox.showerror("ERROR",f"Error due to: {str(es)}",parent=self.root)

root = Tk()
obj = Register(root)
root.mainloop()      
