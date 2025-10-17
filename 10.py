import tkinter as tk
import re
from textblob import TextBlob
def apply_theme(ss):
    if ss>0.2:
        root.configure(bg="lightyellow")
        res_lab.config(bg="lightyellow",fg="yellow",font=("Arial",14))
        return "Positive Mood"
    elif ss<-0.2:
        root.configure(bg="lightblue")
        res_lab.config(bg="lightblue",fg="green",font=("Arial",14))
        return "Negative Mood"
    else:
        root.configure(bg="red")
        res_lab.config(bg="red",fg="blue",font=("Arial",14))
        return "Neutral Mood"
def is_mean(text):
    w= re.findall(r'^[a-zA-Z]+',text)
    return len(w)>0
def analyze_sentiment():
    sen=entry.get().strip()
    if not sen:
        res_lab.config(text="enter sentence")
        return
    if not is_mean(sen):
        res_lab.config(text="Input does not make sense")
        return
    anal=TextBlob(sen)
    ss=anal.sentiment.polarity
    if ss==0.0 and len(sen.split())<=2:
        return
    theme=apply_theme(ss)
    res_lab.config(text=f"{ss:.2f}")
root=tk.Tk()
root.title("Fucker")
root.geometry("550x350")
root.configure(bg="lightgrey")
tl=tk.Label(root,text="Enter you sentence",font=("Arial",14)).pack(pady=10)
entry=tk.Entry(root,font=("Arial",14))
entry.pack(pady=10)
submit=tk.Button(root,text="Analyze",command=analyze_sentiment)
submit.pack(pady=10)
res_lab=tk.Label(root,text="",wraplength=500,justify="left",bg="purple")
res_lab.pack(pady=20)
root.mainloop()