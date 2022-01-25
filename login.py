from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import tkinter as tk
import random
import time
import datetime

def main():
    root = Tk()
    app = SalesLogin(root)

class SalesLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Sales Manangment Login System")
        self.master.geometry('1080x500+0+0')
        self.master.config(bg ='cadet blue')
        self.frame = Frame(self.master,bg='cadet blue')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame,text='Sales Management Login System',font=('arial',20,'bold'),
                            bg='cadet Blue',fg='Cornsilk')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=20)
#=====================================================================================================
        self.LoginFrame1 = LabelFrame(self.frame, width=1080,height=300,text='Login',
                            font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=40)
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1080,height=100,text='Log',
                            font=('arial',20,'bold'),relief='ridge',bg='cadet blue',bd=40)
        self.LoginFrame2.grid(row=2,column=0)

#======================================================================================================
        self.lblUsername = Label(self.LoginFrame1,text='Username',font=('arial',20,'bold'),
                            bg='cadet Blue',fg='Cornsilk')
        self.lblUsername.grid(row=0,column=0)
        
        self.txtUsername=Entry(self.LoginFrame1,font=('arial',10,'bold'),bd=7,textvariable=self.Username,width=33)
        self.txtUsername.grid(row=0,column=1,padx=88)
        self.lblPassword = Label(self.LoginFrame1,text='Password',font=('arial',20,'bold'),
                            bg='cadet Blue',fg='Cornsilk')
        self.lblPassword.grid(row=1,column=0)
        
        self.txtPassword=Entry(self.LoginFrame1,font=('arial',10,'bold'),show='*',bd=7,textvariable=self.Password,width=33)
        self.txtPassword.grid(row=1,column=1, columnspan=2,pady=30)

#======================================================================================================
        self.btnLogin = Button(self.LoginFrame2, text='Login',width=15,font=('arial',30,'bold'),bg='cadet Blue',fg='cornsilk',command=self.Login_System)
        self.btnLogin.grid(row=3,column=0,pady=20,padx=8)

        self.btnReset = Button(self.LoginFrame2, text='Reset',width=15,font=('arial',30,'bold'),bg='cadet Blue',fg='cornsilk',command=self.iReset)
        self.btnReset.grid(row=3,column=1,pady=20,padx=8)

        self.btnExit = Button(self.LoginFrame2, text='Exit',width=15,font=('arial',30,'bold'),bg='cadet Blue',fg='cornsilk',command=self.iExit)
        self.btnExit.grid(row=3,column=2,pady=20,padx=8)
#======================================================================================================
    def Login_System(self):
        user=(self.Username.get())
        pas=(self.Password.get())
        if (user == str(1234) and pas == str(5678)):
            self.Login_Window()
        else:
            tkinter.messagebox.askyesno("Sales Manangment Login System","Invalid Login details")
            self.Username.set("")
            self.Password.set("")

    def iReset(self):
        self.Username.set("")
        self.Password.set("")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("sales Login System","Confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
            return

    def Login_Window(self):
        self.SaleWindow = Toplevel(self.master)
        self.app = SalesManagement(self.SaleWindow)




class SalesManagement:
    def __init__(self,master):
        self.master = master
        self.master.title("Sales Manangment Login System")
        self.master.geometry('1080x500+0+0')
        self.master.config(bg='cadet blue')
        self.frame = Frame(self.master,bg='Red')
        self.frame.pack()

#==================================================



#===================================================
root = tk.Tk()
my_gui = SalesLogin(root)
#win.geometry('1080x500')
#win.title('Book store')

root.mainloop()