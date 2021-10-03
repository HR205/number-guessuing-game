#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import *

win = tk.Tk()

mylabel = Label(win,text="Guess the Button",bg="aqua")
mylabel.grid(row=0, column=1)

def click_me1():
    B1.configure(text ="looser")
    mylabel.configure(text="13")
    
def click_me2():
    B2.configure(text= "looser")
    mylabel.configure(text= "49")
    
def click_me3():
    B3.configure(text ="winner")
    mylabel.confgure(text="10")
    mylabel.configure(bg= "yellow")
    
def click_me4():
    B4.configure(text ="looser")
    mylabel.configure(text ="69")
    
B1=Button(win,text="guess 10",bg="yellow",font=("Dnacing Script OT",14,"bold","italic"),underline=1)
B1.grid(row=1,column=1)


B2=Button(win,text="guess 10",bg="yellow",command=click_me2)
B2.grid(row=2,column=1)

B3=Button(win,text="guess 10",bg="yellow",command=click_me3)
B3.grid(row=3,column=1)

B4=Button(win,text="guess 10",bg="yellow",command=click_me4)
B4.grid(row=4,column=1)

win.mainloop() 


# In[ ]:




