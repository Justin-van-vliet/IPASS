from tkinter import *
import random
from playsound import playsound

root = Tk()
storylist = [1, 2, 3, 4, 5]

def story_flux():
    nexus = 0
    while nexus < 3:
        storys = random.choice(storylist)
        if storys == 1:
            storylist.remove(1)
            nexus += 1
            print('1')
        elif storys == 2:
            storylist.remove(2)
            nexus += 1
            print('2')
        elif storys == 3:
            storylist.remove(3)
            nexus += 1
            print('3')
        elif storys == 4:
            storylist.remove(4)
            nexus += 1
            print('4')
        elif storys == 5:
            storylist.remove(5)
            nexus += 1
            print('5')
        print(storylist)

def story():
    print(story_flux())

def ai_vs_ai():
    global gamemode
    gamemode += 2

def mainmenu():
    label1 = Label(master = root,
                   text='hello',
                   background= 'black',
                   foreground='green',)

    button = Button(master=root,
                    text = 'story mode',
                    command= story)
    button2 = Button(master=root,
                     text='Ai vs Ai',
                     command= ai_vs_ai)
    button.grid()
    button.pack(padx= 10, pady= 10, side= BOTTOM)
    button2.pack(padx= 10, pady= 10, side= BOTTOM)
    label1.pack(pady=100, padx= 100)
    root.mainloop()

def you_died():
    img= PhotoImage(file= 'You DIED.png')
    label = Label(master=root,
                  image= img,)
    label.pack()
    root.mainloop()

print(mainmenu())