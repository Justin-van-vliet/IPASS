import random

import Bandit
import player_stats
import pygame
from Class import Class
from Slime import enemy_slime
from Lizerdman import enemy_lizardman
from Bandit import enemy_bandit
from Revenant import enemy_revenant
from Hellhound import enemy_hellhound
from mothman import enemy_mothman
from fenrir import boss_fenrir
from Golem import boss_golem
from Hydra import boss_hydra
from AI_vs_AI import *
from tkinter import *

root = Tk()
pygame.init()

#story chooser
def story_flux(enemy,player_HP):
    print(''
          'you are the chosen one, you must face evil and defeat it. now awaken! you hear as you wake up\n'
          f'you dont know where you are or who you are all you can figure out is that you are a {player_stats.player} based on youre clothing.\n'
          f'you look around and you appear to be n a field full of grass undeneath a blood red moon in the distance you see a village so u decide to ask around there.\n'
          f'u arrive at the village and ask where you are and what is going on with the unusual red moon in the sky.\n'
          f'the answer that you are in Satus and that a cult called sanguis lunae ruber is trying too summon there evil lord with some kind of ritual\n '
          f'and that is causing the red moon. then you remember that voice in you dream. you now know what you have to do\n'
          f'you ask where the cult is performing this ritual and set of to stop them.\n'
          f'but first you dicide to train a bit on a slime and you regain some of youre memories.\n'
          f'you remember that:\n'
          f'attack wins from dodge\n'
          f'dodge wins from magic\n'
          f'magic wins form block\n'
          f'and block wins from attack\n'
          f'')
    player_stats.enemy = 'slime'
    enemy_slime(player_FP,player_HP)
    print(' \n'
          'now that you defeated the slime you set of on youre adventure to stop sanguis lunae ruber\n'
          '')
    nexus = 0
    while nexus != 3 and player_stats.player_HP > 0:
        storys = random.choice(player_stats.storylist)
        if storys == 1:
            player_stats.enemy = 'bandit'
            player_stats.storylist.remove(1)
            nexus += 1
            print(''
                  'a you are walking trough a forest u feel like you are being watched.\n')
            if player_stats.player_DEX > 5:
                print('you sens that there are bandits around so you decide to be 1 step ahead of them and perform a sneak attack\n'
                      'if you perform a attack that is not magic now you will do extra damage\n'
                      '\n')
                player_stats.player_STR += 10
            else:
                print('but you dont know from where so you dicide to wait for them to attack you.\n'
                      '\n')
            enemy_bandit(player_FP,player_HP)
            player_stats.player_STR -=10
        elif storys == 2:
            player_stats.enemy = 'lizardman'
            player_stats.storylist.remove(2)
            nexus += 1
            print(''
                  'while trekking through a marsh you are suddenly spottedd by a lizardman\n'
                  'there is noway out of this you have to fight.\n'
                  '\n')
            enemy_lizardman(player_FP,player_HP)
        elif storys == 3:
            player_stats.enemy = 'revenant'
            player_stats.storylist.remove(3)
            nexus += 1
            print(''
                  'while passing trough what at first glance appears to be just a normal hamlet to a turn for the worst\n'
                  'it appears this hamlet is actually a ghost town and if that wasnt bad enough there are revenant everywhere\n'
                  '')
            if player_stats.player_DEX >= 7:
                print('fortunatly you are able to sneak by most of them. \n'
                      'still one revenant spotted you and engaged in combat.\n'
                      '\n')
                enemy_revenant(player_FP,player_HP)
            else:
                print('unfortunatly you are spotted by three of them and you have to engage in combat\n'
                      '\n')
                enemy_revenant(player_FP, player_HP)
                enemy_revenant(player_FP, player_HP)
                enemy_revenant(player_FP, player_HP)
        elif storys == 4:
            player_stats.enemy = 'hellhound'
            player_stats.storylist.remove(4)
            nexus += 1
            print('\n'
                  'will passing trough a large field full of tall grass you encounter a hellhound snarling at you\n'
                  'you try not to provoke it and go around, but the hellhound is out for blood an started attacking\n'
                  '')
            enemy_hellhound(player_FP,player_HP)
        elif storys == 5:
            player_stats.enemy = 'mothman'
            player_stats.storylist.remove(5)
            nexus += 1
            print('\n'
                  'while hiking around a mountian you a suddenly attack from a far fortunatly you are able to dodge it\n'
                  'you look around you to find the attacker and spot a mothman. youu decide to teach this adversary not to mess with you\n'
                  '\n')
            enemy_mothman(player_FP,player_HP)
    if nexus == 3:
        bosslist = ['golem', 'fenrir', 'hydra']
        boss = random.choice(bosslist)
        print('you finally arive at the church that sanguis lunae ruber is using for the ritual.\n'
              'u open the and are greeted by hooded figures. the head priest says to you:\n'
              'youre to late soon our dark lord shall be revived and he shall plundge this world in beautiful darkess\n'
              'and nobody can stop it. suddenly the hooded figures jump you and hold you down\n'
              f'you are forced to watch them summon a fierce {boss}\n'
              f'youre unable to stop the ritual but there is another way to stop the cult\n'
              f'you have to defeat the {boss}\n'
              f'\n')
        if boss == 'fenrir':
            print('')
            boss_fenrir(player_FP, player_HP)
            if player_stats.player_HP > 0:
                print(f'you defeated the {boss} and stop the cult. the moon turns back to normal and you saved the world\n'
                      f'you hev finished the game!\n'
                      f'thank you for playing\n')
        elif boss == 'hydra':
            print('')
            boss_hydra(player_FP, player_HP)
            if player_stats.player_HP > 0:
                print(f'you defeated the {boss} and stop the cult. the moon turns back to normal and you saved the world\n'
                      f'you hev finished the game!\n'
                      f'thank you for playing\n')
        elif boss == 'golem':
            print('')
            boss_golem(player_FP, player_HP)
            if player_stats.player_HP > 0:
                print(f'you defeated the {boss} and stop the cult. the moon turns back to normal and you saved the world\n'
                      f'you hev finished the game!\n'
                      f'thank you for playing\n')

