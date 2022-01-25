from tkinter import *
import tkinter as tk
import time 
from tkinter import messagebox

import tkinter.messagebox
from tkinter import ttk
import a15th
#import 15th

localtime=time.asctime(time.localtime(time.time()))
#=================================================
def main():
    root = Tk()
    app = App1(root)

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


        self.Username = StringVar()
        self.Password = StringVar()



        self.Label1 = tk.Label(master=top, text='Namaste Stationary Store',font=font11,background='#091833',foreground='#903838')
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


        self.entry1=tk.Entry(master=top,background='#d9d9d9',foreground='#c60000',selectbackground='#f24445',textvariable=self.Username,font=font10)
        self.entry1.place(relx=0.4,rely=0.41,height=35,width=250)

        self.entry1=tk.Entry(master=top,background='#d9d9d9',foreground='#c60000',selectbackground='#f24445',textvariable=self.Password,font=font10)
        self.entry1.place(relx=0.4,rely=0.51,height=35,width=250)

        self.Button2 = tk.Button(master=top,text=' Login ',background='#e16740',font=font13,command=self.Login_System)
        self.Button2.place(relx=0.31,rely=0.61,width=100)
        self.Button2 = tk.Button(master=top,text=' Reset ',background='#e16740',font=font13,command=self.iReset)
        self.Button2.place(relx=0.425,rely=0.61,width=100)
        self.Button2 = tk.Button(master=top,text=' Exit ',background='#e16740',font=font13)
        self.Button2.place(relx=0.54,rely=0.61,width=100)



#==========================================================
    def Login_System(self):
        user=(self.Username.get())
        pas=(self.Password.get())
        if (user == str(1234) and pas == str(5678)):
            self.Login_Window()
        else:
            tkinter.messagebox.askyesno("Book store","Invalid Login details")
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
        self.SaleWindow = Toplevel(self.top)
        self.app = App2(self.SaleWindow)



#==========================================================
class App2:  
    def __init__(self,top):
        self.top = top
        

        top.title("Book store")
        top.geometry("1080x500")
        top.configure(background="#091833")

        font10="{courier New} 10 normal"
        font11="{U.S. 101} 30 bold"
        font12="{times new roman} 18 bold"
        font13="{courier New} 14 bold"

#        operator=""
        def btnClick(numbers):
                current = self.entry0.get()
                self.entry0.delete(0,END)
                self.entry0.insert(0,str(current)+str(numbers))
#                 global operator
#                operator=operator + str(numbers)
#                text_Input.set(operator)
#                return
        def btnClear():
                self.entry0.delete(0,END)

        def btnAdd():
                first_number = self.entry0.get()
                global f_num
                global math
                math = "addition"
                f_num = float(first_number)
                self.entry0.delete(0,END)

        def btnSubstract():
                first_number = self.entry0.get()
                global f_num
                global math
                math = "substraction"
                f_num = float(first_number)
                self.entry0.delete(0,END)

        def btnMultiply():
                first_number = self.entry0.get()
                global f_num
                global math
                math = "multiplication"
                f_num = float(first_number)
                self.entry0.delete(0,END)

        def btnDivide():
                first_number = self.entry0.get()
                global f_num
                global math
                math = "division"
                f_num = float(first_number)
                self.entry0.delete(0,END)


        def btnEqual():
                second_number = self.entry0.get()
                self.entry0.delete(0,END)
                
                if math == "addition":
                        self.entry0.insert(0,f_num + float(second_number))
                if math == "substraction":
                        self.entry0.insert(0,f_num - float(second_number))
                if math == "multiplication":
                        self.entry0.insert(0,f_num * float(second_number))
                if math == "division":
                        self.entry0.insert(0,f_num / float(second_number))


        def view_command():
                self.list1.delete(0,END)
                for row in a15th.view():
                        self.list1.insert(END,row)

        def search_command():
                self.list1.delete(0,END)
                for row in a15th.search(title_text.get(),auther_text.get(),year_text.get(),price_text.get()):
                        self.list1.insert(END,row)

        def add_command():
                a15th.insert(title_text.get(),auther_text.get(),year_text.get(),price_text.get())
                self.list1.delete(0,END)
                self.list1.insert(END,(title_text.get(),auther_text.get(),year_text.get(),price_text.get()))

        def get_selected_rows(event):
                global selected_tuple
                index=self.list1.curselection()[0]
                selected_tuple=self.list1.get(index)
#                print (selected_tuple)
                self.entry1.delete(0,END)
                self.entry1.insert(END,selected_tuple[1])
                self.entry2.delete(0,END)
                self.entry2.insert(END,selected_tuple[2])
                self.entry3.delete(0,END)
                self.entry3.insert(END,selected_tuple[3])
                self.entry4.delete(0,END)
                self.entry4.insert(END,selected_tuple[4])



        def delete_command():
                a15th.delete(selected_tuple[0])

        def update_command():
                a15th.update(selected_tuple[0],title_text.get(),auther_text.get(),year_text.get(),price_text.get())
             #   print(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])




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

        title_text=StringVar()
        self.entry1=tk.Entry(master=top,background="#d9d9d9",foreground="#c60000",selectbackground="#f24445",font=font10,textvariable=title_text)
        self.entry1.place(relx=0.119,rely=0.26)
        auther_text=StringVar()
        self.entry2=tk.Entry(master=top,foreground='#c60000',background='#d9d9d9',selectbackground='#f24445',font=font10,textvariable=auther_text)
        self.entry2.place(relx=0.385,rely=0.26)
        year_text=StringVar()
        self.entry3=tk.Entry(master=top,background='#d9d9d9',foreground='#c60000',selectbackground='#f24445',font=font10,textvariable=year_text)
        self.entry3.place(relx=0.119,rely=0.33)
        price_text=StringVar()
        self.entry4=tk.Entry(master=top,background='#d9d9d9',foreground='#c60000',selectbackground='#f24445',font=font10,textvariable=price_text)
        self.entry4.place(relx=0.385,rely=0.33)
