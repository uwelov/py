# различие между кнопочкой "очистить" и "удалить"

# кнопочка "очистить" - очищает только одно число, которое ввели с ошибкой. все действия и прошлые числа сохраняются

# кнопочка "удалить" - удаляет весь результат, числа и действия

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('calculator')

global num1, num2, sign, click, s

s = ''
num1 = 0
num2 = 0
sign = ''
click = 0
r = ''

#чистка
def clear():
    global num1, num2, sign, s
    if sign == '':
        num1 = 0
        s = ''
        txtBox.config(text = '')
        print(num1, num2, sign)
    else:
        num2 = 0
        s = ''
        txtBox.config(text = '')
        print(num1, num2, sign)


def delete():
    confirmed = messagebox.askyesno('Пожалуйста подтвердите', 'Вы действительно хотите удалить все?')
    if confirmed:
        global num1, sign, num2, click, s
        num1 = 0
        num2 = 0
        sign = ''
        click = 0
        s = ''
        txtBox.config(text = '')
        print(num1, num2, sign, click)


# функции автом. ввода цифр
def one():
    global s
    s += str(1)
    txtBox.config(text = s)

def two():
    global s
    s += str(2)
    txtBox.config(text = s)

def three():
    global s
    s += str(3)
    txtBox.config(text = s)

def four():
    global s
    s += str(4)
    txtBox.config(text = s)

def five():
    global s
    s += str(5)
    txtBox.config(text = s)

def six():
    global s
    s += str(6)
    txtBox.config(text = s)

def seven():
    global s
    s += str(7)
    txtBox.config(text = s)

def eight():
    global s
    s += str(8)
    txtBox.config(text = s)

def nine():
    global s
    s += str(9)
    txtBox.config(text = s)

def zero():
    global s
    s += str(0)
    txtBox.config(text = s)

def nullNull():
    global s
    s += str(0)
    s += str(0)
    txtBox.config(text = s)

#def keyNum(ev):
#    global s
#    s += str(ev.char)
#    txtBox.config(text = s)

#ввод с клавиатуры
def keySign(ev):
    global r, click, s, num1, num2, sign
    r = str(ev.char)
    if r == '+':
        click += 1
        if click >= 2:
            num2 = int(s)
            num1 = num1 + num2
            num2 = 0
            s = ''
            r = ''
            txtBox.config(text = '')
            sign = '+'
            print(num1, sign)
        else:
            num1 = int(s)
            txtBox.config(text = '')
            sign = '+'
            s = ''
            r = ''
            print(num1, sign)
    elif r == '-':
        click += 1
        if click >= 2:
            num2 = int(s)
            num1 = num1 - num2
            num2 = 0
            s = ''
            r = ''
            txtBox.config(text = '')
            sign = '-'
            print(num1, sign)
        else:
            num1 = int(s)
            txtBox.config(text = '')
            sign = '-'
            s = ''
            r = ''
            print(num1, sign)
    elif r == '*':
        click += 1
        if click >= 2:
            num2 = int(s)
            num1 = num1 * num2
            num2 = 0
            s = ''
            r = ''
            txtBox.config(text = '')
            sign = '*'
            print(num1, sign)
        else:
            num1 = int(s)
            txtBox.config(text = '')
            sign = '*'
            s = ''
            r = ''
            print(num1, sign)
    elif r == '/':
        click += 1
        if click >= 2:
            num2 = int(s)
            num1 = num1 / num2
            num2 = 0
            s = ''
            r = ''
            txtBox.config(text = '')
            sign = '/'
            print(num1, sign)
        else:
            num1 = int(s)
            txtBox.config(text = '')
            sign = '/'
            s = ''
            r = ''
            print(num1, sign)
    elif r == '=':
        num2 = int(s)
        txtBox.config(text = '')
        if sign == '+':
            num1 = num1 + num2
            num2 = 0
            click = 0
            r = ''
            s = ''
            txtBox.config(text = num1)
            s = str(num1)
        elif sign == '-':
            num1 = num1 - num2
            num2 = 0
            click = 0
            r = ''
            s = ''
            txtBox.config(text = num1)
            s = str(num1)
        elif sign == '*':
            num1 = num1 * num2
            num2 = 0
            click = 0
            r = ''
            s = ''
            txtBox.config(text = num1)
            s = str(num1)
        elif sign == '/':
            num1 = num1 / num2
            num2 = 0
            click = 0
            r = ''
            s = ''
            txtBox.config(text = num1)
            s = str(num1)
    else:
        s += r
        txtBox.config(text = s)
        r = ''


# функции действий
def addit():
    global num1, sign, num2, click, s
    click += 1
    if click >= 2:
        num2 = int(s)
        num1 = num1 + num2
        num2 = 0
        s = ''
        txtBox.config(text = '')
        sign = '+'
        print(num1, sign)
    else:
        num1 = int(s)
        txtBox.config(text = '')
        sign = '+'
        s = ''
        print(num1, sign)


