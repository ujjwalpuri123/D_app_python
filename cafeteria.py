from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time

class Online_billing:
    def __init__(self, root):
        self.root=root
        self.root.title("online Billing System")
        self.root.geometry("1350x7500+0+0")
        self.root.config(background="Navy blue")

        MainFrame = Frame(self.root,bg="Navy blue",bd=20,relief=RIDGE)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame,bd=14,width=1350,height=100,padx=10,relief=RIDGE,bg="Cadet blue")
        TitleFrame.grid(row=0,column=0,columnspan=4,sticky=W)

        CustomersFrame = Frame(MainFrame,bd=14,width=450,height=488,padx=10,relief=RIDGE,bg="Cadet blue")
        CustomersFrame.grid(row=1,column=0,sticky=W)

        FoodItemFrame = Frame(MainFrame,bd=14,width=450,height=488,padx=10,relief=RIDGE,bg="Cadet blue")
        FoodItemFrame.grid(row=1,column=1,sticky=W)

        BaseFrames = Frame(MainFrame,bd=14,width=460,height=399,padx=8,relief=RIDGE,bg="Cadet blue")
        BaseFrames.grid(row=1,column=2,sticky=W)

        NoteBookFrames = Frame(BaseFrames,bd=14,width=388,height=340,padx=10,relief=RIDGE,bg="Cadet blue")
        NoteBookFrames.grid(row=0,column=0,sticky=W)

        ButtonsFrames = Frame(BaseFrames,bd=14,width=388,height=120,padx=10,relief=RIDGE,bg="blue")
        ButtonsFrames.grid(row=1,column=0,columnspan=4,sticky=W)

        Date1 = StringVar()
        Time1=StringVar()
        Date1.set(time.strftime("%d/%m/%y"))
        Time1.set(time.strftime("%H:%M:%S"))


        CustomerRef =StringVar()
        Firstname =StringVar()
        Surname =StringVar()
        Address=StringVar()
        PostalCode=StringVar()
        Mobile=StringVar()
        Email=StringVar()
        Nationality=StringVar()
        DateofBirth=StringVar()
        IDType=StringVar()
        Gender=StringVar()
        CheckInDate=StringVar()
        CheckOutDate=StringVar()
        Meal=StringVar()
        RoomType=StringVar()
        RoomNo=StringVar()
        RoomExtNo=StringVar()
        TotalCost=StringVar()
        SubTotal=StringVar()
        PaidTax=StringVar()


        text_Input = StringVar()
        global operator
        operator = ""


        CustomerRef.set(random.randint(19800, 987654))

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()

        E_Latta=StringVar()
        E_Espresso=StringVar()
        E_Espress=StringVar()
        E_spresso=StringVar()
        E_Epresso=StringVar()
        E_Esesso=StringVar()
        E_Esprsso=StringVar()
        E_Espreso=StringVar()

        E_Latta.set("0")
        E_Espresso.set("0")
        E_Espress.set("0")
        E_spresso.set("0")
        E_Epresso.set("0")
        E_Esesso.set("0")
        E_Esprsso.set("0")
        E_Espreso.set("0")






        self.lblTitle =Label(TitleFrame, textvariable=Date1,bg='cadetblue',font=('arial',30,'bold'),pady=9,bd=5).grid(row=0,column=0)

        self.lblTitle=Label(TitleFrame,text="\t BhetGhat Cafe\t\t",bg='cadetblue',font=('arial',30,'bold') ,pady=9,bd=5,justify=CENTER).grid(row=0,column=1)
        
        self.lblTitle=Label(TitleFrame,textvariable=Time1,bg='cadetblue',font=('arial',30,'bold'),pady=9,bd=5).grid(row=0,column=2)




        self.btnTotal = Button(ButtonsFrames, padx=16, pady=7, bd=5, fg="black", font=('arial',16,'bold'), width=4,height=1,
                            bg="green",text="Total").grid(row=0,column=0)

        self.btnReset = Button(ButtonsFrames, padx=16, pady=7, bd=5, fg="black", font=('arial',16,'bold'), width=4,height=1,
                            bg="green",text="Reset").grid(row=0,column=1)

        self.btnExit = Button(ButtonsFrames, padx=16, pady=7, bd=5, fg="black", font=('arial',16,'bold'), width=4,height=1,
                            bg="green",text="Exit").grid(row=0,column=2)





if __name__=='__main__':
    root = Tk()
    application=Online_billing(root)
    root.mainloop()