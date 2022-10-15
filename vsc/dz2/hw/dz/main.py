from tkinter import *
import math

height = 500
width = 500

root = Tk()
root.title('calculator')
root.geometry("%dx%d" % (height, width))
root.resizable(False, False)

txtBox = Entry(width=30)
txtBox.place(relx=0.4, rely=0.2, relheight=0.1, relwidth=0.55)
txtBox.pack()

global num1, num2, sign

num1 = 0
num2 = 0
sign = ''

#функции автом. ввода цифр
def one():
    txtBox.insert(0, '1')

def two():
    txtBox.insert(0, '2')

def three():
    txtBox.insert(0, '3')

def four():
    txtBox.insert(0, '4')

def five():
    txtBox.insert(0, '5')

def six():
    txtBox.insert(0, '6')

def seven():
    txtBox.insert(0, '7')

def eight():
    txtBox.insert(0, '8')

def nine():
    txtBox.insert(0, '9')

def zero():
    txtBox.insert(0, '0')

#функции действий
def addit():
    global num1, sign
    num1 = int(txtBox.get())
    txtBox.delete(0, END)
    sign = '+'
    print(num1, sign)


def subtr():
    global num1, sign
    num1 = int(txtBox.get())
    txtBox.delete(0, END)
    sign = '-'
    print(num1, sign)

def multipl():
    global num1, sign
    num1 = int(txtBox.get())
    txtBox.delete(0, END)
    sign = '*'
    print(num1, sign)

def divis():
    global num1, sign
    num1 = int(txtBox.get())
    txtBox.delete(0, END)
    sign = '/'
    print(num1, sign)

def equally():
    global num1, sign, num2
    num2 = int(txtBox.get())
    if sign == '+':
        res.config(text = num1+num2)
    elif sign == '-':
        res.config(text = num1 - num2)
    elif sign == '*':
        res.config(text = num1 * num2)
    elif sign == '/':
        res.config(text= math.ceil(num1 / num2))
    print(num1, sign, num2)

#кнопки-действия
butAdd = Button(command = addit, text = '+',  width=10, height=1)
butAdd.place()
butAdd.pack()

butSub = Button(command = subtr, text = '-',  width=10, height=1)
butSub.pack()

butMult = Button(command = multipl, text = '*',  width=10, height=1)
butMult.pack()

butDiv = Button(command = divis, text = '/',  width=10, height=1)
butDiv.pack()

butEqua = Button(command = equally, text = '=',  width=10, height=1)
butEqua.pack()

#вывод инфы
res = Label(width=10, height=1, text = '', fg = 'black')
res.pack()

#кнопки-цифры
#btn = Button(text="1".format(r,c))
#btn.grid(row=r, column=c, ipadx=10, ipady=6, padx=10, pady=10)
but1 = Button(command = one, text = '1', padx = 1, pady = 1)
#but1.grid(row = 0, column = 0, ipadx = 10, ipady = 6, padx = 10, pady = 1)
but1.pack()


but2 = Button(command = two, text = '2', padx = 1, pady = 1)
but2.pack()

but3 = Button(command = three, text = '3', padx = 1, pady = 1)
but3.pack()

but4 = Button(command = four, text = '4', padx = 1, pady = 1)
but4.pack()

but5 = Button(command = five, text = '5', padx = 1, pady = 1)
but5.pack()

but6 = Button(command = six, text = '6', padx = 1, pady = 1)
but6.pack()

but7 = Button(command = seven, text = '7', padx = 1, pady = 1)
but7.pack()

but8 = Button(command = eight, text = '8', padx = 1, pady = 1)
but8.pack()

but9 = Button(command = nine, text = '9', padx = 1, pady = 1)
but9.pack()

but0 = Button(command = zero, text = '0', padx = 1, pady = 1)
but0.pack()

root.mainloop()