def subtr():
    global num1, sign, num2, click, s
    click += 1
    if click >= 2:
        num2 = int(s)
        num1 = num1 - num2
        num2 = 0
        s = ''
        txtBox.config(text = '')
        sign = '-'
        print(num1, sign)
    else:
        num1 = int(s)
        txtBox.config(text = '')
        sign = '-'
        s = ''
        print(num1, sign)


def multipl():
    global num1, sign, num2, click, s
    click += 1
    if click >= 2:
        num2 = int(s)
        num1 = num1 * num2
        num2 = 0
        s = ''
        txtBox.config(text = '')
        sign = '*'
        print(num1, sign)
    else:
        num1 = int(s)
        txtBox.config(text = '')
        sign = '*'
        s = ''
        print(num1, sign)


def divis():
    global num1, sign, num2, click, s
    click += 1
    if click >= 2:
        num2 = int(s)
        num1 = num1 / num2
        num2 = 0
        s = ''
        txtBox.config(text = '')
        sign = '/'
        print(num1, sign)
    else:
        num1 = int(s)
        txtBox.config(text = '')
        sign = '/'
        s = ''
        print(num1, sign)


def equally():
    global num1, sign, num2, click, s
    num2 = int(s)
    txtBox.config(text = '')
    if sign == '+':
        num1 = num1 + num2
        num2 = 0
        click = 0
        txtBox.config(text = num1)
        s = str(num1)
    elif sign == '-':
        num1 = num1 - num2
        num2 = 0
        click = 0
        txtBox.config(text = num1)
        s = str(num1)
    elif sign == '*':
        num1 = num1 * num2
        num2 = 0
        click = 0
        txtBox.config(text = num1)
        s = str(num1)
    elif sign == '/':
        num1 = num1 / num2
        num2 = 0
        click = 0
        txtBox.config(text = num1)
        s = str(num1)
    print(num1, sign, num2)


# textbox
txtBox = Label(width=30)
txtBox.grid(row=0, columnspan=4, sticky=W + E)

# block1
butCle = Button(text='Очистить', command=clear, font='serif 10')
butCle.grid(row=1, column=0, ipadx=0, ipady=5, padx=0, pady=5)

butDel = Button(text='Удалить', command=delete, font='serif 10')
butDel.grid(row=1, column=1, ipadx=0, ipady=5, padx=0, pady=5)

butClo = Button(text='Закрыть', command=exit, font='serif 10')
butClo.grid(row=1, column=3, ipadx=0, ipady=5, padx=0, pady=5)

# block2
but7 = Button(text='7', command=seven, font='serif 10')
but7.grid(row=2, column=0, ipadx=0, ipady=5, padx=0, pady=5)

but8 = Button(text='8', command=eight, font='serif 10')
but8.grid(row=2, column=1, ipadx=0, ipady=5, padx=0, pady=5)

but9 = Button(text='9', command=nine, font='serif 10')
but9.grid(row=2, column=2, ipadx=0, ipady=5, padx=0, pady=5)

butDiv = Button(text='/', command=divis, font='serif 10')
butDiv.grid(row=2, column=3, ipadx=0, ipady=5, padx=0, pady=5)

# block3
but4 = Button(command=four, text='4', font='serif 10')
but4.grid(row=3, column=0, ipadx=0, ipady=5, padx=0, pady=5)

but5 = Button(command=five, text='5', font='serif 10')
but5.grid(row=3, column=1, ipadx=0, ipady=5, padx=0, pady=5)

but6 = Button(command=six, text='6', font='serif 10')
but6.grid(row=3, column=2, ipadx=0, ipady=5, padx=0, pady=5)

butMult = Button(command=multipl, text='*', font='serif 10')
butMult.grid(row=3, column=3, ipadx=0, ipady=5, padx=0, pady=5)

# block4
but1 = Button(command=one, text='1', font='serif 10')
but1.grid(row=4, column=0, ipadx=0, ipady=5, padx=0, pady=5)

but2 = Button(command=two, text='2', font='serif 10')
but2.grid(row=4, column=1, ipadx=0, ipady=5, padx=0, pady=5)

but3 = Button(command=three, text='3', font='serif 10')
but3.grid(row=4, column=2, ipadx=0, ipady=5, padx=0, pady=5)

butSub = Button(command=subtr, text='-', font='serif 10')
butSub.grid(row=4, column=3, ipadx=0, ipady=5, padx=0, pady=5)

# block5
but0 = Button(command=zero, text='0', font='serif 10')
but0.grid(row=5, column=0, ipadx=0, ipady=5, padx=0, pady=5)

butNullNull = Button(command=nullNull, text='00', font='serif 10')
butNullNull.grid(row=5, column=1, ipadx=0, ipady=5, padx=0, pady=5)

butEqua = Button(command=equally, text='=', font='serif 10')
butEqua.grid(row=5, column=2, ipadx=0, ipady=5, padx=0, pady=5)

butAdd = Button(command=addit, text='+', font='serif 10')
butAdd.grid(row=5, column=3, ipadx=0, ipady=5, padx=0, pady=5)

#root.bind('<Key>', keyNum)
root.bind('<Key>', keySign)

root.mainloop()