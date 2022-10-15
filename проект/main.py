from tkinter import *

# insert text

def insert():
    entry.insert(0, 'Hello ')

#delete text

def delete():
    entry.delete(0, END)

# creation_window

root = Tk()
root.title('Widgets')
root.geometry('200x140')

# label

label = Label(text='Say hello!', font=('Arial', 16, 'bold'))
label.config(bd=10)
label.pack()

# entry

entry = Entry(width=30)
entry.pack()

#create button1

button1 = Button(text='Click me', bg='#ffffff', fg='#000000', width=10, height=1)
button1.config(command=insert)
button1.pack(side=LEFT, padx=10, pady=15)

#create button1

button2 = Button(text='Delete', bg = '#ffffff', fg='#000000', width=10, height=1)
button2.config(command=delete)
button2.pack(side=RIGHT, padx=10, pady=15)

root.mainloop()