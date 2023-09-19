from tkinter import *
import random

official_flag_bank  = [
    "United States",
    "United Kingdom",
    "Russia",
    "Poland",
    "India",
    "Germany"
]

flag_bank  = [
    "United States",
    "United Kingdom",
    "Russia",
    "Poland",
    "India",
    "Germany"
]

temp_bank = []

list_o_flags = [
    ["us.png", "United States"],
    ["uk.png", "United Kingdom"],
    ["ru.png", "Russia"],
    ["pl.png", "Poland"],
    ["in.png", "India"],
    ["de.png", "Germany"]
]

root = Tk()

def play():
    root.destroy()
    root2 = Tk()
    icon = PhotoImage(file="mrflagicon.png") 
    root2.iconphoto(False, icon)
    root2.title("Mr. Flag")
    canvas2= Canvas(root2, width = 175, height = 175)      
    canvas2.grid()
    img2 = PhotoImage(file="mrflagneutral.png")
    canvas2.create_image(10,5, anchor=NW, image=img2)
    lbl_title = Label(root2, text="MR FLAG: \"Alright, let's see what you got.\"").grid(row=0, column=1)
    randomly_generated_country = random.randint(0, len(list_o_flags) - 1)
    img3 = PhotoImage(file=list_o_flags[randomly_generated_country][0])
    del flag_bank[randomly_generated_country]
    canvas3= Canvas(root2, width = 150, height = 150)      
    canvas3.grid()
    canvas3.create_image(10,5, anchor=NW, image=img3)
    temp_bank = []
    for i in flag_bank:
        temp_bank.append(i)
    while len(temp_bank) != 3:
        del temp_bank[-1]
    temp_bank.append(list_o_flags[randomly_generated_country][1])
    print(temp_bank)
    temp_bank.sort()
    for i in temp_bank:
        btn_quiz = Button(root2, text=i, fg="black", bg="white", command=exit)
        btn_quiz.grid(column=1)
    mainloop()


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
