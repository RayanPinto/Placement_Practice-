import re
from tkinter import messagebox
import tkinter as tk
def validate_inputs():
    name=ne.get().strip()
    email=ee.get().strip()
    password=pe.get().strip()
    if not name:
        messagebox.showerror("Error","Name cannot be empty")
        return
    if not email:
        messagebox.showerror("Error","Email cannot be empty")
        return 
    if not password:
        messagebox.showerror("Error", "Password cannot be empty")
        return
    email_pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0]{2,}$'
    if not re.match(email,email_pattern):
        messagebox.showerror("Error","invalid email found")
        return
    if not any(char.isdight() for char in password):
        messagebox.showerror("Error","password should have atleast 1 digit")
        return 
    if not any(char.isupper() for char in password):
        messagebox.showerror("Error","Password must atleast an uppercase letter ")
        return
    if len(password)<8:
        messagebox.showerror("Error","password must contain 8 characters")
        return 
    messagebox.showinfo("Success","form submitted ")
root=tk.Tk()
root.title("User registration form")
root.geometry("400x300")
tk.Label(root,text="Name:",font=("Arial",12)).pack(pady=5)
ne=tk.Entry(root,font=("Arial",12))
ne.pack(pady=5)
tk.Label(root,text="Email:",font=("Arial",12))
ee.pack(pady=5)
pe=tk.Entry(root,font=("Arial",12)).pack(pady=5)
tk.Label(root,text="Password:",font=("Arial",12))
ne.pack(pady=5)
ee=tk.Entry(root,font=("Arial",12)).pack(pady=5)
submit=tk.Button(root,text="Submit",command=validate_inputs,font=("Arial",12)).pack(pady=5)
root.mainloop()
