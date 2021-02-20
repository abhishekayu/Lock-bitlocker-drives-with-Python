import os
import tkinter as tk
import win32com.shell.shell as shell
from tkinter import * 
from tkinter.ttk import *

root= tk.Tk()
root.geometry('400x200')
root.configure(bg='black')
#root.iconbitmap(r'F:\py\Lock\ok.png')
root.resizable(width=False, height=False) 
root.title ("Lock Mount")
w = tk.Label(root, text=" Abhishek Patel @imdarkcoder " ,font = ("Times New Roman", 12),bg='black',fg="white")
w.pack()

def myc():
    commands = 'manage-bde -lock E: -forcedismount'
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)


photo = PhotoImage(file = r"F:\py\Lock\b.ico")
photoimage = photo.subsample(2,2)

button1 = tk.Button (root,image = photoimage, compound = LEFT,text = "Lock E:Mount ", font = ("Times New Roman", 20),bg='darkslategray', command = myc)
button1.pack (expand = 1)     


root.mainloop()