from tkinter import messagebox 
mb=messagebox.showerror
mbb=messagebox.showinfo
import tkinter as tk
import re


def vi():
    n=ne.get().strip()
    e=ee.get().strip()
    p=pe.get().strip()
    if not n:
        mb("Error","fuck off")
        return
    if not e:
        mb("Error","fuck off")
        return
    ep=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(ep,e):
        mb("Error","asdfghj")
    if not p:
        mb("Error","fuck off")
        return
    if not any(ch.isdigit() for ch in p):
        mb("Error","fuck off")
        return
    if not any(ch.isupper() for ch in p):
        mb("Error","fuck off")
        return
    if len(p)<8:
        mb("Error","fuck off")
        return
    mbb.showinfo("Success","form submitted")
root=tk.Tk()
root.title("User registration form")
root.geometry("700x800")
tk.Label(root,font=("Arial",12),text="Name:").pack(pady=5)
ne=tk.Entry(root,font=("Arial",12))
ne.pack(pady=10)
tk.Label(root,font=("Arial",12),text="email:").pack(pady=5)
ee=tk.Entry(root,font=("Arial",12))
ee.pack(pady=10)
tk.Label(root,font=("Arial",12),text="password:").pack(pady=5)
pe=tk.Entry(root,font=("Arial",12))
pe.pack(pady=10)
submit=tk.Button(root,text="Button",command=vi,font=("Arial",12))
submit.pack(pady=10)
root.mainloop()