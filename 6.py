import re
from textblob import TextBlob
import tkinter as tk
def apply_theme(ss):
    if ss>0.2:
        root.configure(bg="lightyellow")
        res_lab.config(bg="lightyellow",fg="green",font=("Arial",12))
        return "Positive Mood:Bright colors,normal layout,standard font size"
    elif ss<0.2:
        root.configure(bg="lightblue")
        res_lab.config(bg="lightblue",fg="red",font=("Arial",14))
        return "Negative Mood"
    else:
        root.configure(bg="red")
        res_lab.config(bg="red",fg="red",font=("Arial",14))
        return "Neutral Mood"
def ismean(text):
        words=re.findall(r"[a-zA-z]+",text)
        return len(words)>0
def anal():
        sen=entry.get().strip()
        if not sen:
            res_lab.config(text="Please enter a sentence")
            return
        if not ismean(sen):
            res_lab.config(text="input does not sense")
            return
        analysis=TextBlob(sen)
        ss=analysis.sentiment.polarity
        if ss==0.0 :
            res_lab.config(text="Unable")
        theme_text=apply_theme(ss)
        res_lab.config(text=f"{ss:.2f}")
root=tk.Tk()
root.title("Adaptive UI")
root.geometry("700x800")
root.configure(bg="lightgrey")
tl=tk.Label(root,text="Enter you feeling",font=("Arial",14),bg="lightgrey")
tl.pack(pady=10)
entry=tk.Entry(root,font=("Arial",14),width=45)
entry.pack(pady=10)
ab=tk.Button(root,text="Analyze sentiment",command=anal,font=("Arial",14),bg="black",fg="white")
ab.pack(pady=10)
res_lab=tk.Label(root,text="",font=("Arial",12),wraplength=500,bg="lightgrey",justify="left")
res_lab.pack(pady=10)
root.mainloop()