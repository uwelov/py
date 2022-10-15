from tkinter import *
root = Tk()
root.title('window')
root.geometry("300x250")

txtbox1 = Entry(width=30)
txtbox1.pack()

newTxt = Label(text='Введите Ваш год рождения', font=('Arial', 15, 'bold'))
newTxt.config(bd=15)
newTxt.pack()

def test():
    year = int(txtbox1.get())
    age = 2021 - year
    newTxt.config(text=age)

start = Button(text='тык', bg='#ffffff', fg='#000000', width=10, height=1)
start.config(command=test)
start.pack()

root.mainloop()