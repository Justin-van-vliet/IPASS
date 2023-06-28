from acties import *
from CES import CES
from enemy_choser import get_enemies

enemy_HP = 1000
player_HP = 1000
PAC = []
PAP = []
enemy_action = ''
player = 'rogue'
enemy = 'bandit'

def AWESOME(PAC, PAP, enemy_HP, player_HP):
    APPE = True
    APS = True
    B = False
    while enemy_HP > 0 and player_HP > 0:
        if APS == True:
            get_enemies()
        if APPE == False:
            if B == False:
                if PAP != PAC:
                    APS = False
                    B = False
                    CES()
                    print('2')
        if APPE == True:
            if PAP != PAC:
                APPE = False
                B = True
                CES()
                print('3')
    PAP = [player_action]

AWESOME(PAC, PAP, enemy_HP, player_HP)