import tkinter as tk
import random
import string
import pyperclip
from tkinter import filedialog,Text
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
dict1={"CSK VS RR":'12/12/2020',"KXIP VS DC":'13/12/2020',"KKR VS RCB":'14/12/2020',"RR VS SRH":'15/12/2020',"CSK VS MI":'16/12/2020',"KKR VS DC":'17/12/2020','KXIP VS SRH':'18/12/2020','RCB VS CSK':'19/12/2020','RR VS MI':'20/12/2020'}
import mysql.connector as pyt
mycon=pyt.connect(host="localhost",user='root',password="prashu@1910",database="cricbook")
csr=mycon.cursor()
def BUY():
    root1=tk.Tk()
    root1.title("Welcome,Customer To our Booking System")
    canvas1=tk.Canvas(root1,height=700,width=700,bg="#56a0b3")
    canvas1.pack()
    fontExample = ("Courier", 16, "bold")
    frame1=tk.Frame(root1)
    frame1.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    label1=tkinter.Label(frame1,text="ENTER YOUR NAME",font=fontExample)
    label1.grid(row=1,column=0)
    e1=tk.Entry(frame1)
    e1.grid(row=5,column=0)
    label2=tkinter.Label(frame1,text="ENTER YOUR PHONE NUMBER",font=fontExample)
    label2.grid(row=8,column=0)
    e2=tk.Entry(frame1)
    e2.grid(row=12,column=0)
    label4=tkinter.Label(frame1,text="ENTER THE NUMBER OF SEATS",font=fontExample)
    label4.grid(row=18,column=0)
    e4=tk.Entry(frame1)
    e4.grid(row=20,column=0)
    
    label3=tkinter.Label(frame1,text="choose the match from the drop down menu",font=fontExample)
    label3.grid(row=24,column=0)
    combo=tkinter.ttk.Combobox(frame1,values=["CSK VS RR","KXIP VS DC","KKR VS RCB","RR VS SRH","CSK VS MI","KKR VS DC",'KXIP VS SRH','RCB VS CSK','RR VS MI'],font=fontExample)
    combo.grid(row=28,column=0)
    def ENTER():
        d=combo.get()
        d1=e1.get()
        d2=e2.get()
        d3=dict1[d]
        d4=e4.get()
        letters=string.ascii_uppercase
        res=''.join(random.choice(letters) for i in range (2))
        a=random.randint(100,200)
        tn=str(res)+"-"+str(a)
        root1.destroy()
        rootp=tk.Tk()
        canvasp=tk.Canvas(rootp,height=700,width=700,bg="#263d42")
        canvasp.pack()
        fontExample = ("Times New Roman", 20)
        framep=tk.Frame(rootp)
        framep.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
        text1=f"THIS IS YOUR TICKET NUMBER:{tn}"
        labelp3=tk.Label(framep,text="YOUR TICKET HAS BEEN BOOKED",font=fontExample)
        labelp3.pack()
        labelp2=tk.Label(framep,text=text1,font=fontExample)
        labelp2.pack()
        labelp3=tk.Label(framep,text='THIS IS YOUR TICKET INFORMATION')
        labelp3.pack()
        text4=f'NAME: {d1}'
        text5=f'PHONE NUMBER: {d2}'
        text6=f'TICKET NUMBER: {tn}'
        text7=f'NUMBER OF TICKETS: {d4}'
        labelp4=tk.Label(framep,text=text4,font=fontExample)
        labelp5=tk.Label(framep,text=text5,font=fontExample)
        labelp6=tk.Label(framep,text=text6,font=fontExample)
        labelp7=tk.Label(framep,text=text7,font=fontExample)
        labelp4.pack()
        labelp5.pack()
        labelp6.pack()
        labelp7.pack()
        csr.execute("insert into name values('%s','%s','%s','%s','%s')"% (d1,tn,d2,d3,d4))
        mycon.commit()
        csr.execute("insert into matches values('%s','%s','%s','%s')"% (d,tn,d2,d3))
        mycon.commit()
        def ENTER2():

            pyperclip.copy(tn)
            tk.messagebox.showinfo("","TICKET NUMBER COPIED")
            
        enter2=tk.Button(framep,text="COPY TICKET NUMBER",padx=10,pady=5,fg="black",command=ENTER2).pack()
        
        def ENTER1():
            global img1
            rootp.destroy()
            rootp1=tk.Tk()
            canvasp1=tk.Canvas(rootp1,height=700,width=700,bg="#263d42")
            canvasp1.pack()
            framep1=tk.Frame(rootp1)
            framep1.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
            labelp1=tk.Label(framep1,text="THANK YOU FOR USING OUR BOOKING SYSTEM").pack()

           

        enter1=tk.Button(framep,text="ENTER",padx=10,pady=5,fg="black",command=ENTER1).pack()
    enter=tk.Button(frame1,text="ENTER",padx=10,pady=5,fg="black",command=ENTER).grid(row=50,column=0)
