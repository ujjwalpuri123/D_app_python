from tkinter import *
import tkinter as tk
import time 
from tkinter import messagebox

import tkinter.messagebox
from tkinter import ttk

#import 15th

localtime=time.asctime(time.localtime(time.time()))
#=================================================

#=================================================
class App1:  
    def __init__(self,top):
        self.top = top
        top.title("Book store")
        top.geometry("1080x500")
        top.configure(background="#091833")

        font11="{U.S. 101} 20 bold"
        font12="{times new roman} 18 bold"
        font10="{courier New} 10 normal"
        font13="{courier New} 14 bold"

        self.Label1 = tk.Label(master=top, text='Pharmacy Management System',font=font11,background='#091833',foreground='#903838')
        self.Label1.place(relx=0.268,rely=0.02,height=51,width=507)
        self.Label12=tk.Label(master=top,text='created by:',foreground='white',font=font10,background='#091833')
        self.Label12.place(relx=0.85,rely=0.86)

        self.Label12=tk.Label(master=top,text='Ujjwal Raj Puri',foreground='white',font=font10,background='#091833')
        self.Label12.place(relx=0.85,rely=0.90)


        localtime1 = Label(master=top,background='#091833',text=localtime,font='{Segoe UI} 13 bold',fg='steel blue')
        localtime1.place(relx=0.420,rely=0.12)

        self.Label12=tk.Label(master=top,text='Username :',foreground='white',font=font12,background='#091833')
        self.Label12.place(relx=0.286,rely=0.41)
        self.Label12=tk.Label(master=top,text='Password :',foreground='white',font=font12,background='#091833')
        self.Label12.place(relx=0.286,rely=0.51)


        self.entry1=tk.Entry(master=top,background='#d9d9d9',foreground='#c60000',selectbackground='#f24445',font=font10)
        self.entry1.place(relx=0.4,rely=0.41,height=35,width=250)

        self.entry1=tk.Entry(master=top,background='#d9d9d9',foreground='#c60000',selectbackground='#f24445',font=font10)
        self.entry1.place(relx=0.4,rely=0.51,height=35,width=250)

        self.Button2 = tk.Button(master=top,text=' Login ',background='#e16740',font=font13)
        self.Button2.place(relx=0.31,rely=0.61,width=100)
        self.Button2 = tk.Button(master=top,text=' Reset ',background='#e16740',font=font13)
        self.Button2.place(relx=0.425,rely=0.61,width=100)
        self.Button2 = tk.Button(master=top,text=' Exit ',background='#e16740',font=font13)
        self.Button2.place(relx=0.54,rely=0.61,width=100)

#=====================================================

#======================================================================


root = tk.Tk()
my_gui = App1(root)
#win.geometry('1080x500')
#win.title('Book store')

root.mainloop()