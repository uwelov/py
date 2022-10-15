from tkinter import *

global x,y

height = 500
width = 500

x = ''
y = ''

root = Tk()
root.title('coord')
root.geometry("%dx%d" % (width, height))
root.resizable(False, False)


writen = Label(width=15)
writen.pack()

def func(ev):
    global x,y
    x = str(ev.x)
    y = str(ev.y)
    writen.config(text='x='+ x +', y='+ y)

root.bind('<Motion>',func)
root.mainloop()