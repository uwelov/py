from tkinter import *

height = 500
width = 500

global click

click = 0

x = []
y = []

window = Tk()
window.title('coord')
window.geometry("%dx%d" % (height, width))
window.resizable(False, False)

def touch():
    click+=1
    if click == 1:
        x[0] = event.x
        y[0] = event.y
    if click == 2:
        x[1] = event.x
        y[1] = event.y
    if click == 3:
        x[2] = event.x
        y[2] = event.y

window.bind('<Button-1>', touch)
window.mainloop()