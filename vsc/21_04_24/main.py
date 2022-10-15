from tkinter import *

file = open('11.txt', 'a+', encoding='utf-8')
number = open('11.txt', encoding='utf-8')


root = Tk()
root.title('Msg')
root.geometry('600x400')

def add():
    file.write(txtBox.get()+'\n')
    info.config(text=(txtBox.get()+'\n'))

def clear():
    txtBox.delete(0, END)
    info.config(text="")

def maxValue():
    numMax = 0
    for x in number:
        if int(x) > numMax:
            numMax = int(x)
    info.config(text=numMax)

txtBox = Entry(width=100)
txtBox.pack()

click = Button(text='жмяк', bg='#ffffff', fg='#000000', width=10, height=1)
click.config(command=add)
click.pack(side=LEFT, padx=10, pady=15)

delt = Button(text='удалить', bg = '#ffffff', fg='#000000', width=10, height=1)
delt.config(command=clear)
delt.pack(side=RIGHT, padx=10, pady=15)

max = Button(text='макс', bg = '#ffffff', fg='#000000', width=10, height=1)
max.config(command=maxValue)
max.pack()

info = Label(font=30)
info.pack()

root.mainloop()