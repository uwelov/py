from tkinter import *
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")
for r in range(3):
    for c in range(3):
        btn = Button(text="1")
        btn.grid(row=r, column=c, ipadx=10, ipady=6, padx=10, pady=10)
        btn2 = Button(text="2")
        btn2.grid(row=r, column=c, ipadx=10, ipady=6, padx=10, pady=10)
root.mainloop()