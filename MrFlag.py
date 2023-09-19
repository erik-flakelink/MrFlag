from tkinter import *
import random

score = 0

def listy():
    list_o_flags = [
        ["us.png", "United States"],
        ["uk.png", "United Kingdom"],
        ["ru.png", "Russia"],
        ["pl.png", "Poland"],
        ["in.png", "India"],
        ["de.png", "Germany"]
    ]
    return list_o_flags

def backups():
    backup = [
        ["us.png", "United States"],
        ["uk.png", "United Kingdom"],
        ["ru.png", "Russia"],
        ["pl.png", "Poland"],
        ["in.png", "India"],
        ["de.png", "Germany"]
    ]
    return backup

choices = []

rooted = True

root = Tk()

def play():
    global rooted
    list_o_flags = listy()
    backup = backups()
    if rooted == True:
        root.destroy()
        rooted = False
    else:
        global root2
        root2.destroy()
    root2 = Tk()
    icon = PhotoImage(file="mrflagicon.png") 
    root2.iconphoto(False, icon)
    root2.title("Mr. Flag")
    country = random.randint(0, len(list_o_flags) - 1)
    img3 = PhotoImage(file=list_o_flags[country][0])
    choices.append(list_o_flags[country][1])
    del list_o_flags[country]
    options = 3
    canvas3= Canvas(root2, width = 125, height = 100)      
    canvas3.grid()
    canvas3.create_image(0,0, anchor=NW, image=img3)
    while options != 0:
        tbd = random.randint(0, len(list_o_flags) - 1)
        choices.append(list_o_flags[tbd][1])
        del list_o_flags[tbd]
        options -= 1
    print(choices)
    choices.sort()
    for i in choices:
        if i == backup[country][1]:
            btn = Button(root2, text=i, fg="black", bg="white", command=lvlup)
            btn.grid(column=0)
        else:
            btn = Button(root2, text=i, fg="black", bg="white")
            btn.grid(column=0)
    mainloop()

def lvlup():
    global score
    score = score + 1
    play()

icon = PhotoImage(file="mrflagicon.png") 
root.iconphoto(False, icon)
root.title("Mr. Flag")

canvas = Canvas(root, width = 244, height = 225)      
canvas.pack()  

img = PhotoImage(file="mrflag.png")
    
canvas.create_image(10,10, anchor=NW, image=img)     

btn_play = Button(root, text="PLAY", fg="black", bg="white", command=play)
btn_play.pack()

btn_exit = Button(root, text="EXIT", fg="black", bg="white", command=exit)
btn_exit.pack()

mainloop()
