import tkinter as tk
import random
import string
from tkinter import filedialog,Text
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
dict1={"CSK VS RR":'12/12/2020',"KXIP VS DC":'13/12/2020',"KKR VS RCB":'14/12/2020',"RR VS SRH":'15/12/2020',"CSK VS MI":'16/12/2020',"KKR VS DC":'17/12/2020','KXIP VS SRH':'18/12/2020','RCB VS CSK':'19/12/2020','RR VS MI':'20/12/2020'}
import mysql.connector as pyt
mycon=pyt.connect(host="localhost",user='root',password="prashu@1910",database="cricbook")
csr=mycon.cursor()   
    
def SHOW():
    root3=tk.Tk()
    root3.title("Welcome,Customer To our Cancellation System")
    canvas3=tk.Canvas(root3,height=700,width=700,bg="#263d42")
    canvas3.pack()
    frame3=tk.Frame(root3)
    frame3.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    label3=tk.Label(frame3,text="PLEASE ENTER YOUR TICKET NUMBER").grid(row=0,column=0)
    e3=tk.Entry(frame3)
    e3.grid(row=0,column=1)
    csr = mycon.cursor(buffered=True)
    def ENTER():
        global img3
        global img4
        d=e3.get()
        d1=str(d)
        root3.destroy()
        rootp=tk.Tk()
        canvasp=tk.Canvas(rootp,height=700,width=700,bg="#263d42")
        canvasp.pack()
        framep=tk.Frame(rootp)
        framep.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
        a="select ticket_number from name"
        csr.execute(a)
        b=list(csr.fetchall())
        for i in b:
            l=list(i)
            if d in l:
                fontExample = ("Times New Roman", 20)
                csr.execute('select * from name where ticket_number="%s"' % (d,))
                mycon.commit()
                b1=list(csr.fetchall())
                name=b1[0][0]
                tn=b1[0][1]
                pn=b1[0][2]
                csr.execute('select * from matches where ticket_number="%s"' % (d,))
                mycon.commit()
                b2=list(csr.fetchall())
                match=b2[0][0]
                labelp1=tk.Label(framep,text=f'NAME:  {name}',font=fontExample)
                labelp1.pack()
                labelp2=tk.Label(framep,text=f'TICKET NUMBER:  {tn}',font=fontExample)
                labelp2.pack()
                labelp3=tk.Label(framep,text=f'PHONE NUMBER:  {pn}',font=fontExample)
                labelp3.pack()
                labelp4=tk.Label(framep,text=f'MATCH:  {match}',font=fontExample)
                labelp4.pack()
                break
            else:
                continue
        else:
            fontExample = ("Courier", 20)
            labelp1=tk.Label(framep,text=" SORRY NO SUCH RECORD AVAILABLE",font=fontExample)
            labelp1.pack()
    labela1=tk.Label(frame3,text='''
                 ''').grid(row=1,column=0)  
    enter=tk.Button(frame3,text="ENTER",padx=10,pady=5,fg="black",command=ENTER).grid(row=2,column=1)
    csr.execute("select * from name")
