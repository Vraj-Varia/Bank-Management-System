from tkinter import *
from tkinter import ttk


class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x200")
        self.login()
    
    def login(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300)
        self.frame1.pack()
        self.reg_txt = ttk.Label(self.frame1, text='login')
        self.reg_txt.pack()
        self.register_btn = ttk.Button(self.frame1, text="Go to Register", command=self.register)
        self.register_btn.pack()
    
    def register(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = ttk.Label(self.frame2, text='register')
        self.reg_txt2.pack()
        self.login_btn = ttk.Button(self.frame2, text="Go to Login", command=self.login)
        self.login_btn.pack()

root = Tk()
app(root)
root.mainloop()


# import tkinter as tk
# from tkinter import *
# from tkinter import ttk


# class app:
#     def __init__(self, master):
#         self.frame1 = Frame(root, width=300, height=300)
#         self.frame1.pack()
#         self.reg_txt = ttk.Label(root, text='page1')
#         self.reg_txt.place(x=88, y=30)
# class app2:
#     def __init__(self, master):
#         self.frame2 = Frame(root, width=300, height=300)
#         self.reg_txt2 = ttk.Label(root, text='page2')
#         self.reg_txt2.place(x=88, y=30)
#         self.frame2.pack()
    
# root = Tk()
# a = app(root)
# a = app2(root)
# root.mainloop()