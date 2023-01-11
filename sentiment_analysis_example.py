from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import tkinter as tk
from tkinter import ttk

def Run_B1():
    blob=TextBlob(T1.get(),analyzer=NaiveBayesAnalyzer())
    temp1=str(blob.sentiment)
    temp2=temp1.find("\'neg\'")
    if temp2 > 0:
        T2.set("Negative Sentence")
    else:
        T2.set("Positive Sentence")

main=tk.Tk()
main.title("Analyze the sentence")
main.geometry("500x250")

ttk.Label(main,text="Your Sentence").grid(column=0,row=0,sticky=tk.W)

T1=tk.StringVar()
TBox1 = ttk.Entry(main,width=50, textvariable=T1).grid(column=1,row=0)

button1=ttk.Button(main,text="ANALYZE",command=Run_B1).grid(column=1,row=1)

ttk.Label(main,text="Result").grid(column=0,row=2,sticky=tk.E)
T2=tk.StringVar()
TBox2=ttk.Entry(main,width=50,textvariable=T2).grid(column=1,row=2)

main.mainloop()
