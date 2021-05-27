#TO Show internet speed in Tkinter application

import speedtest
from tkinter import *
from tkinter import messagebox

st=speedtest.Speedtest()

def up():
    global st
    data=str(st.upload())
    data=data[:2]+" Mbps"
    l1.config(text="Upload speed is: "+data)
def down():
    global st
    data=str(st.download())
    data=data[:2]+" Mbps"
    l1.config(text="Download speed is: "+data)

top=Tk()
top.geometry("600x400")

b1=Button(top,text="Upload",command=up)
b1.place(x=220,y=150)
b2=Button(top,text="Download",command=down)
b2.place(x=320,y=150)

l1=Label(top)
l1.place(x=150,y=200)
