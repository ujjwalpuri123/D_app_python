from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time

class Customer:
    def __init__(self,root):
        self.root = root
        self.root.title("Customer Billing System")
        self.root.geometry("1350x750+0+0")
        self.root.config(backgroun="cadetblue")

        ABC = Frame(self.root, bg='cadetblue',bd=20,relief=RIDGE)
        ABC.grid()
        ABC1 = Frame(ABC,bd=14,width=1320,padx=10,bg='cadetblue',height=100,relief=RIDGE)
        ABC1.grid(row=0, column=0,columnspan=4,sticky=W)
        ABC2 = Frame(ABC,bd=14,width=450,padx=10,bg='cadetblue',height=488,relief=RIDGE)
        ABC2.grid(row=1, column=0,sticky=W)
        ABC3 = Frame(ABC,bd=14,width=450,padx=10,bg='cadetblue',height=488,relief=RIDGE)
        ABC3.grid(row=1, column=1,sticky=W)
        ABC4 = Frame(ABC,bd=14,width=460,padx=10,bg='cadetblue',height=488,relief=RIDGE)
        ABC4.grid(row=1, column=2,sticky=W)
        ABC5 = Frame(ABC4,bd=14,width=370,padx=10,bg='cadetblue',height=340,relief=RIDGE)
        ABC5.grid(row=0, column=0,sticky=W)
        ABC6 = Frame(ABC4,bd=14,width=370,padx=10,bg='cadetblue',height=120,relief=RIDGE)
        ABC6.grid(row=1, column=0,columnspan=4,sticky=W)
        

        Date1 =StringVar()
        Time1 =StringVar()
        Date1.set(time.strftime("%d/%m/%Y"))
        Time1.set(time.strftime("%H:%M:%S"))

        self.lblTitle = Label(ABC1,textvariable=Time1,font=('arial',30,'bold'),pady=9,bd=5,bg='cadetblue',fg="lightgreen").grid(row=0,column=0)
        self.lblTitle = Label(ABC1,text='\tAvinash Cafe\t\t\t',font=('arial',30,'bold'),pady=9,bd=5,bg='cadetblue',fg="lightgreen",justify=CENTER).grid(row=0,column=1)
        self.lblTitle = Label(ABC1,textvariable=Date1,font=('arial',30,'bold'),pady=9,bd=5,bg='cadetblue',fg="lightgreen").grid(row=0,column=2)






        def iExit():
            iExit = tkinter.messagebox.askyesno("Customer Billing System","confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        

        def Reset():
            self.txtReceipt.delete("1.0",END)
            E_Momo.set("0")
            E_Chowmin.set("0")
            E_Omlet.set("0")
            E_BlackTea.set("0")
            E_MilkTea.set("0")
            E_KhajaSet.set("0")
            E_VegKhana.set("0")
            E_ChikenKhana.set("0")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)


        self.txtReceipt =Text(ABC5,height=19,width=43,bd=10,font=('arial',9,'bold')).grid(row=0,column=0)





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
        TotalDays=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        var10=IntVar()
        var11=IntVar()
        var12=IntVar()
        var13=IntVar()
        var14=IntVar()
        var15=IntVar()
        var16=IntVar()


        E_Momo=StringVar()
        E_Chowmin=StringVar()
        E_Omlet=StringVar()
        E_BlackTea=StringVar()
        E_MilkTea=StringVar()
        E_KhajaSet=StringVar()
        E_VegKhana=StringVar()
        E_ChikenKhana=StringVar()

        E_Momo.set("0")
        E_Chowmin.set("0")
        E_Omlet.set("0")
        E_BlackTea.set("0")
        E_MilkTea.set("0")
        E_KhajaSet.set("0")
        E_VegKhana.set("0")
        E_ChikenKhana.set("0")

        





        self.lblCus_Ref=Label(ABC2,font=('arial',12,'bold'),text="Customer Ref:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=0,column=0,sticky=W)
        self.txtCus_Ref=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=CustomerRef,).grid(row=0,column=1, padx=20, pady=3)

        self.lblFirstname=Label(ABC2,font=('arial',12,'bold'),text="Firstname:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=1,column=0,sticky=W)
        self.txtFirstname=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=Firstname).grid(row=1,column=1, padx=20,pady=3)

        self.lblSurname=Label(ABC2,font=('arial',12,'bold'),text="Surname:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=2,column=0,sticky=W)
        self.lblSurname=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=Surname).grid(row=2,column=1, padx=20,pady=3)

        self.lblAddress=Label(ABC2,font=('arial',12,'bold'),text="Address:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=3,column=0,sticky=W)
        self.txtAddress=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=Address).grid(row=3,column=1, padx=20,pady=3)

        self.lblPostalCode=Label(ABC2,font=('arial',12,'bold'),text="PostalCode:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=4,column=0,sticky=W)
        self.txtPostalCode=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=PostalCode).grid(row=4,column=1, padx=20,pady=3)
        self.lblMobile=Label(ABC2,font=('arial',12,'bold'),text="Mobile:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=5,column=0,sticky=W)
        self.txtMobile=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=Mobile).grid(row=5,column=1, padx=20,pady=3)
        self.lblEmail=Label(ABC2,font=('arial',12,'bold'),text="Email:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=Email).grid(row=6,column=1, padx=20,pady=3)
        self.lblNationality=Label(ABC2,font=('arial',12,'bold'),text="Nationality:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=7,column=0,sticky=W)
        self.txtNationality=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=Nationality).grid(row=7,column=1, padx=20,pady=3)
        self.lblDateofBirth=Label(ABC2,font=('arial',12,'bold'),text="DateofBirth:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=8,column=0,sticky=W)
        self.txtDateofBirth=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=DateofBirth).grid(row=8,column=1, padx=20,pady=3)
        self.lblIDType=Label(ABC2,font=('arial',12,'bold'),text="IDType:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=9,column=0,sticky=W)
        self.cboIDType=ttk.Combobox(ABC2,font=('arial',12,'bold'),textvariable=IDType,width=18,state='readonly')
        self.cboIDType['value']=('','Driving License','Student ID','Passport')
        self.cboIDType.current(0)
        self.cboIDType.grid(row=9,column=1,pady=3,padx=20)
        '''
        self.txtIDType=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=IDType).grid(row=9,column=1, padx=20,pady=3)
        '''
        self.lblGender=Label(ABC2,font=('arial',12,'bold'),text="Gender:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=10,column=0,sticky=W)
        self.cboGender=ttk.Combobox(ABC2,font=('arial',12,'bold'),width=18,textvariable=Gender,state='readonly')
        self.cboGender['value']=('','Male','Female','Other')
        self.cboGender.current(0)
        self.cboGender.grid(row=10,column=1,padx=20,pady=3)
        '''
        self.txtGender=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=Gender).grid(row=10,column=1, padx=20,pady=3)
        '''
        self.lblCheckInDate=Label(ABC2,font=('arial',12,'bold'),text="CheckInDate:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=11,column=0,sticky=W)
        self.txtCheckInDate=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=CheckInDate).grid(row=11,column=1, padx=20,pady=3)
        self.lblCheckOutDate=Label(ABC2,font=('arial',12,'bold'),text="CheckOutDate:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=12,column=0,sticky=W)
        self.txtCheckOutDate=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=CheckOutDate).grid(row=12,column=1, padx=20,pady=3)
        self.lblMeal=Label(ABC2,font=('arial',12,'bold'),text="Meal:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=13,column=0,sticky=W)
        self.cboMeal=ttk.Combobox(ABC2,font=('arial',12,'bold'),width=18,textvariable=Meal,state='readonly')
        self.cboMeal['value']=('','Breakfast','Launch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13,column=1, padx=20,pady=3)
        '''
        self.txtMeal=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=Meal).grid(row=13,column=1, padx=20,pady=3)
        '''
        
        self.lblRoomType=Label(ABC2,font=('arial',12,'bold'),text="RoomType:",padx=2,fg="cornsilk",bg='cadetblue').grid(row=14,column=0,sticky=W)
        self.cboRoomType=ttk.Combobox(ABC2,textvariable=RoomType,state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomType['value']=('','single','double','family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14,column=1,pady=3,padx=20)       
        '''
        self.txtRoomType=Entry(ABC2,font=('arial',12,'bold'),width=20,textvariable=RoomType).grid(row=14,column=1, padx=20,pady=3)
'''
        self.Momo = Checkbutton(ABC3,text="Momo ", variable=var1, onvalue=1,offvalue=0,font=('arial',12,'bold'),bg="cadetblue").grid(row=0,sticky=W)
        self.txtMomo =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Momo,bd=8,width=20,justify='left',state=DISABLED)
        self.txtMomo.grid(row=0,column=1)
        self.Chowmin = Checkbutton(ABC3,text="Chowmin ", variable=var2, onvalue=1,offvalue=0,font=('arial',12,'bold'),bg="cadetblue").grid(row=1,sticky=W)
        self.txtChowmin =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Chowmin,bd=8,width=20,justify='left',state=DISABLED)
        self.txtChowmin.grid(row=1,column=1)
        self.Chowmin = Checkbutton(ABC3,text="Omlet ", variable=var3, onvalue=1,offvalue=0,font=('arial',12,'bold'),bg="cadetblue").grid(row=2,sticky=W)
        self.txtChowmin =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Momo,bd=8,width=20,justify='left',state=DISABLED)
        self.txtChowmin.grid(row=2,column=1)
        self.Momo = Checkbutton(ABC3,text="BlackTea ", variable=var4, onvalue=1,offvalue=0,font=('arial',12,'bold'),bg="cadetblue").grid(row=3,sticky=W)
        self.txtMomo =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Momo,bd=8,width=20,justify='left',state=DISABLED)
        self.txtMomo.grid(row=3,column=1)
        self.Momo = Checkbutton(ABC3,text="MilkTea", variable=var5, onvalue=1,offvalue=0,font=('arial',12,'bold'),bg="cadetblue").grid(row=4,sticky=W)
        self.txtMomo =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Momo,bd=8,width=20,justify='left',state=DISABLED)
        self.txtMomo.grid(row=4,column=1)
        self.Momo = Checkbutton(ABC3,text="KhajaSet", variable=var6, onvalue=1,offvalue=0,font=('arial',12,'bold'),bg="cadetblue").grid(row=5,sticky=W)
        self.txtMomo =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Momo,bd=8,width=20,justify='left',state=DISABLED)
        self.txtMomo.grid(row=5,column=1)
        self.Momo = Checkbutton(ABC3,text="VegKhana", variable=var7, onvalue=1,offvalue=0,font=('arial',12,'bold'),bg="cadetblue").grid(row=6,sticky=W)
        self.txtMomo =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Momo,bd=8,width=20,justify='left',state=DISABLED)
        self.txtMomo.grid(row=6,column=1)
        self.Momo = Checkbutton(ABC3,text="Chickenkhana", variable=var8, onvalue=1,offvalue=0,font=('arial',12,'bold'),bg="cadetblue").grid(row=7,sticky=W)
        self.txtMomo =Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Momo,bd=8,width=20,justify='left',state=DISABLED)
        self.txtMomo.grid(row=7,column=1)
        self.lblspace=Label(ABC3,text="Tax and Total Sum",font=('arial',18,'bold'),pady=1,bd=9,bg='darkblue',fg='cornsilk',width=26,justify=CENTER).grid(row=8,column=0,columnspan=4)



        self.lblPaidTax=Label(ABC3,font=('arial',12,'bold'),text="Paid Tax",bd=7,bg="cadetblue",fg='black')
        self.lblPaidTax.grid(row=10,column=0,sticky=W)
        self.txtPaidTax = Entry(ABC3,font=('arial',12,'bold'),textvariable=PaidTax,bd=7,bg='white',width=25,justify=LEFT)
        self.txtPaidTax.grid(row=10,column=1)

        self.lblSubTotal=Label(ABC3,font=('arial',12,'bold'),text="Sub Total",bd=7,bg="cadetblue",fg='black')
        self.lblSubTotal.grid(row=11,column=0,sticky=W)
        self.txtSubTotal = Entry(ABC3,font=('arial',12,'bold'),textvariable=SubTotal,bd=7,bg='white',width=25,justify=LEFT)
        self.txtSubTotal.grid(row=11,column=1)

        self.lblTotalCost=Label(ABC3,font=('arial',12,'bold'),text="Total Cost",bd=7,bg="cadetblue",fg='black')
        self.lblTotalCost.grid(row=12,column=0,sticky=W)
        self.txtTotalCost = Entry(ABC3,font=('arial',12,'bold'),textvariable=TotalCost,bd=7,bg='white',width=25,justify=LEFT)
        self.txtTotalCost.grid(row=12,column=1)









        self.btnTotal = Button(ABC6,padx=14, pady=7,bd=5,bg='cadetblue',fg='black',font=('arial',16,'bold'),width=5,height=2,text="Total").grid(row=0,column=0)
        self.btnReset = Button(ABC6,padx=14, pady=7,bd=5,bg='cadetblue',fg='black',font=('arial',16,'bold'),width=5,height=2,text="Reset",command=Reset).grid(row=0,column=1)
        self.btnExit = Button(ABC6,padx=14, pady=7,bd=5,bg='cadetblue',fg='black',font=('arial',16,'bold'),width=5,height=2,text="Exit",command=iExit).grid(row=0,column=2)



if __name__=='__main__':
    root = Tk()
    application = Customer(root)
    root.mainloop()
