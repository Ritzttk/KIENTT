from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import shutil,os
from QUAN_LY_CAUTHU.database_manager import *
from QUAN_LY_CAUTHU.quanly import *

def win1():
    mainframe = ttk.Frame(root,padding='3 3 12 12')
    mainframe.grid(column =0,row =0,sticky = (N,W,E,S))
    mainframe.columnconfigure(0,weight=1)
    mainframe.rowconfigure(0,weight=1)

    ttk.Label(master=mainframe,text="Username").grid(row=0,column=0)
    ttk.Entry(master=mainframe,textvariable=var_user).grid(row=0,column=1)
    ttk.Label(master=mainframe,text="Password").grid(row=1,column=0)
    ttk.Entry(master=mainframe,show="*",textvariable=var_pass).grid(row=1,column=1)

    ttk.Button(mainframe,text='Login page',command=win2).grid(row=2,column=1,sticky=W)

    root.mainloop()

def win2():
    global var_user, var_pass
    username = var_user.get()
    password = var_pass.get()

    list_users = select_user()
    flag = False
    for user in list_users:
        if user[1] == username and user[2]==password:
            flag = True
    if flag:
        str_kq = "Welcome" + username + "to Arsenal Shop"
        messagebox.showinfo("Welcome",str_kq)
        root.widthraw()
        new = Toplevel()
        new.title('Shop Arsenal')
        new.geometry("400x300")
        new.resizable(0,0)

        menubar = Menu(new)
        chuc_nang = Menu(menubar,tearoff=0)
        chuc_nang.add_command(label="Add member",command="")
        chuc_nang.add_command(label="Find",command="")
        chuc_nang.add_separator()
        chuc_nang.add_command(label="Exit",command=new.quit)

        menubar.add_cascade(label="Function",menu=chuc_nang)

        mainframe = ttk.Frame(new, passding='3 3 12 12')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0,weight=1)
        new.config(menu=menubar)

        logo1 = PhotoImage(file="images/arsenal.gif")
        L = ttk.Label(master=mainframe,image=logo1)
        L.image=logo1
        L.grid(row=0,column=1,sticky=W)
    else:
        messagebox.showinfo("Warning","Username or Password incorrect!")
        var_user.set("")
        var_pass.set("")





#RUN SOFTWARE
root =Tk()
root.title('Login')
root.geometry("200x100")
root.resizable(0,0)

var_user = StringVar()
var_pass = StringVar()

win1()


