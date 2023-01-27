import tkinter as tk
import random
import string
import pyperclip
from tkinter import filedialog,Text
import tkinter.messagebox
from tkinter import *
root=tk.Tk()
from tkinter.ttk import *
dict1={"CSK VS RR":'12/12/2020',"KXIP VS DC":'13/12/2020',"KKR VS RCB":'14/12/2020',"RR VS SRH":'15/12/2020',"CSK VS MI":'16/12/2020',"KKR VS DC":'17/12/2020','KXIP VS SRH':'18/12/2020','RCB VS CSK':'19/12/2020','RR VS MI':'20/12/2020'}
import mysql.connector as pyt
mycon=pyt.connect(host="localhost",user='root',password="prashu@1910",database="cricbook")
csr=mycon.cursor()
if mycon.is_connected:
    print("WELCOME")
from buy import *
from cancel import *   
from show import *
from FORGET import *
root.title("Welcome To our Booking System")
canvas=tk.Canvas(root,height=700,width=700,bg="#54596d")
canvas.pack()
fontExample = ("Times New Roman", 40)
frame=tk.Frame(root)
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
label=tk.Label(frame,text="CRICKBOOK",font=fontExample).pack()
labela1=tk.Label(frame,text='''
                 ''').pack()
def help1():
    tk.messagebox.showinfo('HELP','''1.TICKETS CAN BE BOOKED FOR THE MATCHES USING THE FIRST OPTION
2.BOOKED TICKETS CAN BE CANCELLED USING THE SECOND OPTION
3.BOOKED TICKET DETAILS CAN BE VIEWED USING THE THIRD OPTION''')
    
        
        
helpa=tk.Button(frame,text="?",padx=10,pady=5,fg="black",command=help1)
helpa.pack()
buy=tk.Button(frame,text="1.BOOK TICKETS  ",padx=10,pady=5,fg="black",command=BUY)
buy.pack(side=tk.TOP)
labela1=tk.Label(frame,text='''
                 ''').pack()
cancel=tk.Button(frame,text="2.CANCELATION OF TICKETS",padx=10,pady=5,fg="black",command=CANCEL)
cancel.pack(side='top')
labela1=tk.Label(frame,text='''
                 ''').pack()
show=tk.Button(frame,text="3.DETAILS OF TICKET",padx=10,pady=5,fg="black",command=SHOW)
show.pack(side='top')

FORGET=tk.Button(frame,text="Forgot Ticket Number?",padx=10,pady=5,command=FORGET)
FORGET.pack(side='bottom')
    

root.mainloop()
