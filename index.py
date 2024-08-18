import random
import time
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import Frame, ttk

# Balance = float(0.00)
rand_id = random.randrange(100000, 999999)
id = f"24BM{rand_id}"
user_file = pd.read_csv("user_data.csv")
# print(user_file['first name'])


#---------------------------------------------------------------------------------------------------------


class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400")
        self.welcome()
    
    def welcome(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=600, height=400)
        self.frame1.pack()
        self.reg_txt = ttk.Label(self.frame1, text="######################################")
        self.reg_txt.pack()
        self.reg1_txt = ttk.Label(self.frame1, text="Bank Management System")
        self.reg1_txt.pack()
        self.reg2_txt = ttk.Label(self.frame1, text="######################################")
        self.reg2_txt.pack()
        self.exit_btn = ttk.Button(self.frame1, text="Exit", command=lambda:quit())
        self.exit_btn.pack()
        self.register_btn = ttk.Button(self.frame1, text="Start Banking", command=self.banking)
        self.register_btn.pack()
    
    def banking(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=600, height=400)
        self.frame2.pack()
        self.create_acc = ttk.Button(self.frame2, text="Create Account", command=self.create_account)
        self.create_acc.pack()
        self.login_btn = ttk.Button(self.frame2, text="Login Account", command=self.welcome)
        self.login_btn.pack()
        self.not_btn = ttk.Button(self.frame2, text="Home", command=self.welcome)
        self.not_btn.pack()

    def create_account(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame3 = Frame(self.master, width=600, height=400)
        self.frame3.pack()
        self.first = ttk.Label(text="First name : ")
        self.first.pack()
        self.first_name = ttk.Entry(self.frame3)
        self.first_name.pack()
        self.last = ttk.Label(text="Last name : ")
        self.last.pack()
        self.last_name = ttk.Entry(self.frame3)
        self.last_name.pack()



#---------------------------------------------------------------------------------------------------------



root = tk.Tk()

app(root)

root.title("Bank Management System")

canvas = tk.Canvas(bg="black", height=400, width=600)
# canvas.grid(columnspan=5, rowspan=6)

design = tk.Label(text="######################################", fg="white", bg="black")
# design.grid(column=2, row=0)
messsage = tk.Label(text="Bank Management System", fg="white", bg="black")
# messsage.grid(column=2, row=1)
design2 = tk.Label(text="######################################", fg="white", bg="black")
# design2.grid(column=2, row=2)

exit_btn = tk.Button(text="Exit", fg="white", bg="black", height=2, width=12, border=0, command=lambda:quit())
# exit_btn.grid(column=0, row=4)

banking_btn = tk.Button(text="Start Banking", fg="white", bg="black", height=2, width=12, border=0)
# banking_btn.grid(column=4, row=4)

tk.mainloop()


def balance():
  pass

def deposite():
  pass

def withdraw():
  pass

def create_account():

  print("\n")
  print("##########################################################")
  print("\n")
  print("Enter your details for creating account")
  first_name = input("First name : ")
  last_name = input("Last name : ")
  age = int(input("Age : "))
  contact = int(input("Contact : "))
  print("NOTE : Minimum amout to be paid is 0.00")
  min_balance = float(input("Amount to deposite : "))
  user_id = id

  print("\n")
  print("##########################################################")
  print("\n")

  #-------------------------------------------------------------------------------------------------

  

  #-------------------------------------------------------------------------------------------------

  print(f"first name : {first_name}")
  print(f"last name : {last_name}")
  print(f"age : {age}")
  print(f"balance : {min_balance}")
  print(f"id : {user_id}")
  print("\n")
  print("##########################################################")
  print("\n")

  data_frame = {
    # 'Sr no': [f"{age}"],
    'first name': [f"{first_name}"],
    'last name': [f"{last_name}"],
    'age': [f"{age}"],
    'contact': [f"{contact}"],
    'balance': [f"{min_balance}"],
    'user_id': [f"{user_id}"],
  }

  conformation = input("To conform type Y and to go back type N : ")

  if conformation == "Y":
    upload_file = pd.DataFrame(data_frame)
    upload_file.to_csv('user_data.csv', mode='a', index=False, header=False)
  else :
    print("servers not working right now, come after lunch break")


def login_account():
  pass

##########################################################

def main():
  print("\n")
  print("##########################################################")
  print("\n")
  print("Bank Management System")
  print("\n")
  print("##########################################################")
  print("\n")
  print("1. CREATE NEW ACCOUNT")
  print("2. LOGIN YOUR ACCOUNT")
  print("3. EXIT")
  print("\n")

  first_choice = input("Enter the number here : ")

  if first_choice == "1":
    create_account()
  elif first_choice == "2":
    login_account()
  elif first_choice == "3":
    time.sleep(3)
    print("Thankyou for visiting, goodbye")
    quit()
  else:
    print("wrong input")


# if __name__ == '__main__':
#   main()