#demo account login credential given below
#Account Number : 0000 ------------ Password : demo

# modules used

from tkinter import *
from tkinter import messagebox
import sqlite3
import time
import math, random,smtplib

#global font
ARIAL = ("arial",10,"bold")

class Bank:

# login page 

    def __init__(self,root):

        root.geometry("550x550")
        self.conn = sqlite3.connect("atm_databse.db", timeout=100)
        self.login = False
        self.root = root

        self.header = Label(self.root,text="STATE BANK OF INDIA",bg="#50A8B0",fg="white",font=("arial",20,"bold"))
        self.header.pack(fill=X)
        self.frame = Frame(self.root,bg="#728B8E",width=550,height=550)
        

        #  Login Page Form Components
        
        self.userlabel =Label(self.frame,text="ACCOUNT NUMBER",bg="#728B8E",fg="white",font=ARIAL)
        self.uentry = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.plabel = Label(self.frame, text="PASSWORD",bg="#728B8E",fg="white",font=ARIAL)
        self.pentry = Entry(self.frame,bg="honeydew",show="*",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.fpbutton =Button(self.frame,text="Forgot Password",bg="#50A8B0",fg="white",font=ARIAL,command=self.otp)
        self.nubutton = Button(self.frame,text="New User",bg="#50A8B0",fg="white",font=ARIAL,command=self.new_user)
        self.log_button = Button(self.frame,text="LOGIN",bg="#50A8B0",fg="white",font=ARIAL,command=self.verify)
        self.q = Button(self.frame,text="Quit",bg="#50A8B0",fg="white",font=ARIAL,command = self.root.destroy)
       
        #  placement of buttons,labels

        self.userlabel.place(x=145,y=100,width=200,height=20)
        self.uentry.place(x=153,y=130,width=200,height=20)
        self.plabel.place(x=125,y=160,width=200,height=20)
        self.pentry.place(x=153,y=190,width=200,height=20)
        self.log_button.place(x=220,y=240,width=55,height=25)
        self.fpbutton.place(x=50,y=300,width=150,height=25)
        self.nubutton.place(x=250,y=300,width=100,height=25)
        self.q.place(x=400,y=300,width=50,height=25)
        self.frame.pack()

# forgot password : otp methoed to retrive password
 
    def otp(self):

        messagebox._show("Notice","get to the idle screen" )
        self.acc_list = []
        self.temp = self.conn.execute("select email from atm where acc_no = ? ",(int(self.uentry.get()),))
        for i in self.temp:
            self.acc_list.append("{}".format(i[0]))
        import math, random,smtplib
        
        email=self.acc_list
        string = '0123456789'
        OTP = ""
        length = len(string)
        for i in range(6):
            OTP += string[math.floor(random.random() * length)]
            

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("statebankofindia.in.com@gmail.com", "assveera")
        subject = "Your One Time Password (OTP) for BANKING on SBI is  "
        body = "The requested otp is : "
        message = f'Subject :{subject}\n\n{body+OTP}'
        s.sendmail("statebankofindia.in.com@gmail.com", email, message)
        s.quit()

        otp = input("ENTER OTP  :   ")
        
        if otp == OTP:
            print("OTP is correct")
            self.acc=int(self.uentry.get())
            passw=input("enter your password here :  ")
            self.conn.execute("update atm set pass = ? where acc_no = ?",(passw,self.acc))
            messagebox._show("Notice", "your password has been changed successfully")
            
        else:
        
            print("OTP is wrong :(")
    
# new user registration       

    def new_user(self):
        
        self.frame.destroy()
        
        self.header = Label(self.root,text="NEW USER APPLICATION",bg="#50A8B0",fg="white",font=("arial",20,"bold"))
        self.header.pack(fill=X)
        self.frame = Frame(self.root,bg="#728B8E",width=1000,height=1100)


        #  Login Page Form Components
        
        self.name_label =Label(self.frame,text="NAME",bg="#728B8E",fg="white",font=ARIAL)
        self.name_entry = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.accno_label = Label(self.frame, text="ACC_NO.",bg="#728B8E",fg="white",font=ARIAL)
        self.accno_entry = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.acctype_label =Label(self.frame,text="ACC_TYPE",bg="#728B8E",fg="white",font=ARIAL)
        self.acctype_entry = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.balance_label =Label(self.frame,text="BALANCE",bg="#728B8E",fg="white",font=ARIAL)
        self.balance_entry = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.password_label =Label(self.frame,text="PASSWORD",bg="#728B8E",fg="white",font=ARIAL)
        self.password_entry = Entry(self.frame,bg="honeydew",show="*",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")        
        self.email_label =Label(self.frame,text="EMAIL",bg="#728B8E",fg="white",font=ARIAL)
        self.email_entry = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.phno_label =Label(self.frame,text="PHONE NO.",bg="#728B8E",fg="white",font=ARIAL)
        self.phno_entry = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.done_button = Button(self.frame,text="Done",bg="#50A8B0",fg="white",font=ARIAL,command=self.insert)      
        self.quit = Button(self.frame,text="Quit",bg="#50A8B0",fg="white",font=ARIAL,command = self.root.destroy)

        #  placement of buttons,labels

        self.name_label.place(x=50,y=50,width=150,height=20)
        self.name_entry.place(x=250,y=50,width=150,height=20)
        self.accno_label.place(x=50,y=100,width=150,height=20)
        self.accno_entry.place(x=250,y=100,width=150,height=20)
        self.acctype_label.place(x=50,y=150,width=150,height=20)
        self.acctype_entry.place(x=250,y=150,width=150,height=20)
        self.balance_label.place(x=50,y=200,width=150,height=20)
        self.balance_entry.place(x=250,y=200,width=150,height=20)       
        self.password_label.place(x=50,y=250,width=150,height=20)
        self.password_entry.place(x=250,y=250,width=150,height=20)
        self.email_label.place(x=50,y=300,width=150,height=20)
        self.email_entry.place(x=250,y=300,width=150,height=20)
        self.phno_label.place(x=50,y=350,width=150,height=20)
        self.phno_entry.place(x=250,y=350,width=150,height=20)
        self.done_button.place(x=123,y=400,width=50,height=20)
        self.quit.place(x=325,y=400,width=50,height=20)
        self.frame.pack()

    def insert(self):
        entries=(self.name_entry.get(),self.accno_entry.get(),self.acctype_entry.get(),self.balance_entry.get(),self.password_entry.get(),self.email_entry.get(),self.phno_entry.get())
        self.conn.execute("insert into atm values(?,?,?,?,?,?,?)",entries)
        self.conn.commit()
        messagebox._show("Notice", "your account is been created ! please log in again")

#Fetching Account data from database
        
    def database_fetch(self):
        self.acc_list = []
        self.temp = self.conn.execute("select name,pass,acc_no,acc_type,bal,email,phno from atm where acc_no = ? ",(self.ac,))
        for i in self.temp:
            self.acc_list.append("Name = {}".format(i[0]))
            self.acc_list.append("Password = {}".format(i[1]))
            self.acc_list.append("Account no = {}".format(i[2]))
            self.acc_list.append("Account type = {}".format(i[3]))
            self.ac = i[2]
            self.acc_list.append("Balance = {}".format(i[4]))
            self.acc_list.append("{}".format(i[5]))
            self.acc_list.append("Phone No. = {}".format(i[6]))
            return self.ac
        
#verifying of authorised user

    def verify(self):
        ac = False
        self.temp = self.conn.execute("select name,pass,acc_no,acc_type,bal from atm where acc_no = ? ", (int(self.uentry.get()),))
        for i in self.temp:
            self.ac = i[2]
            if i[2] == self.uentry.get():
                ac = True
            elif i[1] == self.pentry.get():
                ac = True
                m = "{} Login SucessFull".format(i[0])
                self.database_fetch()
                messagebox._show("Login Info", m)
                self.frame.destroy()
                self.MainMenu()
            else:
                ac = True
                m = " Login UnSucessFull ! Wrong Password"
                messagebox._show("Login Info!", m)
                self.MainMenu() 
                self.email()


        if not ac:
            m = " Wrong Acoount Number !"
            messagebox._show("Login Info!", m)

#security alert ensured : send a mail about wrong login
            
    def email(self):
                import smtplib
                from email.mime.text import MIMEText
                from email.mime.multipart import MIMEMultipart
                from email.mime.base import MIMEBase
                from email import encoders
                import os.path
                self.database_fetch()
                email = 'statebankofindia.in.com@gmail.com' #login details
                password = 'assveera'
                send_to_email = self.acc_list[5]
                subject = 'Critical security alert'  # The subject line
                message =   ("Your Bank Account was just signed in from a new Windows device.\n" #message 
                             "You're getting this email to make sure it was you.\n"
                             "If you didn't change it, you should check what happened.\n")
                
                #file location :: please change this location according to your computer
                file_location=r"C:\Users\surya\Desktop\Banking_Project-ATM-- MASTER\DATA\How to protect your bank cards from fraud.docx"
                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject
                msg.attach(MIMEText(message, 'plain'))

                # Setup the attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                # Attach the attachment to the MIMEMultipart object                 
                msg.attach(part)
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()

#Main App Appears after logined !
                
    def MainMenu(self):
        self.frame = Frame(self.root,bg="#728B8E",width=1300,height=600)
        root.geometry("1300x510")
        #button anf funtional commands
        self.detail = Button(self.frame,text="Account Details",bg="#50A8B0",fg="white",font=ARIAL,command=self.account_detail)
        self.enquiry = Button(self.frame, text="Balance Enquiry",bg="#50A8B0",fg="white",font=ARIAL,command= self.Balance)
        self.deposit = Button(self.frame, text="Deposit Money",bg="#50A8B0",fg="white",font=ARIAL,command=self.deposit_money)
        self.withdrawl = Button(self.frame, text="Withdrawl Money",bg="#50A8B0",fg="white",font=ARIAL,command=self.withdrawl_money)
        self.pinchange = Button(self.frame, text="Pin Change",bg="#50A8B0",fg="white",font=ARIAL,command=self.pinchange2)       
        self.transfer = Button(self.frame, text="Transfer Fund",bg="#50A8B0",fg="white",font=ARIAL,command=self.transfer)
        self.q = Button(self.frame, text="Quit", bg="#50A8B0", fg="white", font=ARIAL, command=self.root.destroy)
        self.log = Button(self.frame, text="Logout",bg="#50A8B0",fg="white",font=ARIAL, command=self.logout)
        #placement of these buttons
        self.detail.place(x=100,y=50 ,width=200,height=50)
        self.withdrawl.place(x=100, y=200, width=200, height=50)
        self.transfer.place(x=100, y=350, width=200, height=50)
        self.enquiry.place(x=900, y=50, width=200, height=50)
        self.deposit.place(x=900, y=200, width=200, height=50)       
        self.pinchange.place(x=900, y=350, width=200, height=50)   
        self.q.place(x=350, y=350, width=200, height=50)
        self.log.place(x=650, y=350, width=200, height=50)
        self.frame.pack()  

#internal functions
        
    def logout(self): 
        text="STATE BANK OF INDIA"+"\n"+"You Have Been Successfully Logged Out!"+"\n"+str(time.ctime())
        self.label = Label(self.frame, text=text,font=ARIAL)
        self.label.place(x=400,y=150,width=400,height=100)
        self.frame.destroy()
        self.header.destroy()
        self.__init__(root)

    def account_detail(self):   
        self.database_fetch()
        text = self.acc_list[0]+"\n"+self.acc_list[2]+"\n"+self.acc_list[3]+"\n"+self.acc_list[5]+"\n"+self.acc_list[6]
        self.label = Label(self.frame,text=text,font=ARIAL)
        self.label.place(x=400,y=150,width=400,height=100)
        self.ok = Button(self.frame,text="ok",bg="#50A8B0",fg="white",font=ARIAL,command = self.label.destroy)
        self.ok.place(x=575,y=300,width=50,height=25)

    def Balance(self):
        self.database_fetch()
        self.label = Label(self.frame, text=self.acc_list[4],font=ARIAL)
        self.label.place(x=400,y=150,width=400,height=100)
        self.ok = Button(self.frame,text="ok",bg="#50A8B0",fg="white",font=ARIAL,command = self.label.destroy)
        self.ok.place(x=575,y=300,width=50,height=25)

    def deposit_money(self):
        self.money_box = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.submitButton = Button(self.frame,text="Submit",bg="#50A8B0",fg="white",font=ARIAL)
        self.money_box.place(x=375,y=100,width=175,height=20)
        self.submitButton.place(x=575,y=200,width=55,height=20)
        self.submitButton.bind("<Button-1>",self.deposit_trans)

    def deposit_trans(self,flag):
        self.label = Label(self.frame, text="Transaction Completed !", font=ARIAL)
        self.label.place(x=400,y=150,width=400,height=100)
        self.conn.execute("update atm set bal = bal + ? where acc_no = ?",(self.money_box.get(),self.ac))
        self.conn.commit()

    def withdrawl_money(self):
        self.money_box = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.submitButton = Button(self.frame,text="Submit",bg="#50A8B0",fg="white",font=ARIAL)
        self.money_box.place(x=650,y=100,width=175,height=20)
        self.submitButton.place(x=575,y=200,width=55,height=20)
        self.submitButton.bind("<Button-1>",self.withdrawl_trans)

    def withdrawl_trans(self,flag):
        self.label = Label(self.frame, text="Money Withdrawl !", font=ARIAL)
        self.label.place(x=400,y=150,width=400,height=100)
        self.conn.execute("update atm set bal = bal - ? where acc_no = ?",(self.money_box.get(),self.ac))
        self.conn.commit()

    def pinchange2(self): 
        self.label = Label(self.frame, text="Type Password Below !", font=ARIAL)
        self.label.place(x=400,y=150,width=400,height=100)
        self.passwd_entry = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.passwd_entry.place(x=520,y=225,width=175,height=20)
        self.submit_Button = Button(self.frame,text="Submit",bg="#50A8B0",fg="white",font=ARIAL,command=self.fppinchange) 
        self.submit_Button.place(x=570,y=270,width=55,height=20)
        passwd=str(self.passwd_entry.get())
        self.conn.execute("update atm set pass = ? where acc_no = ?",(passwd,self.ac))
        self.conn.commit()
        
    def fppinchange (self):        
        self.conn.execute("update atm set pass = ? where acc_no = ?",(self.passwd_entry.get(),self.ac))
        self.conn.commit()
        messagebox._show("Notice", "your password has been changed successfully")

    def transfer(self):
        self.tacc = Label(self.frame, text="account no. of the recipient", font=ARIAL)        
        self.tacc_entry = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.tamt = Label(self.frame, text="amt to be transferred", font=ARIAL)        
        self.tamt_entry = Entry(self.frame,bg="honeydew",highlightcolor="#50A8B0",highlightthickness=2,highlightbackground="white")
        self.submit_Button = Button(self.frame,text="Submit",bg="#50A8B0",fg="white",font=ARIAL,command=self.transfer1)       
        self.tacc.place(x=400,y=100,width=400,height=20)
        self.tacc_entry.place(x=535,y=150,width=150,height=20)
        self.tamt.place(x=400,y=200,width=400,height=20)
        self.tamt_entry.place(x=535,y=250,width=150,height=20)        
        self.submit_Button.place(x=575,y=300,width=70,height=20)

    def transfer1(self):
        self.conn.execute("update atm set bal = bal - ? where acc_no = ?",(self.tamt_entry.get(),self.ac))
        self.conn.commit()
        self.conn.execute("update atm set bal = bal + ? where acc_no = ?",(self.tamt_entry.get(),self.tacc_entry.get()))
        self.conn.commit()
        messagebox._show("Notice", "transferred successfully")
        
        
        
root = Tk()
root.title("Sign In")
root.geometry("600x420")
icon = PhotoImage(file="icon.png")
root.tk.call("wm",'iconphoto',root._w,icon)
obj = Bank(root)
root.mainloop()


