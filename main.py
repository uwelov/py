# Нем числительные до миллиона словами пишутся слитно, независимо от количества цифр
# Немного сложнее обстоит дело с двузначными числительными, здесь сначала идут единицы, а затем десятки, например, число 23 пишется и произносится как "три-и-двадцать".
# Также в нем есть умлауты и эсцет, но вместо умлаута я использовала обычную буквы, а эсцет как две ss
from tkinter import *

def func():
    global num, des, ost, entNum, lblNum, txtNum
    num = int(entNum.get())
    if num >= 20 :
        des = int(num / 10)
        ost = num % 10
        if ost == 1:
            txtNum+='einund'
        elif ost == 2:
            txtNum+='zweiund'
        elif ost == 3:
            txtNum+='dreiund'
        elif ost == 4:
            txtNum+='vierund'
        elif ost == 5:
            txtNum+='funfund'
        elif ost == 6:
            txtNum+='sechsund'
        elif ost == 7:
            txtNum+='siebenund'
        elif ost == 8:
            txtNum+='achtund'
        elif ost == 9:
            txtNum+='neunund'

        if des == 2:
            txtNum += 'zwanzig'
        elif des == 3:
            txtNum+= 'dreissig'
        elif des == 4:
            txtNum+= 'vierzig'
        elif des == 5:
            txtNum+= 'funfzig'
        elif des == 6:
            txtNum+= 'sechzig'
        elif des == 7:
            txtNum+= 'siebzig'
        elif des == 8:
            txtNum+= 'achtzig'
        elif des == 9:
            txtNum+= 'neunzig'

    elif num >= 10 and num <=19:
        ost = num % 10
        if ost == 3:
            txtNum+='drei'
        elif ost == 4:
            txtNum+='vier'
        elif ost == 5:
            txtNum+='funf'
        elif ost == 6:
            txtNum+='sechs'
        elif ost == 7:
            txtNum+='sieb'
        elif ost == 8:
            txtNum+='acht'
        elif ost == 9:
            txtNum+='neun'

        if num !=11 and num !=12:
            txtNum+='zehn'
        elif num == 11:
            txtNum+='elf'
        elif num == 12:
            txtNum+='zwolf'
    elif num < 10:
        if num == 0:
            txtNum+= 'null'
        elif num == 1:
            txtNum += 'eins'
        elif num == 2:
            txtNum+= 'zwei'
        elif num == 3:
            txtNum+= 'drei'
        elif num == 4:
            txtNum+= 'vier'
        elif num == 5:
            txtNum+= 'funf'
        elif num == 6:
            txtNum+= 'sechs'
        elif num == 7:
            txtNum+= 'sieben'
        elif num == 8:
            txtNum+= 'acht'
        elif num == 9:
            txtNum+= 'neun'

    lblNum.config(text=txtNum)
    txtNum = ''


global num, des, ost, txtNum

num = 0
des = 0
ost = 0
txtNum = ''


root = Tk()
root.title('билетик')
root.geometry('500x500')

entNum = Entry(font = '80', width = 30)
entNum.pack()

butNum = Button(text = 'тык', width = 10, bg = 'black', fg = 'white', command = func)
butNum.pack()

lblNum = Label(font = '80', width = 30, fg = 'black')
lblNum.pack()


root.mainloop()