#pip install pyshorteners
import pyshorteners
from tkinter import *

win = Tk()
win.geometry("320x270")
win.configure(bg="lightblue")
#Button function
def short():
   url =entry1.get()
   s= pyshorteners.Shortener().tinyurl.short(url)

   entry2.insert(END,s)
#label for entering user url
Label(win,text="Enter Your URL Link",font="impack 17 bold",bg="darkblue",fg="white").pack(fill="x")
#Entry box
entry1=Entry(win,font="10",bd=3,width=40)
entry1.pack(pady=30)
#Button
Button(win,text="Click Me",font="impack 12 bold",bg="pink",fg="darkblue",width="14",command=short).pack()
entry2 = Entry(win,font="impack 16 bold",bg="lightblue",width=24,bd=0)
entry2.pack(pady=30)
mainloop()


