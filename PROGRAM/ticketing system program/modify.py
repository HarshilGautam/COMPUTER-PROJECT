import tkinter as tk
import random
import string
import pyperclip
from tkinter import filedialog,Text
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
dict1={"CSK VS RR":'12/12/2020',"KXIP VS DC":'13/12/2020',"KKR VS RCB":'14/12/2020',"RR VS SRH":'15/12/2020',"CSK VS MI":'16/12/2020',"KKR VS DC":'17/12/2020','KXIP VS SRH':'18/12/2020','RCB VS CSK':'19/12/2020','RR VS MI':'20/12/2020'}
dict2={'Phone Number':'phone_number','Name':'name','NO of Seats':'no_seats'}
import mysql.connector as pyt
mycon=pyt.connect(host="localhost",user='root',password="prashu@1910",database="cricbook")
csr=mycon.cursor()

def modify():
    fontExample = ("Times New Roman", 20)
    root1=tk.Tk()
    root1.title("Welcome,Customer To our Booking System")
    canvas1=tk.Canvas(root1,height=700,width=700,bg="#56a0b3")
    canvas1.pack()
    frame1=tk.Frame(root1)
    frame1.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    label3=tkinter.Label(frame1,text="Ticket Number",font=fontExample)
    label3.grid(row=16,column=0)
    e2=tk.Entry(frame1)
    e2.grid(row=20,column=0)
    label1=tkinter.Label(frame1,text="CHOOSE THE OPTION YOU WOULD WANT TO  MODIFY",font=fontExample)
    label1.grid(row=24,column=0)
    combo=tkinter.ttk.Combobox(frame1,values=['Phone Number','Name','NO of Seats'],font=fontExample)
    combo.grid(row=28,column=0)
    label2=tkinter.Label(frame1,text="MODIFIED VALUE",font=fontExample)
    label2.grid(row=32,column=0)
    e1=tk.Entry(frame1)
    e1.grid(row=36,column=0)
    
    def ENTER():
        d=combo.get()
        d3=dict2[d]
        d2=e1.get()
        d4=e2.get()
        root1.destroy()
        rootp=tk.Tk()
        frame1=tk.Frame(root1)
        frame1.pack()
        canvasp=tk.Canvas(rootp,height=700,width=700,bg="#263d42")
        canvasp.pack()
        e='update name set %s=%s where ticket_number=%s'
        i=(d3,d2,d4)
        csr.execute(e,i)
        label4=tkinter.Label(frame1,text="VALUES ARE MODIFIEED",font=fontExample)
        label4.pack()
    enter2=tk.Button(frame1,text="ENTER",padx=10,pady=5,fg="black",command=ENTER).grid(row=40,column=0)
        
        
        
