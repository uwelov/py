from tkinter import *

def func():
    global num, mass, sum1, sum2, lblNum
    num = txtNum.get()
    for x in range(6):
        mass.append(int(num[x]))

    sum1 = mass[0] + mass[1] + mass[2]
    sum2 = mass[3] + mass[4] + mass[5]
    if sum1 == sum2:
        lblNum.config(text = 'Yes')
    else:
        lblNum.config(text='No')

global num, sum1, sum2, mass

num = 0
sum1 = 0
sum2 = 0
mass = []

root = Tk()
root.title('билетик')
root.geometry('500x500')

txtNum = Entry(font = '80', width = 30)
txtNum.pack()

butNum = Button(text = 'тык', width = 10, bg = 'black', fg = 'white', command = func)
butNum.pack()

lblNum = Label(font = '80', width = 30, fg = 'black')
lblNum.pack()


root.mainloop()