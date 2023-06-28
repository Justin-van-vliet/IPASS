import random

actionlist = ['attack','block','magic','dodge']
player= ''
PAC = []
PAP = []

def CES():
    global PAC,PAP,enemy_action
    if player == 'warrior':
        enemy_action = 'block'
        print('werkt')
    elif player == 'mage':
        enemy_action = 'dodge'
        print('werkt')
    else:
        if PAP != PAC:
            enemy_action = random.choice(actionlist)
        if PAC[0] == 'attack':
            enemy_action = 'block'
            print('werkt')
        if PAC[0] == 'block':
            enemy_action = 'magic'
            print('werkt')
        if PAC[0] == 'magic':
            enemy_action = 'dodge'
            print('werkt')
        if PAC[0] == 'dodge':
            enemy_action = 'attack'
            print('werkt')