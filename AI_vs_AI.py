import random

player_STR = 0
player_INT = 0
player_DEX = 0
player_HP = 100
player_FP = 100
choose = 0
player = ''
player_action = ''
Shadow = 0
shadow_STR = 0
shadow_INT = 0
shadow_DEX = 0
shadow_HP = 100
shadow_FP = 100
shadow_class = ''
gamemode =0
winnerlist = []

#players previous actions
PPA = []
PPA_attack = 0
PPA_block = 0
PPA_dodge = 0
PPA_magic = 0
TPA = []
PSA = []
SPA_attack = 0
SPA_block = 0
SPA_dodge = 0
SPA_magic = 0
coin_log = []

def fighter(choose, player_STR, player_INT, player_DEX, player_HP, player_FP, player, Shadow, shadow_STR,shadow_INT,
            shadow_DEX, shadow_HP, shadow_FP, shadow_class):
    classes = [1, 2, 3]
    choose += random.choice(classes)
    if choose == 1:
        print('class: warrior\n'
              'STR = 10\n'
              'INT = 3\n'
              'DEX = 4\n'
              'HP = 125\n')
        player = 'warrior'
        player_STR += 10
        player_INT += 3
        player_DEX += 4
        player_HP += 25
    elif choose == 2:
        print('class: mage\n'
              'STR = 2\n'
              'INT = 10\n'
              'DEX = 6\n'
              'FP = 125\n')
        player = 'mage'
        player_STR += 2
        player_INT += 10
        player_DEX += 6
        player_FP += 25
    elif choose == 3:
        print('class: rogue\n'
              'STR = 4\n'
              'INT = 5\n'
              'DEX = 9\n')
        player = 'rogue'
        player_STR += 4
        player_INT += 5
        player_DEX += 9
    Shadow += random.choice(classes)
    if Shadow == 1:
        print('class: warrior\n'
              'STR = 10\n'
              'INT = 3\n'
              'DEX = 4\n'
              'HP = 125\n')
        shadow_class = 'warrior'
        shadow_STR += 10
        shadow_INT += 3
        shadow_DEX += 4
        shadow_HP += 25
    elif Shadow == 2:
        print('class: mage\n'
              'STR = 2\n'
              'INT = 10\n'
              'DEX = 6\n'
              'FP = 125\n')
        shadow_class = 'mage'
        shadow_STR += 2
        shadow_INT += 10
        shadow_DEX += 6
        shadow_FP += 25
    elif Shadow == 3:
        print('class: rogue\n'
              'STR = 4\n'
              'INT = 5\n'
              'DEX = 9\n')
        shadow_class = 'rogue'
        shadow_STR += 4
        shadow_INT += 5
        shadow_DEX += 9

