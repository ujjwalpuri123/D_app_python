from tkinter import *
import tkinter as tk
import time 
from tkinter import messagebox
#import 15th

localtime=time.asctime(time.localtime(time.time()))

class App1:  
    def __init__(self,top):
        self.top = top
        top.title("Book store")
        top.geometry("1080x500")
        top.configure(background="#091833")

        font10="{courier New} 10 normal"
        font11="{U.S. 101} 30 bold"
        font12="{times new roman} 18 bold"
        font13="{courier New} 14 bold"

        self.Label1 = tk.Label(master=top, text='Namaste Stationary Store',font=font11,background='#091833',foreground='#903838')
        self.Label1.place(relx=0.268,rely=0.02,height=51,width=507)

        localtime1 = Label(master=top,background='#091833',text=localtime,font='{Segoe UI} 13 bold',fg='steel blue')
        localtime1.place(relx=0.420,rely=0.12)

        self.Label12=tk.Label(master=top,text='Title :',foreground='white',font=font12,background='#091833')
        self.Label12.place(relx=0.054,rely=0.25)
        self.Label12=tk.Label(master=top,text='Year :',foreground='white',font=font12,background='#091833')
        self.Label12.place(relx=0.044,rely=0.32)
        self.Label12=tk.Label(master=top,text='Auther :',foreground='white',font=font12,background='#091833')
        self.Label12.place(relx=0.286,rely=0.24)
        self.Label12=tk.Label(master=top,text='Price($):',foreground='white',font=font12,background='#091833')
        self.Label12.place(relx=0.28,rely=0.32)
        self.Label12=tk.Label(master=top,text='created by:',foreground='white',font=font10,background='#091833')
        self.Label12.place(relx=0.85,rely=0.86)
        self.Label12=tk.Label(master=top,text='Ujjwal Raj Puri',foreground='white',font=font10,background='#091833')
        self.Label12.place(relx=0.85,rely=0.90)

        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f24445",font=font10)
        self.entry1.place(relx=0.119,rely=0.26)
        self.entry1=tk.Entry(master=top,foreground='#c60000',background='#d9d9d9',selectbackground='#f24445',font=font10)
        self.entry1.place(relx=0.385,rely=0.26)
        self.entry1=tk.Entry(master=top,background='#d9d9d9',foreground='#c60000',selectbackground='#f24445',font=font10)
        self.entry1.place(relx=0.119,rely=0.33)
        self.entry1=tk.Entry(master=top,background='#d9d9d9',foreground='#c60000',selectbackground='#f24445',font=font10)
        self.entry1.place(relx=0.385,rely=0.33)
#listbox
        self.list1=tk.Listbox(master=top,height=10,width=79)
        self.list1.place(relx=0.09,rely=0.62)

#calculator
        self.entry1=tk.Entry(master=top,background='#d9d9d9',foreground='#c60000',selectbackground='#f24445',font=font10)
        self.entry1.place(relx=0.704,rely=0.26,height=35,width=250)

        self.Button1 = tk.Button(master=top,text='''7''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.35,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''8''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.769,rely=0.35,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''9''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.836,rely=0.35,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''4''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.45,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''5''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.769,rely=0.45,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''6''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.836,rely=0.45,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''1''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.55,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''2''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.769,rely=0.55,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''3''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.836,rely=0.55,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''/''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.895,rely=0.35,height=34,width=37)
        self.Button1 = tk.Button(master=top,text='''*''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.895,rely=0.45,height=34,width=37)
        self.Button1 = tk.Button(master=top,text='''-''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.895,rely=0.55,height=34,width=37)
        self.Button1 = tk.Button(master=top,text='''C''',background='red',font=font12,borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.65,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''0''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.769,rely=0.65,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''.''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.836,rely=0.65,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''+''',background='navy blue',font=font12,borderwidth='0')
        self.Button1.place(relx=0.895,rely=0.65,height=34,width=37)
        self.Button1 = tk.Button(master=top,text='''=''',background='pink',font=font12,borderwidth='0')
        self.Button1.place(relx=0.705,rely=0.75,height=34,width=247)

#button control
        self.Button2 = tk.Button(master=top,text='View all ',background='#e16740',font=font13)
        self.Button2.place(relx=0.09,rely=0.41)
        self.Button2 = tk.Button(master=top,text='Delete selected',background='#e16740',font=font13)
        self.Button2.place(relx=0.21,rely=0.41)
        self.Button2 = tk.Button(master=top,text='Search entry',background='#e16740',font=font13)
        self.Button2.place(relx=0.4,rely=0.41)
        self.Button2 = tk.Button(master=top,text='Add entry',background='#e16740',font=font13)
        self.Button2.place(relx=0.09,rely=0.51)
        self.Button2 = tk.Button(master=top,text='Update selected',background='#e16740',font=font13)
        self.Button2.place(relx=0.21,rely=0.51)
        self.Button2 = tk.Button(master=top,text='   Close    ',background='#e16740',font=font13)
        self.Button2.place(relx=0.4,rely=0.51)


root = tk.Tk()
my_gui = App1(root)
#win.geometry('1080x500')
#win.title('Book store')

root.mainloop()