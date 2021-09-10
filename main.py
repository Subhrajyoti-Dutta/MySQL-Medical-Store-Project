import mysql.connector as sql
import tkinter as tk
import tkinter.messagebox as tm
# from tkinter import *
import datetime as dt


passwod=None

windows     = tk.Tk()
windows.title("Pasword")
winwidth    = 550
winheight   = 120
windows.geometry(f"{winwidth}x{winheight}")

pwdlabel = tk.Label(windows, text="ENTER THE PASSWORD : ")
pwdlabel.place(relx = 0.5, rely=0, x = -255, y = winheight//4, anchor = "nw")

pwdentry = tk.Entry(windows, width="40")
pwdentry.place(relx = 0.5, rely=0, x = -75,  y = winheight//4, anchor = "nw")

enter =    tk.Button(windows, text="ENTER", command=passwod, width="10")
enter.place(   relx = 0.5, rely=0, x = 0,    y = 100,          anchor = "s" )

windows.mainloop()

print(type(passwd.get()))