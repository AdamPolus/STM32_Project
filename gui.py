#!/usr/bin/python3

from asyncore import read
from tkinter import *
import tkinter as tk
import serial
import time
import threading


initial ="test"

def verify():
    if 20 <= float(user_input.get()) <=80:
        set_val.set(float(user_input.get()))
        print("True")
    else:
        print("False")


ser = serial.Serial("/dev/ttyACM0", 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE,timeout=0) 






def readserial():

    ser_bytes = ser.readline()
    ser_bytes = ser_bytes.decode("ascii")
    ser_bytes = ser_bytes.rstrip()
    ser_bytes = ser_bytes.strip('Temp: ')
        
    display1 = tk.Label(win,text=ser_bytes, bg= "red",fg= "white",font="none 12 bold").grid(row=2,column=1, sticky=W)
    

def work (): 
  threading.Timer(0.25, work).start ()
  readserial()

   

#window part

win = tk.Tk()
win.geometry("300x250")
user_input = tk.StringVar(win)
set_val = tk.StringVar(win)
win.title("Temperature Control APP")
win.configure(background="red")
label_1= tk.Label (win, text="Set temperature: ",bg= "red",fg= "white",font="none 12 bold") .grid(row=1,column=0, sticky=W)
# Label (win, text="24.00: ",bg= "red",fg= "white",font="none 12 bold") .grid(row=1,column=1, sticky=W)
textentry_1 = tk.Entry(win, textvariable = user_input, width =10,bg="white")  .grid(row=3,column=1, sticky=W)
label_2= tk.Label (win, textvariable=set_val,bg= "red",fg= "white",font="none 12 bold") .grid(row=1,column=1, sticky=W)
btn_1 = tk.Button(win,text="SET",width=4,command=verify)  .grid(row=3,column=2, sticky=W)
label_3= tk.Label (win, text="Actual temperature: ",bg= "red",fg= "white",font="none 12 bold") .grid(row=2,column=0, sticky=W)
label_4= tk.Label (win, textvariable=initial,bg= "red",fg= "white",font="none 12 bold") .grid(row=2,column=1, sticky=W)
work()
win.mainloop()

ser.close()

