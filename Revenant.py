import random
from Experience import EXP
import player_stats

player_actionlist = ['attack', 'dodge', 'block', 'magic']
player_action = ' '
enemy = 'revenant'

def enemy_revenant(player_FP, player_HP):
    if enemy == 'revenant':
        enemy_HP = 30
        actionlist = ['attack','block','magic','dodge']
        with open('stats.txt', 'a') as tpa:
            try:
                while enemy_HP > 0 and player_stats.player_HP > 0:
                    player_action = input('What will you do? attack,block, dodge or magic? ')
                    if player_action == 'attack' or player_action == 'dodge' or player_action == 'block' or player_action == 'magic':
                        player_stats.PPA.append(player_action)
                        tpa.write(player_action+'\n')
                    else:
                        print('that is not a valid action.')
                        player_action = input('What will you do? attack,block, dodge or magic? ')
                        player_stats.PPA.append(player_action)
                        tpa.write(player_action + '\n')
                    if len(player_stats.PPA) > 3:
                        player_stats.PPA.remove(player_stats.PPA[0])
                    print(player_stats.PPA)
                    player_stats.PPA_attack = player_stats.PPA.count('attack')
                    player_stats.PPA_block = player_stats.PPA.count('block')
                    player_stats.PPA_dodge = player_stats.PPA.count('dodge')
                    player_stats.PPA_magic = player_stats.PPA.count('magic')
                    if player_stats.PPA_attack <= 1 and player_stats.PPA_magic <= 1 and player_stats.PPA_dodge <= 1 and player_stats.PPA_block <= 1:
                        AI_action = random.choice(actionlist)
                        if AI_action == 'block':
                            if player_action == 'attack':
                                damagelist_revenant = range(30, 60)
                                damage = random.choice(damagelist_revenant)
                                print(f'the revenant block your attack and counterattacked.\n'
                                      f'revenant did {damage} points of damage.\n'
                                      f' you have {player_stats.player_HP - damage} left')
                                player_stats.player_HP -= damage
                            if player_action == 'magic':
                                multiplier = float(player_stats.player_INT * 0.01) + 1
                                damagelist_player = range(5, 40)
                                player_damage = random.choice(damagelist_player) * multiplier
                                print(
                                    f'the revenant tried to block your attack, but the magic was to strong and hitted the enemy\n'
                                    f'you did {player_damage} points of damage.\n'
                                    f'revenant has {enemy_HP - player_damage} left')
                                enemy_HP -= player_damage
                            if player_action == 'dodge':
                                print('you dodged, but the revenant blocked and so 0 points of damage to both.')
                            if player_action == 'block':
                                print('both you and the revenant blocked')
                        if AI_action == 'attack':
                            if player_action == 'attack':
                                damagelist_revenant = range(30, 60)
                                damage = random.choice(damagelist_revenant)
                                multiplier = float(player_stats.player_STR * 0.01) + 1
                                damagelist_player = range(5, 40)
                                player_damage = random.choice(damagelist_player) * multiplier
                                print(f'both you and the revenant attacked each other\n'
                                      f'you did {player_damage} points of damage\n'
                                      f'revenant has {enemy_HP - player_damage} left\n'
                                      f'revenant did {damage} points of damage\n'
                                      f'you have {player_stats.player_HP - damage} left')
                                player_stats.player_HP -= damage
                            if player_action == 'magic':
                                damagelist_revenant = range(30, 60)
                                damage = random.choice(damagelist_revenant)
                                multiplier = float(player_stats.player_INT * 0.01) + 1
                                damagelist_player = range(5, 40)
                                player_damage = random.choice(damagelist_player) * multiplier
                                print(f'you cast a spell and the revenant attacked. both you and the revenant got hit\n'
                                      f'you did {player_damage} points of damage\n'
                                      f'revenant has {enemy_HP - player_damage} left\n'
                                      f'revenant did {damage} points of damage\n'
                                      f'you have {player_stats.player_HP - damage} left')
                                player_stats.player_HP -= damage
                            if player_action == 'dodge':
                                damagelist_revenant = range(30, 60)
                                damage = random.choice(damagelist_revenant)
                                print(f'you dodged, but you dodge right in to the revenants attack\n'
                                      f'revenant did {damage} points of damage\n'
                                      f'you have {player_stats.player_HP - damage} left')
                                player_stats.player_HP -= damage
                            if player_action == 'block':
                                if player_stats.player_STR > player_stats.player_INT:
                                    multiplier = float(player_stats.player_STR * 0.01) + 1
                                    damagelist_player = range(5, 40)
                                    player_damage = random.choice(damagelist_player) * multiplier
                                    print(f'you blocked the revenants attack and countered it with a attack of youre own\n'
                                          f'you did {player_damage} points of damage\n'
                                          f'revenant has {enemy_HP - player_damage} left\n')
                                    enemy_HP -= player_damage
                                elif player_stats.player_STR < player_stats.player_INT:
                                    multiplier = float(player_stats.player_INT * 0.01) + 1
                                    damagelist_player = range(5, 40)
                                    player_damage = random.choice(damagelist_player) * multiplier
                                    print(f'you blocked the revenants attack and countered it with a magic spell\n'
                                          f'you did {player_damage} points of damage\n'
                                          f'revenant has {enemy_HP - player_damage} left\n')
                                    enemy_HP -= player_damage
                        if AI_action == 'magic':
                            if player_action == 'attack':
                                damagelist_revenant = range(30, 60)
                                damage = random.choice(damagelist_revenant)
                                multiplier = float(player_stats.player_STR * 0.01) + 1
                                damagelist_player = range(5, 40)
                                player_damage = random.choice(damagelist_player) * multiplier
                                print(f'you attacked while the revenant used magic. both got hit.\n'
                                      f'you did {player_damage} points of damage\n'
                                      f'revenant has {enemy_HP - player_damage} left\n'
                                      f'revenant did {damage} points of damage\n'
                                      f'you have {player_stats.player_HP - damage} left')
                                player_stats.player_HP -= damage
                                enemy_HP -= player_damage
                            if player_action == 'block':
                                damagelist_revenant = range(30, 60)
                                damage = random.choice(damagelist_revenant)
                                print(f'you tried to block, but the revenant overwhelmed you with magic.\n'
                                      f'revenant did {damage} points of damage.\n'
                                      f' you have {player_stats.player_HP - damage} left')
                                player_HP -= damage
                            if player_action == 'dodge':
                                multiplier = float(player_stats.player_STR * 0.01) + 1
                                damagelist_player = range(5, 40)
                                player_damage = random.choice(damagelist_player) * multiplier
                                print(f'you dodged the revenants spell and countered it with a attack of youre own\n'
                                      f'you did {player_damage} points of damage\n'
                                      f'revenant has {enemy_HP - player_damage} left\n')
                                enemy_HP -= player_damage
                            if player_action == 'magic':
                                damagelist_revenant = range(30, 60)
                                damage = random.choice(damagelist_revenant)
                                multiplier = float(player_stats.player_INT * 0.01) + 1
                                damagelist_player = range(5, 40)
                                player_damage = random.choice(damagelist_player) * multiplier
                                print(f'both you and the revenant cast spells and hit each other\n'
                                      f'you did {player_damage} points of damage\n'
                                      f'revenant has {enemy_HP - player_damage} left\n'
                                      f'revenant did {damage} points of damage\n'
                                      f'you have {player_stats.player_HP - damage} left')
                                enemy_HP -= player_damage
                                player_stats.player_HP -= damage
                        if AI_action == 'dodge':
                            if player_action == 'attack':
                                multiplier = float(player_stats.player_STR * 0.01) + 1
                                damagelist_player = range(5, 40)
                                player_damage = random.choice(damagelist_player) * multiplier
                                print(f'the revenant dodged right into youre attack.\n'
                                      f'you did {player_damage} points of damage\n'
                                      f'revenant has {enemy_HP - player_damage} left\n')
                                enemy_HP -= player_damage
                            if player_action == 'dodge':
                                print('both you and the revenant dodged')
                            if player_action == 'block':
                                print('you blocked, but the revenant dodged and so 0 points of damage to both.')
                            if player_action == 'magic':
                                damagelist_revenant = range(30, 60)
                                damage = random.choice(damagelist_revenant)
                                print(f'the revenant dodged your spell and countered.\n'
                                      f'revenant did {damage} points of damage.\n'
                                      f' you have {player_stats.player_HP - damage} left')
                                player_stats.player_HP -= damage
                    else:
                        if player_stats.PPA_attack >= 2:
                            AI_action = 'block'
                            if AI_action == 'block':
                                if player_action == 'attack':
                                    damagelist_revenant = range(30, 60)
                                    damage = random.choice(damagelist_revenant)
                                    print(f'the revenant block your attack and countered.\n'
                                          f'revenant did {damage} points of damage.\n'
                                          f' you have {player_HP - damage} left')
                                    player_HP -= damage
                                if player_action == 'magic':
                                    multiplier = float(player_stats.player_INT * 0.01) + 1
                                    damagelist_player = range(5, 40)
                                    player_damage = random.choice(damagelist_player) * multiplier
                                    print(f'the revenant tried to block your attack, but the magic was to strong and hitted the enemy\n'
                                          f'you did {player_damage} points of damage.\n'
                                          f'revenant has {enemy_HP - player_damage} left')
                                    enemy_HP -= player_damage
                                if player_action == 'dodge':
                                    print('you dodged, but the revenant blocked and so 0 points of damage to both.')
                                if player_action == 'block':
                                    print('both you and the revenant blocked')
                        if player_stats.PPA_dodge >= 2:
                            AI_action = 'attack'
                            if AI_action == 'attack':
                                if player_action == 'attack':
                                    damagelist_revenant = range(30, 60)
                                    damage = random.choice(damagelist_revenant)
                                    multiplier = float(player_stats.player_STR * 0.01) + 1
                                    damagelist_player = range(5, 40)
                                    player_damage = random.choice(damagelist_player) * multiplier
                                    print(f'both you and the revenant attacked each other\n'
                                          f'you did {player_damage} points of damage\n'
                                          f'revenant has {enemy_HP - player_damage} left\n'
                                          f'revenant did {damage} points of damage\n'
                                          f'you have {player_stats.player_HP - damage} left')
                                    enemy_HP -=player_damage
                                    player_stats.player_HP -= damage
                                if player_action == 'magic':
                                    damagelist_revenant = range(30, 60)
                                    damage = random.choice(damagelist_revenant)
                                    multiplier = float(player_stats.player_INT * 0.01) + 1
                                    damagelist_player = range(5, 40)
                                    player_damage = random.choice(damagelist_player) * multiplier
                                    print(f'you cast a spell and the revenant attacked. both you and the revenant got hit\n'
                                          f'you did {player_damage} points of damage\n'
                                          f'revenant has {enemy_HP - player_damage} left\n'
                                          f'revenant did {damage} points of damage\n'
                                          f'you have {player_stats.player_HP - damage} left')
                                    player_stats.player_HP -=damage
                                    enemy_HP -= player_damage
                                if player_action == 'dodge':
                                    damagelist_revenant = range(30, 60)
                                    damage = random.choice(damagelist_revenant)
                                    print(f'you dodged, but you dodge right in to the revenant attack\n'
                                          f'revenant did {damage} points of damage\n'
                                          f'you have {player_HP - damage} left')
                                    player_HP -= damage
                                if player_action == 'block':
                                    if player_stats.player_STR > player_stats.player_INT:
                                        multiplier = float(player_stats.player_STR * 0.01) + 1
                                        damagelist_player = range(5, 40)
                                        player_damage = random.choice(damagelist_player) * multiplier
                                        print(f'you blocked the revenant attack and countered it with a attack of youre own\n'
                                              f'you did {player_damage} points of damage\n'
                                              f'revenant has {enemy_HP - player_damage} left\n')
                                        enemy_HP -= player_damage
                                    elif player_stats.player_STR < player_stats.player_INT:
                                        multiplier = float(player_stats.player_INT * 0.01) + 1
                                        damagelist_player = range(5, 40)
                                        player_damage = random.choice(damagelist_player) * multiplier
                                        print(f'you blocked the revenant attack and countered it with a magic spell\n'
                                              f'you did {player_damage} points of damage\n'
                                              f'revenant has {enemy_HP - player_damage} left\n')
                                        enemy_HP -= player_damage
                        if player_stats.PPA_block >= 2:
                            AI_action = 'magic'
                            if AI_action == 'magic':
                                if player_action == 'attack':
                                    damagelist_revenant = range(30, 60)
                                    damage = random.choice(damagelist_revenant)
                                    multiplier = float(player_stats.player_STR * 0.01) + 1
                                    damagelist_player = range(5, 40)
                                    player_damage = random.choice(damagelist_player) * multiplier
                                    print(f'you attacked while the revenant used magic. both got hit.\n'
                                          f'you did {player_damage} points of damage\n'
                                          f'revenant has {enemy_HP - player_damage} left\n'
                                          f'revenant did {damage} points of damage\n'
                                          f'you have {player_stats.player_HP - damage} left')
                                    player_stats.player_HP -= enemy_HP
                                    enemy_HP -= player_damage
                                if player_action == 'block':
                                    damagelist_revenant = range(30, 60)
                                    damage = random.choice(damagelist_revenant)
                                    print(f'you tried to block, but the revenant overwhelmed you with magic.\n'
                                          f'revenant did {damage} points of damage.\n'
                                          f'you have {player_stats.player_HP - damage} left')
                                    player_stats.player_HP -= damage
                                if player_action == 'dodge':
                                    multiplier = float(player_stats.player_STR * 0.01) + 1
                                    damagelist_player = range(5, 40)
                                    player_damage = random.choice(damagelist_player) * multiplier
                                    print(f'you dodged the revenant spell and countered it with a attack of youre own\n'
                                          f'you did {player_damage} points of damage\n'
                                          f'revenant has {enemy_HP - player_damage} left\n')
                                    enemy_HP -= player_damage
                                if player_action == 'magic':
                                    damagelist_revenant = range(30, 60)
                                    damage = random.choice(damagelist_revenant)
                                    multiplier = float(player_stats.player_INT * 0.01) + 1
                                    damagelist_player = range(5, 40)
                                    player_damage = random.choice(damagelist_player) * multiplier
                                    print(f'both you and the revenant cast spells and hit each other\n'
                                          f'you did {player_damage} points of damage\n'
                                          f'revenant has {enemy_HP - player_damage} left\n'
                                          f'revenant did {damage} points of damage\n'
                                          f'you have {player_stats.player_HP - damage} left')
                                    enemy_HP -= player_damage
                                    player_stats.player_HP -= damage
                        if player_stats.PPA_magic >= 2:
                            AI_action = 'dodge'
                            if AI_action == 'dodge':
                                if player_action == 'attack':
                                    multiplier = float(player_stats.player_STR * 0.01) + 1
                                    damagelist_player = range(5, 40)
                                    player_damage = random.choice(damagelist_player) * multiplier
                                    print(f'the revenant dodged right into youre attack.\n'
                                          f'you did {player_damage} points of damage\n'
                                          f'revenant has {enemy_HP - player_damage} left\n')
                                    enemy_HP -= player_damage
                                if player_action == 'dodge':
                                    print('both you and the enemy dodged')
                                if player_action == 'block':
                                    print('you blocked, but the revenant dodged and so 0 points of damage to both.')
                                if player_action == 'magic':
                                    damagelist_revenant = range(30, 60)
                                    damage = random.choice(damagelist_revenant)
                                    print(f'the revenant dodged your spell and countered.\n'
                                          f'revenant did {damage} points of damage.\n'
                                          f' you have {player_HP - damage} left')
                                    player_stats.player_HP -= damage
                    if enemy_HP <= 0:
                        player_stats.PPA.clear()
                        print(EXP(player_stats.player_STR, player_stats.player_INT, player_stats.player_DEX, player_HP, player_FP,enemy))
                    if player_stats.player_HP <= 0:
                        print('you died')
            finally:
                tpa.close()



