from tkinter import *
from tkinter import messagebox

top=Tk()#window creation
top.geometry("600x400")#window size

def get_data():
    tb3.configure(state='normal')
    a=int(tb1.get())
    b=int(tb2.get())
    tb1.delete(0,END)
    tb2.delete(0,END)
    area=a*b
    peri=2*(a+b)
    data="Area: "+str(area)+"  Perimeter:"+str(peri)
    l3.configure(text="Area "+str(area)+" Perimeter: "+str(peri))
    tb3.delete(0,END)
    tb3.insert(0,data)
    tb3.configure(state='disabled')
    messagebox.showinfo("Result: "+data)

l1=Label(top,text="Enter a value for Length : ")
l1.pack()
tb1=Entry(top,width=70)
tb1.pack()

l2=Label(top,text="Enter a value for Breadth : ")
l2.pack()
tb2=Entry(top,width=70)
tb2.pack()

btn1=Button(top,text="Submit",command=get_data)
btn1.pack()

l3=Label(top)
l3.pack()

tb3=Entry(top,width=70)
tb3.pack()