#listbox
        self.list1=tk.Listbox(master=top,height=10,width=79)
        self.list1.place(relx=0.09,rely=0.62)
        self.list1.bind('<<ListboxSelect>>',get_selected_rows)


#calculator
        self.entry0=tk.Entry(master=top,background='powder blue',foreground='#c60000',selectbackground='#f24445',font=font12)
        self.entry0.place(relx=0.704,rely=0.26,height=35,width=250)

        self.Button1 = tk.Button(master=top,text='''7''',background='navy blue',font=font12,borderwidth='0',command=lambda: btnClick(7))
        self.Button1.place(relx=0.705,rely=0.35,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''8''',background='navy blue',font=font12,borderwidth='0',command=lambda: btnClick(8))
        self.Button1.place(relx=0.769,rely=0.35,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''9''',background='navy blue',font=font12,borderwidth='0',command=lambda: btnClick(9))
        self.Button1.place(relx=0.836,rely=0.35,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''4''',background='navy blue',font=font12,borderwidth='0',command=lambda: btnClick(4))
        self.Button1.place(relx=0.705,rely=0.45,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''5''',background='navy blue',font=font12,borderwidth='0',command=lambda: btnClick(5))
        self.Button1.place(relx=0.769,rely=0.45,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''6''',background='navy blue',font=font12,borderwidth='0',command=lambda: btnClick(6))
        self.Button1.place(relx=0.836,rely=0.45,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''1''',background='navy blue',font=font12,borderwidth='0',command=lambda: btnClick(1))
        self.Button1.place(relx=0.705,rely=0.55,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''2''',background='navy blue',font=font12,borderwidth='0',command=lambda: btnClick(2))
        self.Button1.place(relx=0.769,rely=0.55,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''3''',background='navy blue',font=font12,borderwidth='0',command=lambda: btnClick(3))
        self.Button1.place(relx=0.836,rely=0.55,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''/''',background='navy blue',font=font12,borderwidth='0',command=btnDivide)
        self.Button1.place(relx=0.895,rely=0.35,height=34,width=37)
        self.Button1 = tk.Button(master=top,text='''*''',background='navy blue',font=font12,borderwidth='0',command=btnMultiply)
        self.Button1.place(relx=0.895,rely=0.45,height=34,width=37)
        self.Button1 = tk.Button(master=top,text='''-''',background='navy blue',font=font12,borderwidth='0',command=btnSubstract)
        self.Button1.place(relx=0.895,rely=0.55,height=34,width=37)
        self.Button1 = tk.Button(master=top,text='''C''',background='red',font=font12,borderwidth='0',command=btnClear)
        self.Button1.place(relx=0.705,rely=0.65,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''0''',background='navy blue',font=font12,borderwidth='0',command=lambda: btnClick(0))
        self.Button1.place(relx=0.769,rely=0.65,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''.''',background='navy blue',font=font12,borderwidth='0',command=lambda: btnClick("."))
        self.Button1.place(relx=0.836,rely=0.65,height=34,width=57)
        self.Button1 = tk.Button(master=top,text='''+''',background='navy blue',font=font12,borderwidth='0',command=btnAdd)
        self.Button1.place(relx=0.895,rely=0.65,height=34,width=37)
        self.Button1 = tk.Button(master=top,text='''=''',background='pink',font=font12,borderwidth='0',command=btnEqual)
        self.Button1.place(relx=0.705,rely=0.75,height=34,width=247)

#button control
        self.Button2 = tk.Button(master=top,text='View all ',background='#e16740',font=font13,command=view_command)
        self.Button2.place(relx=0.09,rely=0.41)
        self.Button2 = tk.Button(master=top,text='Delete selected',background='#e16740',font=font13,command=delete_command)
        self.Button2.place(relx=0.21,rely=0.41)
        self.Button2 = tk.Button(master=top,text='Search entry',background='#e16740',font=font13,command=search_command)
        self.Button2.place(relx=0.4,rely=0.41)
        self.Button2 = tk.Button(master=top,text='Add entry',background='#e16740',font=font13,command=add_command)
        self.Button2.place(relx=0.09,rely=0.51)
        self.Button2 = tk.Button(master=top,text='Update selected',background='#e16740',font=font13,command=update_command)
        self.Button2.place(relx=0.21,rely=0.51)
        self.Button2 = tk.Button(master=top,text='   Close    ',background='#e16740',font=font13,command=root.destroy)
        self.Button2.place(relx=0.4,rely=0.51)

#======================================================================


root = tk.Tk()
my_gui = App1(root)
#win.geometry('1080x500')
#win.title('Book store')

root.mainloop()