# Нем числительные до миллиона словами пишутся слитно, независимо от количества цифр
# Немного сложнее обстоит дело с двузначными числительными, здесь сначала идут единицы, а затем десятки, например, число 23 пишется и произносится как "три-и-двадцать".
# Также в нем есть умлауты и эсцет, но вместо умлаута я использовала обычную буквы, а эсцет как две ss
from tkinter import *

def func():
    global num, des, ost, txtNum, lblNum
    num = int(txtNum.get())
    if num >= 10 :
        des = int(num / 10)
        ost = num % 10
        if des == 1:
            if ost == 0:
                lblNum.config(text = 'zehn')
            elif ost == 1:
                lblNum.config(text = 'elf')
            elif ost == 2:
                lblNum.config(text = 'zwolf')
            elif ost == 3:
                lblNum.config(text = 'dreizehn')
            elif ost == 4:
                lblNum.config(text = 'vierzenh')
            elif ost == 5:
                lblNum.config(text = 'funfzehn')
            elif ost == 6:
                lblNum.config(text = 'sechszenh')
            elif ost == 7:
                lblNum.config(text = 'siebzehn')
            elif ost == 8:
                lblNum.config(text ='achtzehn')
            elif ost == 9:
                lblNum.config(text ='neunzehn')
        elif des == 2:
            if ost == 0:
                lblNum.config(text = 'zwanzig')
            elif ost == 1:
                lblNum.config(text ='einundzwanzig')
            elif ost == 2:
                lblNum.config(text ='zweiundzwanzig')
            elif ost == 3:
                lblNum.config(text ='dreiundzwanzig')
            elif ost == 4:
                lblNum.config(text ='vierundzwanzig')
            elif ost == 5:
                lblNum.config(text ='funfundzwanzig')
            elif ost == 6:
                lblNum.config(text = 'sechsundzwanzig')
            elif ost == 7:
                lblNum.config(text = 'siebenundzwanzig')
            elif ost == 8:
                lblNum.config(text = 'achtundzwanzig')
            elif ost == 9:
                lblNum.config(text ='neunundzwanzig')
        elif des == 3:
            if ost == 0:
                lblNum.config(text = 'dreissig')
            elif ost == 1:
                lblNum.config(text = 'einunddreissig')
            elif ost == 2:
                lblNum.config(text = 'zweiunddreissig')
            elif ost == 3:
                lblNum.config(text = 'dreiunddreissig')
            elif ost == 4:
                lblNum.config(text = 'vierunddreissig')
            elif ost == 5:
                lblNum.config(text = 'funfunddreissig')
            elif ost == 6:
                lblNum.config(text = 'sechsunddreissig')
            elif ost == 7:
                lblNum.config(text = 'siebenunddreissig')
            elif ost == 8:
                lblNum.config(text = 'achtunddreissig')
            elif ost == 9:
                lblNum.config(text = 'neununddreissig')
        elif des == 4:
            if ost == 0:
                lblNum.config(text = 'vierzig')
            elif ost == 1:
                lblNum.config(text = 'einundvierzig')
            elif ost == 2:
                lblNum.config(text = 'zweiundvierzig')
            elif ost == 3:
                lblNum.config(text = 'dreiundvierzig')
            elif ost == 4:
                lblNum.config(text = 'vierundvierzig')
            elif ost == 5:
                lblNum.config(text = 'funfundvierzig')
            elif ost == 6:
                lblNum.config(text = 'sechsundvierzig')
            elif ost == 7:
                lblNum.config(text = 'siebenundvierzig')
            elif ost == 8:
                lblNum.config(text = 'achtundvierzig')
            elif ost == 9:
                lblNum.config(text = 'neunundvierzig')
        elif des == 5:
            if ost == 0:
                lblNum.config(text = 'funfzig')
            elif ost == 1:
                lblNum.config(text = 'einundfunfzig')
            elif ost == 2:
                lblNum.config(text = 'zweiundfunfzig')
            elif ost == 3:
                lblNum.config(text = 'dreiundfunfzig')
            elif ost == 4:
                lblNum.config(text = 'vierundfunfzig')
            elif ost == 5:
                lblNum.config(text = 'funfundfunfzig')
            elif ost == 6:
                lblNum.config(text = 'sechsundfunfzig')
            elif ost == 7:
                lblNum.config(text = 'siebenundfunfzig')
            elif ost == 8:
                lblNum.config(text = 'achtundfunfzig')
            elif ost == 9:
                lblNum.config(text = 'neunundfunfzig')
        elif des == 6:
            if ost == 0:
                lblNum.config(text = 'sechzig')
            elif ost == 1:
                lblNum.config(text = 'einundsechzig')
            elif ost == 2:
                lblNum.config(text = 'zweiundsechzig')
            elif ost == 3:
                lblNum.config(text = 'dreiundsechzig')
            elif ost == 4:
                lblNum.config(text = 'vierundsechzig')
            elif ost == 5:
                lblNum.config(text = 'funfundsechzig')
            elif ost == 6:
                lblNum.config(text = 'sechsundsechzig')
            elif ost == 7:
                lblNum.config(text = 'siebenundsechzig')
            elif ost == 8:
                lblNum.config(text = 'achtundsechzig')
            elif ost == 9:
                lblNum.config(text = 'neunundsechzig')
        elif des == 7:
            if ost == 0:
                lblNum.config(text = 'siebzig')
            elif ost == 1:
                lblNum.config(text = 'einundsiebzig')
            elif ost == 2:
                lblNum.config(text = 'zweiundsiebzig')
            elif ost == 3:
                lblNum.config(text = 'dreiundsiebzig')
            elif ost == 4:
                lblNum.config(text = 'vierundsiebzig')
            elif ost == 5:
                lblNum.config(text = 'funfundsiebzig')
            elif ost == 6:
                lblNum.config(text = 'sechsundsiebzig')
            elif ost == 7:
                lblNum.config(text = 'siebenundsiebzig')
            elif ost == 8:
                lblNum.config(text = 'achtundsiebzig')
            elif ost == 9:
                lblNum.config(text = 'neunundsiebzig')
        elif des == 8:
            if ost == 0:
                lblNum.config(text = 'achtzig')
            elif ost == 1:
                lblNum.config(text = 'einundachtzig')
            elif ost == 2:
                lblNum.config(text = 'zweiundachtzig')
            elif ost == 3:
                lblNum.config(text = 'dreiundachtzig')
            elif ost == 4:
                lblNum.config(text = 'vierundachtzig')
            elif ost == 5:
                lblNum.config(text = 'funfundachtzig')
            elif ost == 6:
                lblNum.config(text = 'sechsundachtzig')
            elif ost == 7:
                lblNum.config(text = 'siebenundachtzig')
            elif ost == 8:
                lblNum.config(text = 'achtundachtzig')
            elif ost == 9:
                lblNum.config(text = 'neunundachtzig')
        elif des == 9:
            if ost == 0:
                lblNum.config(text = 'neunzig')
            elif ost == 1:
                lblNum.config(text = 'einundneunzig')
            elif ost == 2:
                lblNum.config(text = 'zweiundneunzig')
            elif ost == 3:
                lblNum.config(text = 'dreiundneunzig')
            elif ost == 4:
                lblNum.config(text = 'vierundneunzig')
            elif ost == 5:
                lblNum.config(text = 'funfundneunzig')
            elif ost == 6:
                lblNum.config(text = 'sechsundneunzig')
            elif ost == 7:
                lblNum.config(text = 'siebenundneunzig')
            elif ost == 8:
                lblNum.config(text = 'achtundneunzig')
            elif ost == 9:
                lblNum.config(text = 'neunundneunzig')
    elif num < 10:
        if num == 0:
            lblNum.config(text = 'null')
        elif num == 1:
            lblNum.config(text = 'eins')
        elif num == 2:
            lblNum.config(text = 'zwei')
        elif num == 3:
            lblNum.config(text = 'drei')
        elif num == 4:
            lblNum.config(text = 'vier')
        elif num == 5:
            lblNum.config(text = 'funf')
        elif num == 6:
            lblNum.config(text = 'sechs')
        elif num == 7:
            lblNum.config(text = 'sieben')
        elif num == 8:
            lblNum.config(text = 'acht')
        elif num == 9:
            lblNum.config(text = 'neun')

global num, des, ost

num = 0
des = 0
ost = 0

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