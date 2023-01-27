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
def CANCEL():
    root2=tk.Tk()
    root2.title("Welcome,Customer To our Cancellation System")
    canvas2=tk.Canvas(root2,height=700,width=700,bg="#263d42")
    canvas2.pack()
    frame2=tk.Frame(root2,bg="#263d42")
    frame2.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    label2=tk.Label(frame2,text="PLEASE ENTER YOUR TICKET NUMBER").grid(row=0,column=0)
    
    e1=tk.Entry(frame2)
    e1.grid(row=0,column=1)
    def ENTER():
        global img2
        
        d=e1.get()
        d1=str(d)
        a="select ticket_number from name"
        csr.execute(a)
        b=list(csr.fetchall())
        for i in b:
            l=list(i)
            if d in l:
                res=tk.messagebox.askquestion('DELETE TICKET', 'DO YOU REALLY WANT TO  CANCEL RECORD')
                if res == 'yes' :
                    csr.execute("delete from name where ticket_number='%s'" % (d,))
                    mycon.commit()
                    tk.messagebox.showinfo('TICKET CANCELLED',"YOUR TICKET HAS BEEN CANCELED")
                    root2.destroy()
                    rootp2=tk.Tk()
                    canvasp2=tk.Canvas(rootp2,height=700,width=700,bg="#263d42")
                    canvasp2.pack()
                    framep2=tk.Frame(rootp2)
                    framep2.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
                    labelp2=tk.Label(framep2,text="WE HOPE TO SEE YOU AGAIN!!").pack()

                else:
                    root2.destroy()
                    break
            else:
                continue
        else:
            tk.messagebox.showerror("RECORDS NOT AVAILABLE")

    enter = tk.Button(frame2, text="ENTER", padx=10, pady=5, fg="black", command=ENTER).grid(row=1, column=0)
