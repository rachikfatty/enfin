from tkinter import *
from tkinter import ttk  
from tkinter.ttk import Progressbar
from front_end import main_window
r = Tk()
#r.geometry('427x250')

width_of_window = 427
height_of_window = 250
screen_width = r.winfo_screenwidth()
screen_height = r.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
r.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))
r.overrideredirect(1)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar",foreground='red',background='#4f4f4f')
progress = Progressbar(r,style="red.Horizontal.TProgressbar", orient=HORIZONTAL,length=500,mode='determinate')


def bar():
    l4 = Label(r,text='Loading...',fg='white',bg='#249794')
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=0,y=210)

    import time    
    t=0
    for i in range(100):
        progress['value']=t
        r.update_idletasks()
        time.sleep(0.03)
        t=t+1
    r.destroy()
    main_window()

progress.place(x=-10,y=235)

#adding frame
Frame(r,width=247,height=241,bg='#249794').place(x=0,y=0)
b1 = Button(r,width=10,height=1,text="Get Started",command=bar,border=0,fg='#249794')
b1.place(x=170,y=200)

#labels
l1=Label(r,text="SPLASH",fg='white',bg='#249794')
lst1=('Calibri (Body)',18,'bold')
l1.configure(font=lst1)
l1.place(x=50,y=80)

l2=Label(r,text="SCREEN",fg='white',bg='#249794')
lst2=('Calibri (Body)',18)
l2.configure(font=lst2)
l2.place(x=155,y=82)

l3=Label(r,text="BITCH",fg='white',bg='#249794')
lst3=('Calibri (Body)',13)
l3.configure(font=lst3)
l3.place(x=50,y=110)

r.mainloop()