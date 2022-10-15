from tkinter import *
import random

WIDTH = 600
HEIGHT = 400

file = open('11.txt','a+', encoding='utf-8')
out = open('11.txt', encoding='utf-8')
   
window = Tk()
window.title('Login Form')
window.geometry("%dx%d" % (WIDTH, HEIGHT))
window.resizable(False, False)

def add():
    msg = TextBox.get()+'\n'
    file.write(msg)
    inform.config(text=out.readlines())

def clear():
    TextBox.config(text='')
    inform.config(text='')

def maxValue():
    Vmax = 0
    for x in out:
        if int(x) > Vmax:
            Vmax = int(x)
    maxValue.config(text=Vmax)

TextBox = Entry(width=500)
TextBox.pack()

btn_add = Button(text='Add info', command=add)
btn_add.pack()

btn_clear = Button(text='Clear info', command=clear)
btn_clear.pack()

btn_max = Button(text='Max', command=maxValue)
btn_max.pack()

inform = Label(font=30)
inform.pack()

maxValue = Label(font=50)
maxValue.pack()

window.mainloop()