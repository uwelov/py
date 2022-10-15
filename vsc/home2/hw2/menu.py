from tkinter import *
from tkinter import filedialog


def save_file():
    file_name = filedialog.asksaveasfilename(initialdir='/', title='Select file',
                                             filetypes=(('Text Documents', '*.txt'), ('all files', '*.*')))
    if file_name:
        f = open(file_name, 'w')
        text_save = str(text.get(1.0, END))
        f.write(text_save+'\n')
        f.close()


def open_file():
    file_name = filedialog.askopenfilename(initialdir='/', title='Open file',
                                           filetypes=(('Text Documents', '*.txt'), ('all files', '*.*')))
    if file_name:
        f = open(file_name, 'r')
        text_open = f.read()
        if text_open != NONE:
            text.delete(1.0, END)
            text.insert(END, text_open)

def new_file():
    text.delete(1.0, END)


root = Tk()
root.title('Untitled - Notepad')
root.geometry("300x250")
root.option_add('*Font', '{Times New Roman} 11')
root.option_add('*Background', 'gray')

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='New', command=new_file, font='{Times New Roman}')
file_menu.add_command(label='Open file as..', font='{Times New Roman}', command=open_file)
file_menu.add_command(label='Save file as..', font='{Times New Roman}', command=save_file)
file_menu.add_command(label='Exit', font='{Times New Roman}', command=exit)

help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label='Help', font='{Times New Roman}')
help_menu.add_command(label='About', font='{Times New Roman}')

menu.add_cascade(label='File', menu=file_menu, font='{Times New Roman}')
menu.add_cascade(label='Help', menu=help_menu, font='{Times New Roman}')

# Text
text = Text(root)
text.pack(expand=YES, fill=BOTH)

root.mainloop()