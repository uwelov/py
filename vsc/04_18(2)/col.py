from tkinter import *
root = Tk()
root.title('Colors')
root.geometry('180x310')

def aliceBlue():
    newText.config(text='AliceBlue')
    txtBox.delete(0, END)
    txtBox.insert(0, '#f0f8ff')

def antiqueWhite():
    newText.config(text='AntiqueWhite')
    txtBox.delete(0, END)
    txtBox.insert(0, '#faebd7')

def antiqueWhite1():
    newText.config(text='AntiqueWhite1')
    txtBox.delete(0, END)
    txtBox.insert(0, '#ffefdb')

def antiqueWhite2():
    newText.config(text='AntiqueWhite2')
    txtBox.delete(0, END)
    txtBox.insert(0, '#eedfcc')

def antiqueWhite3():
    newText.config(text='AntiqueWhite3')
    txtBox.delete(0, END)
    txtBox.insert(0, '#cdc0b0')

def antiqueWhite4():
    newText.config(text='AntiqueWhite4')
    txtBox.delete(0, END)
    txtBox.insert(0, '#8b8378')

def aquamarine1():
    newText.config(text='Aquamarine1')
    txtBox.delete(0, END)
    txtBox.insert(0, '#7fffd4')

def aquamarine2():
    newText.config(text='Aquamarine2')
    txtBox.delete(0, END)
    txtBox.insert(0, '#76eec6')

def aquamarine4():
    newText.config(text='Aquamarine4')
    txtBox.delete(0, END)
    txtBox.insert(0, '#458b74')

def azure1():
    newText.config(text='Azure1')
    txtBox.delete(0, END)
    txtBox.insert(0, '#f0ffff')

newText = Label(root, anchor='c')
newText.pack()

txtBox = Entry(root, justify='center', bd=5)
txtBox.pack()

col1 = Button(width=16, bg='#f0f8ff', command=aliceBlue)
col1.pack()

col2 = Button(width=16, bg='#faebd7', command=antiqueWhite)
col2.pack()

col3 = Button(width=16, bg='#ffefdb', command=antiqueWhite1)
col3.pack()

col4 = Button(width=16, bg='#eedfcc', command=antiqueWhite2)
col4.pack()

col5 = Button(width=16, bg='#cdc0b0', command=antiqueWhite3)
col5.pack()

col6 = Button(width=16, bg='#8b8378', command=antiqueWhite4)
col6.pack()

col7 = Button(width=16, bg='#7fffd4', command=aquamarine1)
col7.pack()

col8 = Button(width=16, bg='#76eec6', command=aquamarine2)
col8.pack()

col9 = Button(width=16, bg='#458b74', command=aquamarine4)
col9.pack()

col10 = Button(width=16, bg='#f0ffff', command=azure1)
col10.pack()

root.mainloop()