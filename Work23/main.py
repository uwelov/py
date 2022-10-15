from tkinter import *
import random
import datetime

global color, PlatSwitch, Time, start, Status
color= ["Blue","Red","Green"]
PlatSwitch = False
Time = [] #Храним время
start = 0
Status = False

game = Tk()
game.geometry("500x500")

#Подключение картинки в проект
BotImage = PhotoImage(file="MyBot.png")

textTime = Label(text="time")
textTime.place(x=650,y=50)

#Вывод картинки в проект
Bot = Label(image=BotImage)
Bot.place(x=350,y=350)

Btn = Button(width=800, bg=color[0])
Btn.place(y=750)

def click(ev):
    global PlatSwitch, Time, Status
    Status = False
    PlatSwitch = False
    TimeNow = datetime.datetime.now()
    Time.append(TimeNow.second)
    Btn.config(bg=color[0])
    '''
    if(Time[len(Time)-1] < Time[len(Time)-2]):
        first = 60 - Time[len(Time-2)]
        print(first+Time[len(Time-1)])
    else:
        print(int(Time[len(Time-1)])-int(Time[len(Time-2)]))
    '''
    textTime.config(text=Time)
    Time = []

def result(ev):
    global PlatSwitch, start, Status
    if (Status==False):
        if(PlatSwitch == False):
            start = datetime.datetime.now()
            Time.append(start.second)
            PlatSwitch = True
        if ((start.second + random.randint(2,6)) == datetime.datetime.now().second):
            Btn.config(bg=color[2])
            Status = True
        else:
            Btn.config(bg=color[1])

Bot.bind("<Button-1>",click)
Btn.bind("<Motion>",result)
game.mainloop()