import player_stats
import random

def AWESOME():
    APS = False
    player_stats.enemy_HP = 200
    with open('stats.txt', 'a') as tpa:
        try:
            while player_stats.enemy_HP > 0 and player_stats.player_HP > 0:
                player_stats.user_action = input('What will you do? attack, block, dodge, or magic? ')
                if (
                    player_stats.user_action == 'attack'
                    or player_stats.user_action == 'dodge'
                    or player_stats.user_action == 'block'
                    or player_stats.user_action == 'magic'
                ):
                    player_stats.PPA.append(player_stats.user_action)
                    tpa.write(player_stats.user_action + "\n")
                    player_stats.history_current.append(player_stats.user_action)
                else:
                    print('That is not a valid action.')
                    player_stats.user_action = input('What will you do? attack, block, dodge, or magic? ')
                    player_stats.PPA.append(player_stats.user_action)
                    tpa.write(player_stats.user_action + "\n")
                    player_stats.history_current.append(player_stats.user_action)
                if len(player_stats.PPA) > 3:
                    player_stats.PPA.remove(player_stats.PPA[0])
                if len(player_stats.history_current) > 1:
                    player_stats.history_current.remove(player_stats.history_current[0])
                if player_stats.history_previous == player_stats.history_current:
                    APS = True
                if player_stats.history_previous != player_stats.history_current:
                    APS = False
                print(player_stats.history_previous, player_stats.history_current)
                player_stats.history_previous = [player_stats.user_action]
                if APS:
                    print(1)
                elif not APS:
                    if player_stats.Player_Class == 'warrior':
                        if player_stats.enemy_HP == 200:
                            player_stats.AI_action = 'block'
                    elif player_stats.Player_Class == 'mage':
                        if player_stats.enemy_HP == 200:
                            player_stats.AI_action = 'dodge'
                    else:
                        if len(player_stats.history_previous) == 0:
                            actionlist = ['attack', 'block', 'magic', 'dodge']
                            player_stats.AI_action = random.choice(actionlist)
                    if player_stats.AI_action == 'block':
                        if player_stats.user_action == 'attack':
                            damagelist_golem = range(40, 50)
                            damage = random.choice(damagelist_golem)
                            print(f'The golem blocked your attack and countered.\n'
                                  f'The golem did {damage} points of damage.\n'
                                  f'You have {player_stats.player_HP - damage} left')
                            player_stats.player_HP -= damage
                        if player_stats.user_action == 'magic':
                            multiplier = float(player_stats.player_INT * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(
                                f'The golem tried to block your attack, but the magic was too strong and hit the enemy.\n'
                                f'You did {player_damage} points of damage.\n'
                                f'The golem has {player_stats.enemy_HP - player_damage} left')
                            player_stats.enemy_HP -= player_damage
                        if player_stats.user_action == 'dodge':
                            print('You dodged, but the golem blocked, resulting in 0 points of damage to both.')
                        if player_stats.user_action == 'block':
                            print('Both you and the golem blocked')
                    if player_stats.AI_action == 'attack':
                        if player_stats.user_action == 'attack':
                            damagelist_golem = range(40, 50)
                            damage = random.choice(damagelist_golem)
                            multiplier = float(player_stats.player_STR * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'Both you and the golem attacked each other.\n'
                                  f'You did {player_damage} points of damage.\n'
                                  f'The golem has {player_stats.enemy_HP - player_damage} left.\n'
                                  f'The golem did {damage} points of damage.\n'
                                  f'You have {player_stats.player_HP - damage} left')
                            player_stats.enemy_HP -= player_damage
                            player_stats.player_HP -= damage
                        if player_stats.user_action == 'magic':
                            damagelist_golem = range(40, 50)
                            damage = random.choice(damagelist_golem)
                            multiplier = float(player_stats.player_INT * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'You cast a spell, and the golem attacked. Both you and the golem got hit.\n'
                                  f'You did {player_damage} points of damage.\n'
                                  f'The golem has {player_stats.enemy_HP - player_damage} left.\n'
                                  f'The golem did {damage} points of damage.\n'
                                  f'You have {player_stats.player_HP - damage} left')
                            player_stats.player_HP -= damage
                            player_stats.enemy_HP -= player_damage
                        if player_stats.user_action == 'dodge':
                            damagelist_golem = range(40, 50)
                            damage = random.choice(damagelist_golem)
                            print(f'You dodged, but you dodged right into the golem\'s attack.\n'
                                  f'The golem did {damage} points of damage.\n'
                                  f'You have {player_stats.player_HP - damage} left')
                            player_stats.player_HP -= damage
                        if player_stats.user_action == 'block':
                            if player_stats.player_STR > player_stats.player_INT:
                                multiplier = float(player_stats.player_STR * 0.01) + 1
                                damagelist_player = range(5, 40)
                                player_damage = random.choice(damagelist_player) * multiplier
                                print(f'You blocked the golem\'s attack and countered it with an attack of your own.\n'
                                      f'You did {player_damage} points of damage.\n'
                                      f'The golem has {player_stats.enemy_HP - player_damage} left.')
                                player_stats.enemy_HP -= player_damage
                            elif player_stats.player_STR < player_stats.player_INT:
                                multiplier = float(player_stats.player_INT * 0.01) + 1
                                damagelist_player = range(5, 40)
                                player_damage = random.choice(damagelist_player) * multiplier
                                print(f'You blocked the golem\'s attack and countered it with a magic spell.\n'
                                      f'You did {player_damage} points of damage.\n'
                                      f'The golem has {player_stats.enemy_HP - player_damage} left.')
                                player_stats.enemy_HP -= player_damage
                    if player_stats.AI_action == 'magic':
                        if player_stats.user_action == 'attack':
                            damagelist_golem = range(40, 50)
                            damage = random.choice(damagelist_golem)
                            multiplier = float(player_stats.player_STR * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'You attacked while the golem used magic. Both got hit.\n'
                                  f'You did {player_damage} points of damage.\n'
                                  f'The golem has {player_stats.enemy_HP - player_damage} left.\n'
                                  f'The golem did {damage} points of damage.\n'
                                  f'You have {player_stats.player_HP - damage} left')
                            player_stats.player_HP -= player_stats.enemy_HP
                            player_stats.enemy_HP -= player_damage
                        if player_stats.user_action == 'block':
                            damagelist_golem = range(40, 50)
                            damage = random.choice(damagelist_golem)
                            print(f'You tried to block, but the golem overwhelmed you with magic.\n'
                                  f'The golem did {damage} points of damage.\n'
                                  f'You have {player_stats.player_HP - damage} left')
                            player_stats.player_HP -= damage
                        if player_stats.user_action == 'dodge':
                            multiplier = float(player_stats.player_STR * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'You dodged the golem\'s spell and countered it with an attack of your own.\n'
                                  f'You did {player_damage} points of damage.\n'
                                  f'The golem has {player_stats.enemy_HP - player_damage} left.')
                            player_stats.enemy_HP -= player_damage
                        if player_stats.user_action == 'magic':
                            damagelist_golem = range(40, 50)
                            damage = random.choice(damagelist_golem)
                            multiplier = float(player_stats.player_INT * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'Both you and the golem cast spells and hit each other.\n'
                                  f'You did {player_damage} points of damage.\n'
                                  f'The golem has {player_stats.enemy_HP - player_damage} left.\n'
                                  f'The golem did {damage} points of damage.\n'
                                  f'You have {player_stats.player_HP - damage} left')
                            player_stats.enemy_HP -= player_damage
                            player_stats.player_HP -= damage
                    if player_stats.AI_action == 'dodge':
                        if player_stats.user_action == 'attack':
                            multiplier = float(player_stats.player_STR * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'The golem dodged right into your attack.\n'
                                  f'You did {player_damage} points of damage.\n'
                                  f'The golem has {player_stats.enemy_HP - player_damage} left.')
                            player_stats.enemy_HP -= player_damage
                        if player_stats.user_action == 'dodge':
                            print('Both you and the enemy dodged')
                        if player_stats.user_action == 'block':
                            print('You blocked, but the golem dodged, resulting in 0 points of damage to both')
                        if player_stats.user_action == 'magic':
                            multiplier = float(player_stats.player_INT * 0.01) + 1
                            damagelist_player = range(5, 40)
                            player_damage = random.choice(damagelist_player) * multiplier
                            print(f'The golem tried to dodge your spell but failed.\n'
                                  f'You did {player_damage} points of damage.\n'
                                  f'The golem has {player_stats.enemy_HP - player_damage} left.')
                            player_stats.enemy_HP -= player_damage
                if player_stats.enemy_HP <= 0:
                    print('You won!')
                elif player_stats.player_HP <= 0:
                    print('You lost...')
        except ValueError:
            print("Invalid input! Please enter a valid action.")

AWESOME()