def battlebots(player_HP, shadow_HP):
    actionlist = ['attack', 'block', 'magic', 'dodge']
    while shadow_HP > 0 and player_HP > 0:
        player_action = random.choice(actionlist)
        enemy_action = random.choice(actionlist)
        PPA.append(player_action)
        PSA.append(enemy_action)
        TPA.append(player_action)
        if len(PPA) > 3:
            PPA.remove(PPA[0])
        print(PPA)
        if len(PSA) > 3:
            PSA.remove(PSA[0])
        print(PSA)
        coin = [1, 2]
        coin_log.append(coin)
        x = coin.count(1)
        y = coin.count(2)
        if x > y:
            coin.append(1)
        elif x < y:
            coin.append(2)
        if x == y:
            coin_toss = random.choice(coin)
        PPA_attack = PPA.count('attack')
        PPA_block = PPA.count('block')
        PPA_dodge = PPA.count('dodge')
        PPA_magic = PPA.count('magic')
        if PPA_attack <= 1 and PPA_magic <= 1 and PPA_dodge <= 1 and PPA_block <= 1:

            if enemy_action == 'block':
                if player_action == 'attack':
                    multiplierX = float(shadow_STR * 0.01) + 1
                    damagelist = range(5, 40)
                    shadow_damage = random.choice(damagelist) * multiplierX
                    print(f'the enemy block your attack and counterattacked.\n'
                        f'enemy did {shadow_damage} points of damage.\n'
                        f' you have {player_HP - shadow_damage} left')
                    player_HP -= shadow_damage
                if player_action == 'magic':
                    multiplier = float(player_INT * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(f'the enemy tried to block your attack, but the magic was to strong and hitted the enemy\n'
                        f'you did {player_damage} points of damage.\n'
                        f'enemy has {shadow_HP - player_damage} left')
                    shadow_HP -= player_damage
                if player_action == 'dodge':
                    print('you dodged, but the enemy blocked and so 0 points of damage to both.')
                if player_action == 'block':
                    print('both you and the enemy blocked')
            if enemy_action == 'attack':
                if player_action == 'attack':
                    multiplierX = float(shadow_STR * 0.01) + 1
                    damagelist = range(5, 40)
                    shadow_damage = random.choice(damagelist) * multiplierX
                    multiplier = float(player_STR * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(f'both you and the enemy attacked each other\n'
                          f'you did {player_damage} points of damage\n'
                          f'enemy has {shadow_HP - player_damage} left\n'
                          f'enemy did {shadow_damage} points of damage\n'
                          f'you have {player_HP - shadow_damage} left')
                    player_HP -= shadow_damage
                    shadow_HP -= player_damage
                if player_action == 'magic':
                    multiplierX = float(shadow_STR * 0.01) + 1
                    damagelist = range(5, 40)
                    shadow_damage = random.choice(damagelist) * multiplierX
                    multiplier = float(player_INT * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(f'you cast a spell and the enemy attacked. both you and the enemy got hit\n'
                          f'you did {player_damage} points of damage\n'
                          f'enemy has {shadow_HP - player_damage} left\n'
                          f'enemy did {shadow_damage} points of damage\n'
                          f'you have {player_HP - shadow_damage} left')
                    player_HP -= shadow_damage
                    shadow_HP -= shadow_damage
                if player_action == 'dodge':
                    multiplierX = float(shadow_STR * 0.01) + 1
                    damagelist = range(5, 40)
                    shadow_damage = random.choice(damagelist) * multiplierX
                    print(f'you dodged, but you dodge right in to the enemy attack\n'
                          f'enemy did {shadow_damage} points of damage\n'
                          f'you have {player_HP - shadow_damage} left')
                    player_HP -= shadow_damage
                if player_action == 'block':
                    if player_STR > player_INT:
                        multiplier = float(player_STR * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'you blocked the enemy attack and countered it with a attack of youre own\n'
                              f'you did {player_damage} points of damage\n'
                              f'enemy has {shadow_HP - player_damage} left\n')
                        shadow_HP -= player_damage
                    elif player_STR < player_INT:
                        multiplier = float(player_INT * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'you blocked the enemy attack and countered it with a magic spell\n'
                              f'you did {player_damage} points of damage\n'
                              f'enemy has {shadow_HP - player_damage} left\n')
                        shadow_HP -= player_damage
            if enemy_action == 'magic':
                if player_action == 'attack':
                    multiplierX = float(shadow_INT * 0.01) + 1
                    damagelist = range(5, 40)
                    shadow_damage = random.choice(damagelist) * multiplierX
                    multiplier = float(player_STR * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(f'you attacked while the enemy used magic. both got hit.\n'
                          f'you did {player_damage} points of damage\n'
                          f'enemy has {shadow_HP - player_damage} left\n'
                          f'enemy did {shadow_damage} points of damage\n'
                          f'you have {player_HP - shadow_damage} left')
                    player_HP -= shadow_damage
                    shadow_HP -= player_damage
                if player_action == 'block':
                    multiplierX = float(shadow_INT * 0.01) + 1
                    damagelist = range(5, 40)
                    shadow_damage = random.choice(damagelist) * multiplierX
                    print(f'you tried to block, but the enemy overwhelmed you with magic.\n'
                          f'enemy did {shadow_damage} points of damage.\n'
                          f' you have {player_HP - shadow_damage} left')
                    player_HP -= shadow_damage
                if player_action == 'dodge':
                    multiplier = float(player_STR * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(f'you dodged the enemy spell and countered it with a attack of youre own\n'
                          f'you did {player_damage} points of damage\n'
                          f'enemy has {shadow_HP - player_damage} left\n')
                    shadow_HP -= player_damage
                if player_action == 'magic':
                    multiplierX = float(shadow_INT * 0.01) + 1
                    damagelist = range(5, 40)
                    shadow_damage = random.choice(damagelist) * multiplierX
                    multiplier = float(player_INT * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(f'both you and the enemy cast spells and hit each other\n'
                          f'you did {player_damage} points of damage\n'
                          f'enemy has {shadow_HP - player_damage} left\n'
                          f'enemy did {shadow_damage} points of damage\n'
                          f'you have {player_HP - shadow_damage} left')
                    shadow_HP -= player_damage
                    player_HP -= shadow_damage
            if enemy_action == 'dodge':
                if player_action == 'attack':
                    multiplier = float(player_STR * 0.01) + 1
                    damagelist_player = range(5, 40)
                    player_damage = random.choice(damagelist_player) * multiplier
                    print(f'the enemy dodged right into youre attack.\n'
                          f'you did {player_damage} points of damage\n'
                          f'enemy has {shadow_HP - player_damage} left\n')
                    shadow_HP -= player_damage
                if player_action == 'dodge':
                    print('both you and the enemy dodged')
                if player_action == 'block':
                    print('you blocked, but the enemy dodged and so 0 points of damage to both.')
                if player_action == 'magic':
                    multiplierX = float(shadow_INT * 0.01) + 1
                    damagelist = range(5, 40)
                    shadow_damage = random.choice(damagelist) * multiplierX
                    print(f'the enemy dodged your spell and countered.\n'
                          f'enemy did {shadow_damage} points of damage.\n'
                          f' you have {player_HP - shadow_damage} left')
                    player_HP -= shadow_damage
        coin = [1, 2]
        coin_log.append(coin)
        x = coin.count(1)
        y = coin.count(2)
        if x > y:
            coin.append(1)
        elif x < y:
            coin.append(2)
        if x == y:
            coin_toss = random.choice(coin)
        if coin_toss == 1:
            if len(PPA) > 1:
                PPA_attack = PPA.count('attack')
                PPA_block = PPA.count('block')
                PPA_dodge = PPA.count('dodge')
                PPA_magic = PPA.count('magic')
                if PPA_attack >= 2:
                    enemy_action = 'block'
                    if enemy_action == 'block':
                        if player_action == 'attack':
                            multiplierX = float(shadow_STR * 0.01) + 1
                            damagelist = range(5, 40)
                            shadow_damage = random.choice(damagelist) * multiplierX
                            print(f'the enemy block your attack and countered.\n'
                                f'enemy did {shadow_damage} points of damage.\n'
                                f' you have {player_HP - shadow_damage} left')
                            player_HP -= shadow_damage
                        if player_action == 'magic':
                            multiplier = float(player_INT * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(
                                f'the enemy tried to block your attack, but the magic was to strong and hitted the enemy\n'
                                f'you did {player_damage} points of damage.\n'
                                f'enemy has {shadow_HP - player_damage} left')
                            shadow_HP -= player_damage
                        if player_action == 'dodge':
                            print('you dodged, but the enemy blocked and so 0 points of damage to both.')
                        if player_action == 'block':
                            print('both you and the enemy blocked')
                if PPA_dodge >= 2:
                    enemy_action = 'attack'
                    if enemy_action == 'attack':
                        if player_action == 'attack':
                            multiplierX = float(shadow_STR * 0.01) + 1
                            damagelist = range(5, 40)
                            shadow_damage = random.choice(damagelist) * multiplierX
                            multiplier = float(player_STR * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'both you and the enemy attacked each other\n'
                                  f'you did {player_damage} points of damage\n'
                                  f'enemy has {shadow_HP - player_damage} left\n'
                                  f'enemy did {shadow_damage} points of damage\n'
                                  f'you have {player_HP - shadow_damage} left')
                            shadow_HP -= player_damage
                            player_HP -= shadow_damage
                        if player_action == 'magic':
                            multiplierX = float(shadow_STR * 0.01) + 1
                            damagelist = range(5, 40)
                            shadow_damage = random.choice(damagelist) * multiplierX
                            multiplier = float(player_INT * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'you cast a spell and the enemy attacked. both you and the enemy got hit\n'
                                  f'you did {player_damage} points of damage\n'
                                  f'enemy has {shadow_HP - player_damage} left\n'
                                  f'enemy did {shadow_damage} points of damage\n'
                                  f'you have {player_HP - shadow_damage} left')
                            player_HP -= shadow_damage
                            shadow_HP -= player_damage
                        if player_action == 'dodge':
                            multiplierX = float(shadow_STR * 0.01) + 1
                            damagelist = range(5, 40)
                            shadow_damage = random.choice(damagelist) * multiplierX
                            print(f'you dodged, but you dodge right in to the enemy attack\n'
                                  f'enemy did {shadow_damage} points of damage\n'
                                  f'you have {player_HP - shadow_damage} left')
                            player_HP -= shadow_damage
                        if player_action == 'block':
                            if player_STR > player_INT:
                                multiplier = float(player_STR * 0.01) + 1
                                damagelist_player = range(5, 40)
                                player_damage = random.choice(damagelist_player) * multiplier
                                print(f'you blocked the enemy attack and countered it with a attack of youre own\n'
                                      f'you did {player_damage} points of damage\n'
                                      f'enemy has {shadow_HP - player_damage} left\n')
                                shadow_HP -= player_damage
                            elif player_STR < player_INT:
                                multiplier = float(player_INT * 0.01) + 1
                                damagelist_player = range(5, 40)
                                player_damage = random.choice(damagelist_player) * multiplier
                                print(f'you blocked the enemy attack and countered it with a magic spell\n'
                                      f'you did {player_damage} points of damage\n'
                                      f'enemy has {shadow_HP - player_damage} left\n')
                                shadow_HP -= player_damage
                if PPA_block >= 2:
                    enemy_action = 'magic'
                    if enemy_action == 'magic':
                        if player_action == 'attack':
                            multiplierX = float(shadow_INT * 0.01) + 1
                            damagelist = range(5, 40)
                            shadow_damage = random.choice(damagelist) * multiplierX
                            multiplier = float(player_STR * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'you attacked while the enemy used magic. both got hit.\n'
                                  f'you did {player_damage} points of damage\n'
                                  f'enemy has {shadow_HP - player_damage} left\n'
                                  f'enemy did {shadow_damage} points of damage\n'
                                  f'you have {player_HP - shadow_damage} left')
                            player_HP -= shadow_damage
                            shadow_HP -= player_damage
                        if player_action == 'block':
                            multiplierX = float(shadow_INT * 0.01) + 1
                            damagelist = range(5, 40)
                            shadow_damage = random.choice(damagelist) * multiplierX
                            print(f'you tried to block, but the enemy overwhelmed you with magic.\n'
                                  f'enemy did {shadow_damage} points of damage.\n'
                                  f'you have {player_HP - shadow_damage} left')
                            player_HP -= shadow_damage
                        if player_action == 'dodge':
                            multiplier = float(player_STR * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'you dodged the enemy spell and countered it with a attack of youre own\n'
                                  f'you did {player_damage} points of damage\n'
                                  f'enemy has {shadow_HP - player_damage} left\n')
                            shadow_HP -= player_damage
                        if player_action == 'magic':
                            multiplierX = float(shadow_INT * 0.01) + 1
                            damagelist = range(5, 40)
                            shadow_damage = random.choice(damagelist) * multiplierX
                            multiplier = float(player_INT * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'both you and the enemy cast spells and hit each other\n'
                                  f'you did {player_damage} points of damage\n'
                                  f'enemy has {shadow_HP - player_damage} left\n'
                                  f'enemy did {shadow_damage} points of damage\n'
                                  f'you have {player_HP - shadow_damage} left')
                            shadow_HP -= player_damage
                            player_HP -= shadow_damage
                if PPA_magic >= 2:
                    enemy_action = 'dodge'
                    if enemy_action == 'dodge':
                        if player_action == 'attack':
                            multiplier = float(player_STR * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'the enemy dodged right into youre attack.\n'
                                  f'you did {player_damage} points of damage\n'
                                  f'enemy has {shadow_HP - player_damage} left\n')
                            shadow_HP -= player_damage
                        if player_action == 'dodge':
                            print('both you and the enemy dodged')
                        if player_action == 'block':
                            print('you blocked, but the enemy dodged and so 0 points of damage to both.')
                        if player_action == 'magic':
                            multiplierX = float(shadow_INT * 0.01) + 1
                            damagelist = range(5, 40)
                            shadow_damage = random.choice(damagelist) * multiplierX
                            print(f'the revenant dodged your spell and countered.\n'
                                  f'revenant did {shadow_damage} points of damage.\n'
                                  f' you have {player_HP - shadow_damage} left')
                            player_HP -= shadow_damage
        if coin_toss == 2:
            if SPA_attack >= 2:
                player_action = 'block'
                if player_action == 'block':
                    if enemy_action == 'attack':
                        multiplier = float(player_STR * 0.01) + 1
                        damagelist = range(5, 40)
                        player_damage = random.choice(damagelist) * multiplier
                        print(f'you block the attack and countered.\n'
                            f'you did {player_damage} points of damage.\n'
                            f'enemy has {shadow_HP - player_damage} left')
                        shadow_HP -= player_damage
                    if enemy_action == 'magic':
                        multiplierX = float(shadow_INT * 0.01) + 1
                        damagelist = range(5, 40)
                        shadow_damage = random.choice(damagelist) * multiplierX
                        print(
                            f'you tried to block the attack, but the magic was to strong and hitted you\n'
                            f'enemy did {shadow_damage} points of damage.\n'
                            f'you have {player_HP - shadow_damage} left')
                        player_HP -= shadow_damage
                    if enemy_action == 'dodge':
                        print('you dodged, but the enemy blocked and so 0 points of damage to both.')
                    if enemy_action == 'block':
                        print('both you and the enemy blocked')
            if SPA_dodge >= 2:
                player_action = 'attack'
                if player_action == 'attack':
                    if enemy_action == 'attack':
                        multiplierX = float(shadow_STR * 0.01) + 1
                        damagelist = range(5, 40)
                        shadow_damage = random.choice(damagelist) * multiplierX
                        multiplier = float(player_STR * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'both you and the enemy attacked each other\n'
                            f'you did {player_damage} points of damage\n'
                            f'enemy has {shadow_HP - player_damage} left\n'
                              f'enemy did {shadow_damage} points of damage\n'
                              f'you have {player_HP - shadow_damage} left')
                        shadow_HP -= player_damage
                        player_HP -= shadow_damage
                    if enemy_action == 'magic':
                        multiplierX = float(shadow_STR * 0.01) + 1
                        damagelist = range(5, 40)
                        shadow_damage = random.choice(damagelist) * multiplierX
                        multiplier = float(player_INT * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'you cast a spell and the enemy attacked. both you and the enemy got hit\n'
                            f'you did {player_damage} points of damage\n'
                            f'enemy has {shadow_HP - player_damage} left\n'
                            f'enemy did {shadow_damage} points of damage\n'
                            f'you have {player_HP - shadow_damage} left')
                        player_HP -= shadow_damage
                        shadow_HP -= player_damage
                    if enemy_action == 'dodge':
                        multiplier = float(shadow_STR * 0.01) + 1
                        damagelist = range(5, 40)
                        player_damage = random.choice(damagelist) * multiplier
                        print(f'the enemy dodged, but you dodge right in to youre attack\n'
                              f'you did {player_damage} points of damage\n'
                              f'enemy has {shadow_HP - player_damage} left')
                        shadow_HP -= player_damage
                    if enemy_action == 'block':
                        if player_STR > player_INT:
                            multiplierX = float(shadow_STR * 0.01) + 1
                            damagelist_player = range(5, 40)
                            shadow_damage = random.choice(damagelist_player) * multiplierX
                            print(f'the enemy blocked yiu attack and countered it with a attack of youre own\n'
                                  f'enemy did {shadow_damage} points of damage\n'
                                  f'you have {player_HP - shadow_damage} left\n')
                            player_HP -= shadow_damage
                        elif player_STR < player_INT:
                            multiplierX = float(player_INT * 0.01) + 1
                            damagelist_player = range(5, 40)
                            shadow_damage = random.choice(damagelist_player) * multiplierX
                            print(f'the enemy blocked youre attack and countered it with a magic spell\n'
                                  f'enemy did {shadow_damage} points of damage\n'
                                  f'you has {player_HP - shadow_damage} left\n')
                            player_HP -= shadow_damage
            if SPA_block >= 2:
                player_action = 'magic'
                if player_action == 'magic':
                    if enemy_action == 'attack':
                        multiplierX = float(shadow_STR * 0.01) + 1
                        damagelist = range(5, 40)
                        shadow_damage = random.choice(damagelist) * multiplierX
                        multiplier = float(player_INT * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'the enemy attacked while you used magic. both got hit.\n'
                              f'you did {player_damage} points of damage\n'
                                f'enemy has {shadow_HP - player_damage} left\n'
                              f'enemy did {shadow_damage} points of damage\n'
                              f'you have {player_HP - shadow_damage} left')
                        player_HP -= shadow_damage
                        shadow_HP -= player_damage
                    if player_action == 'block':
                        multiplier = float(shadow_INT * 0.01) + 1
                        damagelist = range(5, 40)
                        player_damage = random.choice(damagelist) * multiplier
                        print(f'the enemy tried to block, but the enemy overwhelmed you with magic.\n'
                              f'enemy did {player_damage} points of damage.\n'
                              f'you have {shadow_HP - player_damage} left')
                        shadow_HP -= player_damage
                    if player_action == 'dodge':
                        multiplierX = float(player_STR * 0.01) + 1
                        damagelist_player = range(5, 40)
                        shadow_damage = random.choice(damagelist_player) * multiplierX
                        print(f'the enemy dodged youre spell and countered it with a attack of youre own\n'
                              f'enemy did {shadow_damage} points of damage\n'
                              f'you have {player_HP - shadow_damage} left\n')
                        player_HP -= shadow_damage
                    if player_action == 'magic':
                        multiplierX = float(shadow_INT * 0.01) + 1
                        damagelist = range(5, 40)
                        shadow_damage = random.choice(damagelist) * multiplierX
                        multiplier = float(player_INT * 0.01) + 1
                        damagelist_player = range(5, 40)
                        player_damage = random.choice(damagelist_player) * multiplier
                        print(f'both you and the enemy cast spells and hit each other\n'
                              f'you did {player_damage} points of damage\n'
                              f'enemy has {shadow_HP - player_damage} left\n'
                              f'enemy did {shadow_damage} points of damage\n'
                              f'you have {player_HP - shadow_damage} left')
                        shadow_HP -= player_damage
                        player_HP -= shadow_damage
            if SPA_magic >= 2:
                player_action = 'dodge'
                if player_action == 'dodge':
                    if enemy_action == 'attack':
                        multiplierX = float(player_STR * 0.01) + 1
                        damagelist_player = range(5, 40)
                        shadow_damage = random.choice(damagelist_player) * multiplierX
                        print(f'you dodged right into the enemy attack.\n'
                              f'enemy did {shadow_damage} points of damage\n'
                              f'you have {player_HP - shadow_damage} left\n')
                        player_HP -= shadow_damage
                    if player_action == 'dodge':
                        print('both you and the enemy dodged')
                    if player_action == 'block':
                        print('you blocked, but the enemy dodged and so 0 points of damage to both.')
                    if player_action == 'magic':
                        multiplier = float(shadow_INT * 0.01) + 1
                        damagelist = range(5, 40)
                        player_damage = random.choice(damagelist) * multiplier
                        print(f'you dodged your spell and countered.\n'
                              f'you did {player_damage} points of damage.\n'
                              f'enemy have {shadow_HP - player_damage} left')
                        shadow_HP -= player_damage
    a = open('winners', 'a')
    if shadow_HP <= 0:
        PPA.clear()
        PSA.clear()
        coin_log.clear()
        print('youre fighter won')
        a.write('fighter\n')
        a.close()
    elif player_HP <= 0:
        PPA.clear()
        PSA.clear()
        coin_log.clear()
        print('youre enemy has won')
        a.write('enemy\n')
        a.close()
    elif player_HP and shadow_HP <= 0:
        PPA.clear()
        PSA.clear()
        coin_log.clear()
        print('both have died')
        a.write('draw\n')
        a.close()
