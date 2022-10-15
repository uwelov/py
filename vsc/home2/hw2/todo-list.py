from tkinter import *
from tkinter import messagebox
import random

HEIGHT = 600
WIDTH = 600

tasks = []


def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)


def add_task():
    task = text_input.get()
    if task != '':
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning('Warning', 'Enter the task in the input box, please.')
    text_input.delete(0, END)


def del_one():
    task = listbox.get('active')
    if task in tasks:
        tasks.remove(task)
    update_listbox()


def del_all():
    confirmed = messagebox.askyesno('Please Confirm', 'Do you really want to delete all?')
    if confirmed:
        global tasks
        tasks = []
        update_listbox()


def sort_asc():
    tasks.sort()
    update_listbox()


def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()


def choose_random():
    if len(tasks) > 0:
        task = random.choice(tasks)
        label_display['text'] = task
    else:
        messagebox.showwarning('Warning', 'No tasks')


def show_number_of_tasks():
    number_of_tasks = len(tasks)
    message = 'Number of tasks: %s' % number_of_tasks
    label_display['text'] = message


root = Tk()
root.title('My Super To-Do List')
root.geometry('%dx%d' % (WIDTH, HEIGHT))
root.resizable(False, False)
root.option_add('*Font', '{Times New Roman} 11')
root.option_add('*Background', 'gray')

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='Add task', command=add_task, font='{Times New Roman}')
file_menu.add_command(label='Delete', font='{Times New Roman}', command=del_one)
file_menu.add_command(label='Delete All', font='{Times New Roman}', command=del_all)
file_menu.add_command(label='Sort (A-Z)', font='{Times New Roman}', command=sort_asc)
file_menu.add_command(label='Sort (Z-A)', font='{Times New Roman}', command=sort_desc)
file_menu.add_command(label='Choose Random', font='{Times New Roman}', command=choose_random)
file_menu.add_command(label='Number of Tasks', font='{Times New Roman}', command=show_number_of_tasks)
file_menu.add_command(label='Exit', font='{Times New Roman}', command=exit)


img = PhotoImage(file='img/todo_bg.gif')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

root.option_add('*Font', '{Times New Roman} 10')
root.option_add('*Background', 'white')

frame = Frame(root, bd=10)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label_title = Label(frame, text='My Super To-Do List', fg='dark orange', font='{Times New Roman} 16', bg='green')
label_title.place(relx=0.3)

label_display = Label(frame, text='')
label_display.place(relx=0.3, rely=0.1)

text_input = Entry(frame, width=15)
text_input.place(relx=0.3, rely=0.15, relwidth=0.6)

listbox = Listbox(frame)
listbox.place(relx=0.3, rely=0.24, relwidth=0.6, relheight=0.6)

menu.add_cascade(label='MENU', menu=file_menu, font='{Times New Roman}')

root.mainloop()
