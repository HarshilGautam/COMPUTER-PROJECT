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
csr=mycon.cursor(buffered=True)
def FORGET():
    fontExample = ("Times New Roman", 20)
    root1=tk.Tk()
    root1.title("Welcome,Customer To our Booking System")
    canvas1=tk.Canvas(root1,height=700,width=700,bg="#56a0b3")
    canvas1.pack()
    frame1=tk.Frame(root1)
    frame1.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    label1=tkinter.Label(frame1,text="ENTER YOUR PHONE NUMBER",font=fontExample)
    label1.grid(row=1,column=0)
    e1=tk.Entry(frame1)
    e1.grid(row=5,column=0)
    def ENTER():
        d=e1.get()
        root1.destroy()
        rootp=tk.Tk()
        canvasp=tk.Canvas(rootp,height=700,width=700,bg="#263d42")
        canvasp.pack()
        framep=tk.Frame(rootp)
        framep.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
        a="select phone_number from name"
        csr.execute(a)
        b=list(csr.fetchall())
        for i in b:
            l=list(i)
            if d in l:
                fontExample = ("Times New Roman", 20)
                csr.execute('select ticket_number from name where phone_number="%s"' % (d,))
                mycon.commit()
                b1=list(csr.fetchall())
                print(b1)
                tn=b1[0][0]
                labelp2=tk.Label(framep,text=f'TICKET NUMBER:  {tn}')
                labelp2.pack()
                def ENTER2():
                    pyperclip.copy(tn)
                    tk.messagebox.showinfo("","TICKET NUMBER COPIED")
                enter2=tk.Button(framep,text="COPY TICKET NUMBER",padx=10,pady=5,fg="black",command=ENTER2).pack()
                break
                
            else:
                continue
        else:
            fontExample = ("Courier", 20)
            labelp1=tk.Label(framep,text=" SORRY NO SUCH RECORD AVAILABLE",font=fontExample)
            labelp1.pack()
        
        
    enter=tk.Button(frame1,text="ENTER",padx=10,pady=5,fg="black",command=ENTER).grid(row=50,column=0)
