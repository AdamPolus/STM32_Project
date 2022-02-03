#!/usr/bin/python3

from asyncore import read
from glob import glob
from sqlite3 import Row
from tkinter import *
import tkinter as tk
import serial
import time
import threading






def verify():
    
    if 20 <= float(user_input.get()) <=80:
        set_val.set("%.2f" % float(user_input.get()))
        # print("True")
        
        delete_err_label()
    # else:
       
        # err_disp = Label(win,text="\n Value must be between 20-80 degree!", bg= "red",fg= "white",font="none 12 bold")
        # err_disp.place(x=0,y=150)
        
        # print("False") 


ser = serial.Serial("/dev/ttyACM0", 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE,timeout=0) 

def delete_err_label():

    
    print("super")


def writeserial():
    ser_w_bytes= (float(user_input.get()))
    if 20 <= ser_w_bytes <=80:
        ser_w_bytes= "%.2f" % ser_w_bytes
    
        ser_w_bytes = str(ser_w_bytes)
    
        # print(str(ser_w_bytes))
        ser_w_bytes = ser_w_bytes.encode("ascii")
        ser.write(ser_w_bytes)
        print("send")


def readserial():

    ser_bytes = ser.readline()
    ser_bytes = ser_bytes.decode("ascii")
    ser_bytes = ser_bytes.rstrip()
    ser_bytes = (ser_bytes.strip('Temp: '))
    # print(ser_bytes)   
    display1 = tk.Label(win,text=ser_bytes, bg= "red",fg= "white",font="none 12 bold").grid(row=2,column=1, sticky=W)
    

def work (): 
  threading.Timer(0.2, work).start ()
  readserial()

   

#window part

win = tk.Tk()
win.geometry("500x300")
user_input = tk.StringVar(win)
set_val = tk.StringVar(win)
tmp_send = tk.StringVar(win)
win.title("Temperature Control APP")
win.configure(background="red")
label_1= tk.Label (win, text="Set temperature: ",bg= "red",fg= "white",font="none 12 bold") .grid(row=1,column=0, sticky=W)
# Label (win, text="24.00: ",bg= "red",fg= "white",font="none 12 bold") .grid(row=1,column=1, sticky=W)
textentry_1 = tk.Entry(win, textvariable = user_input, width =10,bg="white")  .grid(row=3,column=1, sticky=W)
label_2= tk.Label (win, textvariable=set_val,bg= "red",fg= "white",font="none 12 bold") .grid(row=1,column=1, sticky=W)
btn_1 = tk.Button(win,text="SET",width=4,command=lambda:[verify(), writeserial()])  .grid(row=3,column=2, sticky=W)
label_3= tk.Label (win, text="Actual temperature: ",bg= "red",fg= "white",font="none 12 bold") .grid(row=2,column=0, sticky=W)
# label_4= tk.Label (win, textvariable=initial,bg= "red",fg= "white",font="none 12 bold") .grid(row=2,column=1, sticky=W)

# buttonMsg = Button(win, text="send", command = writeserial) .grid(row=4,column=1, sticky=W) # create a send button for send the message
# err_disp= Label(win,text="", bg= "red",fg= "white",font="none 12 bold").place(x=0,y=150)
# err_disp.pa
work()

win.mainloop()

ser.close()

