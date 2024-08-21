import tkinter as tk
from tkinter import *
import pandas as pd
import random

rand_id = random.randrange(100000, 999999)
id = f"24BM{rand_id}"

window = tk.Tk()

class App():

# ------------------------ FUNCTIONS ------------------------
  def __init__(self, master):
    self.master = master
    self.master.geometry("1100x700")
    self.welcome_page()
# ------------------------ WELCOME FRAME ------------------------
  def welcome_page(self):
    for i in self.master.winfo_children():
      i.destroy()
    self.welcome_frame = tk.Frame(
      bg="lightblue"
    )
    self.welcome_frame.pack()

    self.welcome = tk.Label(
      self.welcome_frame, 
      text="BMS",
      font=("Lucida Bright", 30, 'bold'),
      bg="lightblue"
    )
    self.welcome.grid(
      column=2, 
      row=3,
      pady=60,
      padx=40
    )

    self.start_btn = tk.Button(
      self.welcome_frame,
      text="Start Banking",
      font=("Lucida Bright", 20),
      command=self.home,
      width=20,
      borderwidth=1
    )
    self.start_btn.grid(
      column=2,
      row=5,
      pady=40,
      padx=40
    )
    # ------------------------ HOME FRAME ------------------------
  def home(self):
    for i in self.master.winfo_children():
      i.destroy()
    self.home = tk.Frame(
      bg="lightblue"
    )
    self.home.pack()

    self.deposite_amount = tk.Button(
      self.home,
      text="Deposite",
      font=('Lucida Bright', 20),
      width=20
    )
    self.withdraw_amount = tk.Button(
      self.home,
      text="Withdraw",
      font=('Lucida Bright', 20),
      width=20
    )
    self.create_acc = tk.Button(
      self.home,
      text="Create Account",
      font=('Lucida Bright', 20),
      width=20,
      command=self.create_acc
    )
    self.login_acc = tk.Button(
      self.home,
      text="View Balance",
      font=('Lucida Bright', 20),
      width=20,
      command=self.view_balance
    )

    self.deposite_amount.grid(
      column=2,
      row=1,
      pady=40
    )
    self.withdraw_amount.grid(
      column=2,
      row=2,
      pady=40
    )
    self.create_acc.grid(
      column=2,
      row=3,
      pady=40
    )
    self.login_acc.grid(
      column=2,
      row=4,
      pady=40
    )

  def create_acc(self):
    for i in self.master.winfo_children():
      i.destroy()
    self.create = tk.Frame(
      bg="lightblue"
    )
    self.create.pack()

    self.first = tk.Label(
      self.create,
      text="First name : ",
      font=("Lucida Bright", 20),
      bg="lightblue"    
    )
    self.first_input = tk.Entry(
      self.create,
      font=("Lucida Bright", 20),
    )
    self.last = tk.Label(
      self.create,
      text="Last name : ",
      font=("Lucida Bright", 20),
      bg="lightblue"      
    )
    self.last_input = tk.Entry(
      self.create,
      font=("Lucida Bright", 20),
    )
    self.age = tk.Label(
      self.create,
      text="Age : ",
      font=("Lucida Bright", 20),
      bg="lightblue"    
    )
    self.age_input = tk.Entry(
      self.create,
      font=("Lucida Bright", 20),
    )
    self.contact = tk.Label(
      self.create,
      text="Contact : ",
      font=("Lucida Bright", 20),
      bg="lightblue"        
    )
    self.contact_input = tk.Entry(
      self.create,
      font=("Lucida Bright", 20),
    )
    self.Balance = tk.Label(
      self.create,
      text="Minimum Balance : ",
      font=("Lucida Bright", 20),
      bg="lightblue"        
    )
    self.Balance_input = tk.Entry(
      self.create,
      font=("Lucida Bright", 20),
    )
    self.submit_btn = tk.Button(
      self.create,
      text="Submit",
      font=("Lucida Bright", 20),
      command=self.submit,
    )
    self.back = tk.Button(
      self.create,
      text="Home",
      font=("Lucida Bright", 20),
      command=self.home
    )

    self.first.grid(
      column=0,
      row=0,
      pady=20
    )
    self.first_input.grid(
      column=1,
      row=0
    )
    self.last.grid(
      column=0,
      row=1,
      pady=20
    )
    self.last_input.grid(
      column=1,
      row=1
    )
    self.age.grid(
      column=0,
      row=2,
      pady=20
    )
    self.age_input.grid(
      column=1,
      row=2
    )
    self.contact.grid(
      column=0,
      row=3,
      pady=20
    )
    self.contact_input.grid(
      column=1,
      row=3
    )
    self.Balance.grid(
      column=0,
      row=4,
      pady=20
    )
    self.Balance_input.grid(
      column=1,
      row=4
    )
    self.submit_btn.grid(
      column=1,
      row=5,
      pady=10
    )
    self.back.grid(
      column=0,
      row=5,
      pady=10
    )

  def submit(self):
    data_frame = {
      'first name': [f"{self.first_input.get()}"],
      'last name': [f"{self.last_input.get()}"],
      'age': [f"{self.age_input.get()}"],
      'contact': [f"{self.contact_input.get()}"],
      'balance': [f"{self.Balance_input.get()}"],
      'user_id': [f"{id}"],
    }
    print("working") 
    print(data_frame)
    upload_file = pd.DataFrame(data_frame)
    upload_file.to_csv('user_data.csv', mode='a', index=False, header=False)
    return True
  
  def view_balance(self):
    for i in self.master.winfo_children():
      i.destroy()
    self.viewBalance = tk.Frame(
      bg="lightblue"
    )
    self.viewBalance.pack()
    print("view balance")

    self.account_details = {
      ''
    }

window.title("Bank MAnagement System")
window.geometry("1100x700")
window.resizable(False, False)
window.configure(bg="lightblue")

App(window)

window.mainloop()

