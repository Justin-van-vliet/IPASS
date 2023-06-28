import random

player_STR = 10
player_INT = 3
player_DEX = 4
player_HP = 125
player_FP = 100


PPA = []
PPA_attack = 0
PPA_block = 0
PPA_dodge = 0
PPA_magic = 0
PAC = []
PAP = []

player_action = ' '

def atempt(player_HP, history_current, history_previous):
    enemy_HP = 100
    actionlist = ['attack', 'block', 'magic', 'dodge']
    while enemy_HP > 0 and player_HP > 0:
        player_action = input('What will you do? attack,block, dodge or magic? ')
        if player_action == 'attack' or player_action == 'dodge' or player_action == 'block' or player_action == 'magic':
            PPA.append(player_action) #lijkt me niet nodig
            history_current.append(player_action)
        else:
            print('that is not a valid action.')
            player_action = input('What will you do? attack,block, dodge or magic(cost 25FP)? ')
            #hij moet hier opnieuw naar r24
        if len(PPA) > 3:
            PPA.remove(PPA[0])
        if len(history_current) > 1:
            history_current.remove([0])
        print(f'{history_current}\n'
              f'{history_previous}\n'
              f'{PPA}\n'
              f'{player_action}\n')
        if history_previous == history_current:
            if history_current[0] == 'attack':
                enemy_action = 'block'
                if enemy_action == 'block':
                    if player_action == 'attack':
                        damagelist_golem = range(40, 50)
                        damage = random.choice(damagelist_golem)
                        print(f'the golem block your attack and countered.\n'
                              f'the golem did {damage} points of damage.\n'
                              f'you have {player_HP - damage} left')
                        player_HP -= damage
                    if player_action == 'magic':
                        multiplier = float(player_INT * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(
                            f'the golem tried to block your attack, but the magic was to strong and hitted the enemy\n'
                            f'you did {player_damage} points of damage.\n'
                            f'the golem has {enemy_HP - player_damage} left')
                        enemy_HP -= player_damage
                    if player_action == 'dodge':
                        print('you dodged, but the golem blocked and so 0 points of damage to both.')
                    if player_action == 'block':
                        print('both you and the golem blocked')
            elif history_current[0] == 'dodge':
                enemy_action = 'attack'
                if enemy_action == 'attack':
                    if player_action == 'attack':
                        damagelist_golem = range(40, 50)
                        damage = random.choice(damagelist_golem)
                        multiplier = float(player_STR * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'both you and the golem attacked each other\n'
                              f'you did {player_damage} points of damage\n'
                              f'the golem has {enemy_HP - player_damage} left\n'
                              f'the golem did {damage} points of damage\n'
                              f'you have {player_HP - damage} left')
                        enemy_HP -= player_damage
                        player_HP -= damage
                    if player_action == 'magic':
                        damagelist_golem = range(40, 50)
                        damage = random.choice(damagelist_golem)
                        multiplier = float(player_INT * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'you cast a spell and the golem attacked. both you and the golem got hit\n'
                              f'you did {player_damage} points of damage\n'
                              f'the golem has {enemy_HP - player_damage} left\n'
                              f'the golem did {damage} points of damage\n'
                              f'you have {player_HP - damage} left')
                        player_HP -= damage
                        enemy_HP -= player_damage
                    if player_action == 'dodge':
                        damagelist_golem = range(40, 50)
                        damage = random.choice(damagelist_golem)
                        print(f'you dodged, but you dodge right in to the golem attack\n'
                              f'the golem did {damage} points of damage\n'
                              f'you have {player_HP - damage} left')
                        player_HP -= damage
                    if player_action == 'block':
                        if player_STR > player_INT:
                            multiplier = float(player_STR * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'you blocked the golem attack and countered it with a attack of youre own\n'
                                  f'you did {player_damage} points of damage\n'
                                  f'the golem has {enemy_HP - player_damage} left\n')
                            enemy_HP -= player_damage
                        elif player_STR < player_INT:
                            multiplier = float(player_INT * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'you blocked the golem attack and countered it with a magic spell\n'
                                  f'you did {player_damage} points of damage\n'
                                  f'the golem has {enemy_HP - player_damage} left\n')
                            enemy_HP -= player_damage
            elif history_current[0] == 'block':
                enemy_action = 'magic'
                if enemy_action == 'magic':
                    if player_action == 'attack':
                        damagelist_golem = range(40, 50)
                        damage = random.choice(damagelist_golem)
                        multiplier = float(player_STR * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'you attacked while the golem used magic. both got hit.\n'
                              f'you did {player_damage} points of damage\n'
                              f'the golem has {enemy_HP - player_damage} left\n'
                              f'the golem did {damage} points of damage\n'
                              f'you have {player_HP - damage} left')
                        player_HP -= enemy_HP
                        enemy_HP -= player_damage
                    if player_action == 'block':
                        damagelist_golem = range(40, 50)
                        damage = random.choice(damagelist_golem)
                        print(f'you tried to block, but the golem overwhelmed you with magic.\n'
                              f'the golem did {damage} points of damage.\n'
                              f'you have {player_HP - damage} left')
                        player_HP -= damage
                    if player_action == 'dodge':
                        multiplier = float(player_STR * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'you dodged the golem spell and countered it with a attack of youre own\n'
                              f'you did {player_damage} points of damage\n'
                              f'the golem has {enemy_HP - player_damage} left\n')
                        enemy_HP -= player_damage
                    if player_action == 'magic':
                        damagelist_golem = range(40, 50)
                        damage = random.choice(damagelist_golem)
                        multiplier = float(player_INT * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'both you and the golem cast spells and hit each other\n'
                              f'you did {player_damage} points of damage\n'
                              f'the golem has {enemy_HP - player_damage} left\n'
                              f'the golem did {damage} points of damage\n'
                              f'you have {player_HP - damage} left')
                        enemy_HP -= player_damage
                        player_HP -= damage
            elif history_current[0] == 'magic':
                enemy_action = 'dodge'
                if enemy_action == 'dodge':
                    if player_action == 'attack':
                        multiplier = float(player_STR * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'the golem dodged right into youre attack.\n'
                              f'you did {player_damage} points of damage\n'
                              f'the golem has {enemy_HP - player_damage} left\n')
                        enemy_HP -= player_damage
                    if player_action == 'dodge':
                        print('both you and the enemy dodged')
                    if player_action == 'block':
                        print('you blocked, but the golem dodged and so 0 points of damage to both.')
                    if player_action == 'magic':
                        damagelist_golem = range(40, 50)
                        damage = random.choice(damagelist_golem)
                        print(f'the golem dodged youre spell and performed a counter attack.\n'
                              f'the golem did {damage} points of damage\n'
                              f'you have {player_HP - damage} left\n')
                        player_HP -= damage
        elif history_current != history_previous:
            enemy_action = random.choice(actionlist)
            if enemy_action == 'block':
                if player_action == 'attack':
                    damagelist_golem = range(40, 50)
                    damage = random.choice(damagelist_golem)
                    print(f'the golem block your attack and counterattacked.\n'
                          f'the golem did {damage} points of damage.\n'
                          f' you have {player_HP - damage} left')
                    player_HP -= damage
                if player_action == 'magic':
                    multiplier = float(player_INT * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(
                        f'the golem tried to block your attack, but the magic was to strong and hitted the enemy\n'
                        f'you did {player_damage} points of damage.\n'
                        f'the golem has {enemy_HP - player_damage} left')
                    enemy_HP -= player_damage
                if player_action == 'dodge':
                    print('you dodged, but the golem blocked and so 0 points of damage to both.')
                if player_action == 'block':
                    print('both you and the golem blocked')
            if enemy_action == 'attack':
                if player_action == 'attack':
                    damagelist_golem = range(40, 50)
                    damage = random.choice(damagelist_golem)
                    multiplier = float(player_STR * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(f'both you and the golem attacked each other\n'
                          f'you did {player_damage} points of damage\n'
                          f'the golem has {enemy_HP - player_damage} left\n'
                          f'the golem did {damage} points of damage\n'
                          f'you have {player_HP - damage} left')
                    player_HP -= damage
                if player_action == 'magic':
                    damagelist_golem = range(40, 50)
                    damage = random.choice(damagelist_golem)
                    multiplier = float(player_INT * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(f'you cast a spell and the golem attacked. both you and the golem got hit\n'
                          f'you did {player_damage} points of damage\n'
                          f'the golem has {enemy_HP - player_damage} left\n'
                          f'the golem did {damage} points of damage\n'
                          f'you have {player_HP - damage} left')
                    player_HP -= damage
                if player_action == 'dodge':
                    damagelist_golem = range(40, 50)
                    damage = random.choice(damagelist_golem)
                    print(f'you dodged, but you dodge right in to the golem attack\n'
                          f'the golem did {damage} points of damage\n'
                          f'you have {player_HP - damage} left')
                    player_HP -= damage
                if player_action == 'block':
                    if player_STR > player_INT:
                        multiplier = float(player_STR * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'you blocked the golem attack and countered it with a attack of youre own\n'
                              f'you did {player_damage} points of damage\n'
                              f'the golem has {enemy_HP - player_damage} left\n')
                        enemy_HP -= player_damage
                    elif player_STR < player_INT:
                        multiplier = float(player_INT * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'you blocked the golem attack and countered it with a magic spell\n'
                              f'you did {player_damage} points of damage\n'
                              f'the golem has {enemy_HP - player_damage} left\n')
                        enemy_HP -= player_damage
            if enemy_action == 'magic':
                if player_action == 'attack':
                    damagelist_golem = range(40, 50)
                    damage = random.choice(damagelist_golem)
                    multiplier = float(player_STR * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(f'you attacked while the golem used magic. both got hit.\n'
                          f'you did {player_damage} points of damage\n'
                          f'the golem has {enemy_HP - player_damage} left\n'
                          f'the golem did {damage} points of damage\n'
                          f'you have {player_HP - damage} left')
                    player_HP -= damage
                    enemy_HP -= player_damage
                if player_action == 'block':
                    damagelist_golem = range(40, 50)
                    damage = random.choice(damagelist_golem)
                    print(f'you tried to block, but the golem overwhelmed you with magic.\n'
                          f'the golem did {damage} points of damage.\n'
                          f'you have {player_HP - damage} left')
                    player_HP -= damage
                if player_action == 'dodge':
                    multiplier = float(player_STR * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(f'you dodged the golems spell and countered it with a attack of youre own\n'
                          f'you did {player_damage} points of damage\n'
                          f'the golem has {enemy_HP - player_damage} left\n')
                    enemy_HP -= player_damage
                if player_action == 'magic':
                    damagelist_golem = range(40, 50)
                    damage = random.choice(damagelist_golem)
                    multiplier = float(player_INT * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(f'both you and the golem cast spells and hit each other\n'
                          f'you did {player_damage} points of damage\n'
                          f'the golem has {enemy_HP - player_damage} left\n'
                          f'the golem did {damage} points of damage\n'
                          f'you have {player_HP - damage} left')
                    enemy_HP -= player_damage
                    player_HP -= damage
            if enemy_action == 'dodge':
                if player_action == 'attack':
                    multiplier = float(player_STR * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(f'the golem dodged right into youre attack.\n'
                          f'you did {player_damage} points of damage\n'
                          f'the golem has {enemy_HP - player_damage} left\n')
                    enemy_HP -= player_damage
                if player_action == 'dodge':
                    print('both you and the golem dodged')
                if player_action == 'block':
                    print('you blocked, but the golem dodged and so 0 points of damage to both.')
                if player_action == 'magic':
                    damagelist_golem = range(40, 50)
                    damage = random.choice(damagelist_golem)
                    print(f'the golem dodged youre spell and performed a counter attack.\n'
                          f'the golem did {damage} points of damage\n'
                          f'you have {player_HP - damage} left\n')
                    player_HP -= damage
        history_previous = [player_action]
        history_current.clear()
        if enemy_HP <= 0:
            PPA.clear()
            history_current.clear()
            history_previous.clear()

PPA.clear()
atempt(player_HP, PAC, PAP)
