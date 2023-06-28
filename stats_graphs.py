import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image, ImageTk

def actions():
    a = open('stats.txt')
    f = a.readlines()
    tpa_attack = f.count('attack\n')
    tpa_dodge = f.count('dodge\n')
    tpa_block = f.count('block\n')
    tpa_magic = f.count('magic\n')
    activities = ['attack', 'dodge', 'block', 'magic']
    slices = [tpa_attack, tpa_dodge, tpa_block, tpa_magic]
    colors = ['r', 'y', 'g', 'b']
    fig, ax = plt.subplots(figsize=(8, 6))  # Set the width and height of the figure
    ax.pie(slices, labels=activities, colors=colors,
           startangle=90, shadow=True, explode=(0, 0, 0.1, 0),
           radius=1.2, autopct='%1.1f%%')
    plt.savefig('actions.png')
    plt.close()
    a.close()


def show_actions():
    print(actions())
    root = Tk()
    img_actions= ImageTk.PhotoImage(Image.open("actions.png"))
    label = Label(master=root, image=img_actions)
    label.pack()
    root.mainloop()


def winners():
    a = open('winners')
    f = a.readlines()
    fighter = f.count('fighter\n')
    shadow = f.count('enemy\n')
    activities = ['fighter', 'enemy']
    slices = [fighter, shadow,]
    colors = ['r', 'b']
    fig, ax = plt.subplots(figsize=(8, 6))  # Set the width and height of the figure
    ax.pie(slices, labels=activities, colors=colors,
           startangle=90, shadow=True, explode=(0, 0),
           radius=1.2, autopct='%1.1f%%')
    plt.savefig('winners.png')
    plt.close()
    a.close()

def show_winners():
    global img_winner
    print(winners())
    root = Tk()
    img_winner = ImageTk.PhotoImage(Image.open("winners.png"))
    label = Label(master=root, image=img_winner)
    label.pack()
    root.mainloop()

answer = input('do you want to see your actions stats or your AI_vs_AI winner stats? action or winner ')
if answer == 'winner':
    show_winners()
if answer == 'action':
    show_actions()