def story(player_STR,player_INT,player_DEX,player_HP,player,choose,enemy):
    root.destroy()
    Class(player_STR,player_INT,player_DEX,player_HP,player,choose)
    print(story_flux(enemy,player_HP))
    if player_HP <= 0:
        you_died()
        return

def ai_vs_ai():
    fighter(choose, player_STR, player_INT, player_DEX, player_HP, player_FP, player, Shadow, shadow_STR,shadow_INT,
            shadow_DEX, shadow_HP, shadow_FP, shadow_class)
    battlebots(player_HP,shadow_HP)

def mainmenu():
    root.attributes('-fullscreen', True)
    img = PhotoImage(file='Boxart(clean).PNG')
    label1 = Label(master = root,
                   text='hello',
                   image= img)

    button = Button(master=root,
                    text = 'story mode',
                    command= lambda: story(player_STR, player_INT, player_DEX, player_HP, player, choose, player_stats.enemy))
    button2 = Button(master=root,
                     text='Ai vs Ai',
                     command= ai_vs_ai)
    button.grid()
    button.pack(padx= 10, pady= 10, side= BOTTOM)
    button2.pack(padx= 10, pady= 10, side= BOTTOM)
    label1.pack()
    root.mainloop()

def you_died():
    root = Tk()
    root.title("You Died")
    label = Label(master=root,
                  text="YOU DIED",
                  background="black",
                  foreground="red",
                  height= 100,
                  width=1000,
                  font=('castellar', 50))
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    #music by T_SquaredMusic on reddit via mewtwo on youtube
    pygame.mixer.music.load('Battle In The Sky (Team Sky Theme).mp3')
    pygame.mixer.music.play(-1)
    print(mainmenu())

