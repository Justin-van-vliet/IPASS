import random
import player_stats

def responds_golem(player_stats):
    if player_stats.AI_action == 'block':
        if player_stats.player_action == 'attack':
            damagelist_golem = range(40, 50)
            damage = random.choice(damagelist_golem)
            print(f'the golem block your attack and counterattacked.\n'
                  f'the golem did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'magic':
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(
                f'the golem tried to block your attack, but the magic was to strong and hitted the enemy\n'
                f'you did {player_damage} points of damage.\n'
                f'the golem has {player_stats.enemy_HP - player_damage} left')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('you dodged, but the golem blocked and so 0 points of damage to both.')
        if player_stats.player_action == 'block':
            print('both you and the golem blocked')
    if player_stats.AI_action == 'attack':
        if player_stats.player_action == 'attack':
            damagelist_golem = range(40, 50)
            damage = random.choice(damagelist_golem)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the golem attacked each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'the golem has {player_stats.enemy_HP - player_damage} left\n'
                  f'the golem did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_golem = range(40, 50)
            damage = random.choice(damagelist_golem)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you cast a spell and the golem attacked. both you and the golem got hit\n'
                  f'you did {player_damage} points of damage\n'
                  f'the golem has {player_stats.enemy_HP - player_damage} left\n'
                  f'the golem did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            damagelist_golem = range(40, 50)
            damage = random.choice(damagelist_golem)
            print(f'you dodged, but you dodge right in to the golem attack\n'
                  f'the golem did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'block':
            if player_stats.player_STR > player_stats.player_INT:
                multiplier = float(player_stats.player_STR * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the golem attack and countered it with a attack of youre own\n'
                      f'you did {player_damage} points of damage\n'
                      f'the golem has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
            elif player_stats.player_STR < player_stats.player_INT:
                multiplier = float(player_stats.player_INT * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the golem attack and countered it with a magic spell\n'
                      f'you did {player_damage} points of damage\n'
                      f'the golem has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
    if player_stats.AI_action == 'magic':
        if player_stats.player_action == 'attack':
            damagelist_golem = range(40, 50)
            damage = random.choice(damagelist_golem)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you attacked while the golem used magic. both got hit.\n'
                  f'you did {player_damage} points of damage\n'
                  f'the golem has {player_stats.enemy_HP - player_damage} left\n'
                  f'the golem did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'block':
            damagelist_golem = range(40, 50)
            damage = random.choice(damagelist_golem)
            print(f'you tried to block, but the golem overwhelmed you with magic.\n'
                  f'the golem did {damage} points of damage.\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'dodge':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you dodged the golems spell and countered it with a attack of youre own\n'
                  f'you did {player_damage} points of damage\n'
                  f'the golem has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_golem = range(40, 50)
            damage = random.choice(damagelist_golem)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the golem cast spells and hit each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'the golem has {player_stats.enemy_HP - player_damage} left\n'
                  f'the golem did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.enemy_HP -= player_damage
            player_stats.player_HP -= damage
    if player_stats.AI_action == 'dodge':
        if player_stats.player_action == 'attack':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'the golem dodged right into youre attack.\n'
                  f'you did {player_damage} points of damage\n'
                  f'the golem has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('both you and the golem dodged')
        if player_stats.player_action == 'block':
            print('you blocked, but the golem dodged and so 0 points of damage to both.')
        if player_stats.player_action == 'magic':
            damagelist_golem = range(40, 50)
            damage = random.choice(damagelist_golem)
            print(f'the golem dodged youre spell and performed a counter attack.\n'
                  f'the golem did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left\n')
            player_stats.player_HP -= damage

def responds_fenrir(player_stats):
    if player_stats.AI_action == 'block':
        if player_stats.player_action == 'attack':
            damagelist_fenrir = range(50, 70)
            damage = random.choice(damagelist_fenrir)
            print(f'fenrir block your attack and counterattacked.\n'
                  f'fenrir did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'magic':
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(
                f'fenrir tried to block your attack, but the magic was to strong and hitted the enemy\n'
                f'you did {player_damage} points of damage.\n'
                f'fenrir has {player_stats.enemy_HP - player_damage} left')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('you dodged, but fenrir blocked and so 0 points of damage to both.')
        if player_stats.player_action == 'block':
            print('both you and fenrir blocked')
    if player_stats.AI_action == 'attack':
        if player_stats.player_action == 'attack':
            damagelist_fenrir = range(50, 70)
            damage = random.choice(damagelist_fenrir)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and fenrir attacked each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'fenrir has {player_stats.enemy_HP - player_damage} left\n'
                  f'fenrir did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_fenrir = range(50, 70)
            damage = random.choice(damagelist_fenrir)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you cast a spell and fenrir attacked. both you and fenrir got hit\n'
                  f'you did {player_damage} points of damage\n'
                  f'fenrir has {player_stats.enemy_HP - player_damage} left\n'
                  f'fenrir did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            damagelist_fenrir = range(50, 70)
            damage = random.choice(damagelist_fenrir)
            print(f'you dodged, but you dodge right in to fenrir attack\n'
                  f'fenrir did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'block':
            if player_stats.player_STR > player_stats.player_INT:
                multiplier = float(player_stats.player_STR * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked fenrir attack and countered it with a attack of youre own\n'
                      f'you did {player_damage} points of damage\n'
                      f'fenrir has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
            elif player_stats.player_STR < player_stats.player_INT:
                multiplier = float(player_stats.player_INT * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked fenrir attack and countered it with a magic spell\n'
                      f'you did {player_damage} points of damage\n'
                      f'fenrir has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
    if player_stats.AI_action == 'magic':
        if player_stats.player_action == 'attack':
            damagelist_fenrir = range(50, 70)
            damage = random.choice(damagelist_fenrir)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you attacked while fenrir used magic. both got hit.\n'
                  f'you did {player_damage} points of damage\n'
                  f'fenrir has {player_stats.enemy_HP - player_damage} left\n'
                  f'fenrir did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'block':
            damagelist_fenrir = range(50, 70)
            damage = random.choice(damagelist_fenrir)
            print(f'you tried to block, but fenrir overwhelmed you with magic.\n'
                  f'fenrir did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'dodge':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you dodged fenrirs spell and countered it with a attack of youre own\n'
                  f'you did {player_damage} points of damage\n'
                  f'fenrir has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_fenrir = range(50, 70)
            damage = random.choice(damagelist_fenrir)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and fenrir cast spells and hit each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'fenrir has {player_stats.enemy_HP - player_damage} left\n'
                  f'fenrir did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.enemy_HP -= player_damage
            player_stats.player_HP -= damage
    if player_stats.AI_action == 'dodge':
        if player_stats.player_action == 'attack':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'fenrir dodged right into youre attack.\n'
                  f'you did {player_damage} points of damage\n'
                  f'fenrir has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('both you and fenrir dodged')
        if player_stats.player_action == 'block':
            print('you blocked, but fenrir dodged and so 0 points of damage to both.')
        if player_stats.player_action == 'magic':
            damagelist_fenrir = range(50, 70)
            damage = random.choice(damagelist_fenrir)
            print(f'fenrir dodged youre spell and performed a counter attack.\n'
                  f'fenrir did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left\n')
            player_stats.player_HP -= damage

def responds_hydra():
    if player_stats.AI_action == 'block':
        if player_stats.player_action == 'attack':
            damagelist_hydra = range(50, 60)
            damage = random.choice(damagelist_hydra)
            print(f'the hydra block your attack and counterattacked.\n'
                  f'the hydra did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'magic':
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(
                f'the hydra tried to block your attack, but the magic was to strong and hitted the enemy\n'
                f'you did {player_damage} points of damage.\n'
                f'the hydra has {player_stats.enemy_HP - player_damage} left')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('you dodged, but the hydra blocked and so 0 points of damage to both.')
        if player_stats.player_action == 'block':
            print('both you and the hydra blocked')
    if player_stats.AI_action == 'attack':
        if player_stats.player_action == 'attack':
            damagelist_hydra = range(50, 60)
            damage = random.choice(damagelist_hydra)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the hydra attacked each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'the hydra has {player_stats.enemy_HP - player_damage} left\n'
                  f'the hydra did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'magic':
            damagelist_hydra = range(50, 60)
            damage = random.choice(damagelist_hydra)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you cast a spell and the hydra attacked. both you and the hydra got hit\n'
                  f'you did {player_damage} points of damage\n'
                  f'the hydra has {player_stats.enemy_HP - player_damage} left\n'
                  f'the hydra did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.enemy_HP -= player_damage
            player_stats.player_HP -= damage
        if player_stats.player_action == 'dodge':
            damagelist_hydra = range(50, 60)
            damage = random.choice(damagelist_hydra)
            print(f'you dodged, but you dodge right in to the hydra attack\n'
                  f'the hydra did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'block':
            if player_stats.player_STR > player_stats.player_INT:
                multiplier = float(player_stats.player_STR * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the hydra attack and countered it with a attack of youre own\n'
                      f'you did {player_damage} points of damage\n'
                      f'the hydra has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
            elif player_stats.player_STR < player_stats.player_INT:
                multiplier = float(player_stats.player_INT * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the golem attack and countered it with a magic spell\n'
                      f'you did {player_damage} points of damage\n'
                      f'the golem has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
    if player_stats.AI_action == 'magic':
        if player_stats.player_action == 'attack':
            damagelist_hydra = range(50, 60)
            damage = random.choice(damagelist_hydra)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you attacked while the hydra used magic. both got hit.\n'
                  f'you did {player_damage} points of damage\n'
                  f'the hydra has {player_stats.enemy_HP - player_damage} left\n'
                  f'the hydra did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'block':
            damagelist_hydra = range(50, 60)
            damage = random.choice(damagelist_hydra)
            print(f'you tried to block, but the hydra overwhelmed you with magic.\n'
                  f'the hydra did {damage} points of damage.\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'dodge':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you dodged the hydra spell and countered it with a attack of youre own\n'
                  f'you did {player_damage} points of damage\n'
                  f'the hydra has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_hydra = range(50, 60)
            damage = random.choice(damagelist_hydra)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the hydra cast spells and hit each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'the hydra has {player_stats.enemy_HP - player_damage} left\n'
                  f'the hydra did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.enemy_HP -= player_damage
            player_stats.player_HP -= damage
    if player_stats.AI_action == 'dodge':
        if player_stats.player_action == 'attack':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'the hydra dodged right into youre attack.\n'
                  f'you did {player_damage} points of damage\n'
                  f'the hydra has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('both you and the golem dodged')
        if player_stats.player_action == 'block':
            print('you blocked, but the hydra dodged and so 0 points of damage to both.')
        if player_stats.player_action == 'magic':
            damagelist_hydra = range(50, 60)
            damage = random.choice(damagelist_hydra)
            print(f'the hydra dodged youre spell and performed a counter attack.\n'
                  f'the hydra did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left\n')
            player_stats.player_HP -= damage

def responds_revenant():
    if player_stats.AI_action == 'block':
        if player_stats.player_action == 'attack':
            damagelist_revenant = range(30, 60)
            damage = random.choice(damagelist_revenant)
            print(f'the revenant block your attack and counterattacked.\n'
                  f'revenant did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'magic':
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(
                f'the revenant tried to block your attack, but the magic was to strong and hitted the enemy\n'
                f'you did {player_damage} points of damage.\n'
                f'revenant has {player_stats.enemy_HP - player_damage} left')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('you dodged, but the revenant blocked and so 0 points of damage to both.')
        if player_stats.player_action == 'block':
            print('both you and the revenant blocked')
    if player_stats.AI_action == 'attack':
        if player_stats.player_action == 'attack':
            damagelist_revenant = range(30, 60)
            damage = random.choice(damagelist_revenant)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the revenant attacked each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'revenant has {player_stats.enemy_HP - player_damage} left\n'
                  f'revenant did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_revenant = range(30, 60)
            damage = random.choice(damagelist_revenant)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you cast a spell and the revenant attacked. both you and the revenant got hit\n'
                  f'you did {player_damage} points of damage\n'
                  f'revenant has {player_stats.enemy_HP - player_damage} left\n'
                  f'revenant did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'dodge':
            damagelist_revenant = range(30, 60)
            damage = random.choice(damagelist_revenant)
            print(f'you dodged, but you dodge right in to the revenants attack\n'
                  f'revenant did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'block':
            if player_stats.player_STR > player_stats.player_INT:
                multiplier = float(player_stats.player_STR * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the revenants attack and countered it with a attack of youre own\n'
                      f'you did {player_damage} points of damage\n'
                      f'revenant has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
            elif player_stats.player_STR < player_stats.player_INT:
                multiplier = float(player_stats.player_INT * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the revenants attack and countered it with a magic spell\n'
                      f'you did {player_damage} points of damage\n'
                      f'revenant has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
    if player_stats.AI_action == 'magic':
        if player_stats.player_action == 'attack':
            damagelist_revenant = range(30, 60)
            damage = random.choice(damagelist_revenant)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you attacked while the revenant used magic. both got hit.\n'
                  f'you did {player_damage} points of damage\n'
                  f'revenant has {player_stats.enemy_HP - player_damage} left\n'
                  f'revenant did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'block':
            damagelist_revenant = range(30, 60)
            damage = random.choice(damagelist_revenant)
            print(f'you tried to block, but the revenant overwhelmed you with magic.\n'
                  f'revenant did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'dodge':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you dodged the revenants spell and countered it with a attack of youre own\n'
                  f'you did {player_damage} points of damage\n'
                  f'revenant has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_revenant = range(30, 60)
            damage = random.choice(damagelist_revenant)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the revenant cast spells and hit each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'revenant has {player_stats.enemy_HP - player_damage} left\n'
                  f'revenant did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.enemy_HP -= player_damage
            player_stats.player_HP -= damage
    if player_stats.AI_action == 'dodge':
        if player_stats.player_action == 'attack':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'the revenant dodged right into youre attack.\n'
                  f'you did {player_damage} points of damage\n'
                  f'revenant has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('both you and the revenant dodged')
        if player_stats.player_action == 'block':
            print('you blocked, but the revenant dodged and so 0 points of damage to both.')
        if player_stats.player_action == 'magic':
            damagelist_revenant = range(30, 60)
            damage = random.choice(damagelist_revenant)
            print(f'the revenant dodged your spell and countered.\n'
                  f'revenant did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage

def responds_slime():
    if player_stats.AI_action == 'block':
        if player_stats.player_action == 'attack':
            damagelist_slime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            damage = random.choice(damagelist_slime)
            print(f'slime block your attack and counterattacked.\n'
                  f'slime did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'magic':
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(
                f'the slime tried to block your attack, but the magic was to strong and hitted the enemy\n'
                f'you did {player_damage} points of damage.\n'
                f'slime has {player_stats.enemy_HP - player_damage} left')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('you dodged, but the slime blocked and so 0 points of damage to both.')
        if player_stats.player_action == 'block':
            print('both you and the slime blocked')
    if player_stats.AI_action == 'attack':
        if player_stats.player_action == 'attack':
            damagelist_slime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            damage = random.choice(damagelist_slime)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the slime attacked each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'slime has {player_stats.enemy_HP - player_damage} left\n'
                  f'slime did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.enemy_HP -= player_damage
            player_stats.player_HP -= damage
        if player_stats.player_action == 'magic':
            damagelist_slime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            damage = random.choice(damagelist_slime)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you cast a spell and the slime attacked. both you and the slime got hit\n'
                  f'you did {player_damage} points of damage\n'
                  f'slime has {player_stats.enemy_HP - player_damage} left\n'
                  f'slime did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            damagelist_slime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            damage = random.choice(damagelist_slime)
            print(f'you dodged, but you dodge right in to the slimes attack\n'
                  f'slime did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'block':
            if player_stats.player_STR > player_stats.player_INT:
                multiplier = float(player_stats.player_STR * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the slimes attack and countered it with a attack of youre own\n'
                      f'you did {player_damage} points of damage\n'
                      f'slime has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
            elif player_stats.player_STR < player_stats.player_INT:
                multiplier = float(player_stats.player_INT * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the slimes attack and countered it with a magic spell\n'
                      f'you did {player_damage} points of damage\n'
                      f'slime has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
    if player_stats.AI_action == 'magic':
        if player_stats.player_action == 'attack':
            damagelist_slime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            damage = random.choice(damagelist_slime)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you attacked while the slime used magic. both got hit.\n'
                  f'you did {player_damage} points of damage\n'
                  f'slime has {player_stats.enemy_HP - player_damage} left\n'
                  f'slime did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'block':
            damagelist_slime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            damage = random.choice(damagelist_slime)
            print(f'you tried to block, but the slime overwhelmed you with magic.\n'
                  f'slime did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'dodge':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you dodged the slimes spell and countered it with a attack of youre own\n'
                  f'you did {player_damage} points of damage\n'
                  f'slime has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_slime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            damage = random.choice(damagelist_slime)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the slime cast spells and hit each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'slime has {player_stats.enemy_HP - player_damage} left\n'
                  f'slime did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.enemy_HP -= player_damage
            player_stats.player_HP -= damage
    if player_stats.AI_action == 'dodge':
        if player_stats.player_action == 'attack':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'the slime dodged right into youre attack.\n'
                  f'you did {player_damage} points of damage\n'
                  f'slime has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('both you and the enemy dodged')
        if player_stats.player_action == 'block':
            print('you blocked, but the slime dodged and so 0 points of damage to both.')
        if player_stats.player_action == 'magic':
            damagelist_slime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            damage = random.choice(damagelist_slime)
            print(f'slime dodged your spell and countered.\n'
                  f'slime did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage

def responds_lizardman():
    if player_stats.AI_action == 'block':
        if player_stats.player_action == 'attack':
            damagelist_lizardman = range(10, 35)
            damage = random.choice(damagelist_lizardman)
            print(f'the lizardman block your attack and counterattacked.\n'
                  f'lizardman did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'magic':
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(
                f'the lizardman tried to block your attack, but the magic was to strong and hitted the enemy\n'
                f'you did {player_damage} points of damage.\n'
                f'lizardman has {player_stats.enemy_HP - player_damage} left')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('you dodged, but the lizardman blocked and so 0 points of damage to both.')
        if player_stats.player_action == 'block':
            print('both you and the lizardman blocked')
    if player_stats.AI_action == 'attack':
        if player_stats.player_action == 'attack':
            damagelist_lizardman = range(10, 35)
            damage = random.choice(damagelist_lizardman)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the lizardman attacked each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'lizardman has {player_stats.enemy_HP - player_damage} left\n'
                  f'lizardman did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'magic':
            damagelist_lizardman = range(10, 35)
            damage = random.choice(damagelist_lizardman)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you cast a spell and the lizardman attacked. both you and the lizardman got hit\n'
                  f'you did {player_damage} points of damage\n'
                  f'lizardman has {player_stats.enemy_HP - player_damage} left\n'
                  f'lizardman did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            damagelist_lizardman = range(10, 35)
            damage = random.choice(damagelist_lizardman)
            print(f'you dodged, but you dodge right in to the lizardman attack\n'
                  f'lizardman did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'block':
            if player_stats.player_STR > player_stats.player_INT:
                multiplier = float(player_stats.player_STR * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the lizardman attack and countered it with a attack of youre own\n'
                      f'you did {player_damage} points of damage\n'
                      f'lizardman has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
            elif player_stats.player_STR < player_stats.player_INT:
                multiplier = float(player_stats.player_INT * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the lizardman attack and countered it with a magic spell\n'
                      f'you did {player_damage} points of damage\n'
                      f'lizardman has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
    if player_stats.AI_action == 'magic':
        if player_stats.player_action == 'attack':
            damagelist_lizardman = range(10, 35)
            damage = random.choice(damagelist_lizardman)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you attacked while the lizardman used magic. both got hit.\n'
                  f'you did {player_damage} points of damage\n'
                  f'lizardman has {player_stats.enemy_HP - player_damage} left\n'
                  f'lizardman did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'block':
            damagelist_lizardman = range(10, 35)
            damage = random.choice(damagelist_lizardman)
            print(f'you tried to block, but the lizardman overwhelmed you with magic.\n'
                  f'lizardman did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'dodge':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you dodged the lizardman spell and countered it with a attack of youre own\n'
                  f'you did {player_damage} points of damage\n'
                  f'lizardman has player_stats.{player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_lizardman = range(10, 35)
            damage = random.choice(damagelist_lizardman)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the lizardman cast spells and hit each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'lizardman has {player_stats.enemy_HP - player_damage} left\n'
                  f'lizardman did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.enemy_HP -= player_damage
            player_stats.player_HP -= damage
    if player_stats.AI_action == 'dodge':
        if player_stats.player_action == 'attack':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'the lizardman dodged right into youre attack.\n'
                  f'you did {player_damage} points of damage\n'
                  f'lizardman has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('both you and the enemy dodged')
        if player_stats.player_action == 'block':
            print('you blocked, but the slime dodged and so 0 points of damage to both.')
        if player_stats.player_action == 'magic':
            damagelist_lizardman = range(10, 35)
            damage = random.choice(damagelist_lizardman)
            print(f'lizardman dodged your spell and countered.\n'
                  f'lizardman did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage

def responds_mothman():
    if player_stats.AI_action == 'block':
        if player_stats.player_action == 'attack':
            damagelist_mothman = range(20, 30)
            damage = random.choice(damagelist_mothman)
            print(f'the mothman block your attack and counterattacked.\n'
                  f'mothman did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'magic':
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(
                f'the mothman tried to block your attack, but the magic was to strong and hitted the enemy\n'
                f'you did {player_damage} points of damage.\n'
                f'mothman has {player_stats.enemy_HP - player_damage} left')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('you dodged, but the mothman blocked and so 0 points of damage to both.')
        if player_stats.player_action == 'block':
            print('both you and the mothman blocked')
    if player_stats.AI_action == 'attack':
        if player_stats.player_action == 'attack':
            damagelist_mothman = range(20, 30)
            damage = random.choice(damagelist_mothman)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the mothman attacked each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'mothman has {player_stats.enemy_HP - player_damage} left\n'
                  f'mothman did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.enemy_HP -= player_damage
            player_stats.player_HP -= damage
        if player_stats.player_action == 'magic':
            damagelist_mothman = range(20, 30)
            damage = random.choice(damagelist_mothman)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you cast a spell and the mothman attacked. both you and the mothman got hit\n'
                  f'you did {player_damage} points of damage\n'
                  f'mothman has {player_stats.enemy_HP - player_damage} left\n'
                  f'mothman did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.enemy_HP -= player_damage
            player_stats.player_HP -= damage
        if player_stats.player_action == 'dodge':
            damagelist_mothman = range(20, 30)
            damage = random.choice(damagelist_mothman)
            print(f'you dodged, but you dodge right in to the mothman attack\n'
                  f'mothman did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'block':
            if player_stats.player_STR > player_stats.player_INT:
                multiplier = float(player_stats.player_STR * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the mothman attack and countered it with a attack of youre own\n'
                      f'you did {player_damage} points of damage\n'
                      f'mothman has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
            elif player_stats.player_STR < player_stats.player_INT:
                multiplier = float(player_stats.player_INT * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the mothman attack and countered it with a magic spell\n'
                      f'you did {player_damage} points of damage\n'
                      f'mothman has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
    if player_stats.AI_action == 'magic':
        if player_stats.player_action == 'attack':
            damagelist_mothman = range(20, 30)
            damage = random.choice(damagelist_mothman)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you attacked while the mothman used magic. both got hit.\n'
                  f'you did {player_damage} points of damage\n'
                  f'mothman has {player_stats.enemy_HP - player_damage} left\n'
                  f'mothman did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'block':
            damagelist_mothman = range(20, 30)
            damage = random.choice(damagelist_mothman)
            print(f'you tried to block, but the mothman overwhelmed you with magic.\n'
                  f'mothman did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'dodge':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you dodged the mothman spell and countered it with a attack of youre own\n'
                  f'you did {player_damage} points of damage\n'
                  f'mothman has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_mothman = range(20, 30)
            damage = random.choice(damagelist_mothman)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the mothman cast spells and hit each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'mothman has {player_stats.enemy_HP - player_damage} left\n'
                  f'mothman did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.enemy_HP -= player_damage
            player_stats.player_HP -= damage
    if player_stats.AI_action == 'dodge':
        if player_stats.player_action == 'attack':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'the mothman dodged right into youre attack.\n'
                  f'you did {player_damage} points of damage\n'
                  f'mothman has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('both you and the mothman dodged')
        if player_stats.player_action == 'block':
            print('you blocked, but the mothman dodged and so 0 points of damage to both.')
        if player_stats.player_action == 'magic':
            damagelist_mothman = range(20, 30)
            damage = random.choice(damagelist_mothman)
            print(f'the mothman dodged youre spell and performed a counter attack.\n'
                  f'the mothman did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left\n')
            player_stats.player_HP -= damage

def responds_bandit():
    if player_stats.AI_action == 'block':
        if player_stats.player_action == 'attack':
            damagelist_bandit = range(5, 25)
            damage = random.choice(damagelist_bandit)
            print(f'the bandit block your attack and counterattacked.\n'
                  f'bandit did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'magic':
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(
                f'the bandit tried to block your attack, but the magic was to strong and hitted the enemy\n'
                f'you did {player_damage} points of damage.\n'
                f'bandit has {player_stats.enemy_HP - player_damage} left')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('you dodged, but the bandit blocked and so 0 points of damage to both.')
        if player_stats.player_action == 'block':
            print('both you and the bandit blocked')
    if player_stats.AI_action == 'attack':
        if player_stats.player_action == 'attack':
            damagelist_bandit = range(5, 25)
            damage = random.choice(damagelist_bandit)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the bandit attacked each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'bandit has {player_stats.enemy_HP - player_damage} left\n'
                  f'bandit did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_bandit = range(5, 25)
            damage = random.choice(damagelist_bandit)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you cast a spell and the bandit attacked. both you and the bandit got hit\n'
                  f'you did {player_damage} points of damage\n'
                  f'bandit has {player_stats.enemy_HP - player_damage} left\n'
                  f'bandit did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'dodge':
            damagelist_bandit = range(5, 25)
            damage = random.choice(damagelist_bandit)
            print(f'you dodged, but you dodge right in to the bandit attack\n'
                  f'bandit did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'block':
            if player_stats.player_STR > player_stats.player_INT:
                multiplier = float(player_stats.player_STR * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the bandit attack and countered it with a attack of youre own\n'
                      f'you did {player_damage} points of damage\n'
                      f'bandit has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
            elif player_stats.player_STR < player_stats.player_INT:
                multiplier = float(player_stats.player_INT * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the v attack and countered it with a magic spell\n'
                      f'you did {player_damage} points of damage\n'
                      f'bandit has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
    if player_stats.AI_action == 'magic':
        if player_stats.player_action == 'attack':
            damagelist_bandit = range(5, 25)
            damage = random.choice(damagelist_bandit)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you attacked while the bandit used magic. both got hit.\n'
                  f'you did {player_damage} points of damage\n'
                  f'bandit has {player_stats.enemy_HP - player_damage} left\n'
                  f'bandit did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'block':
            damagelist_bandit = range(5, 25)
            damage = random.choice(damagelist_bandit)
            print(f'you tried to block, but the bandit overwhelmed you with magic.\n'
                  f'bandit did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'dodge':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you dodged the bandit spell and countered it with a attack of youre own\n'
                  f'you did {player_damage} points of damage\n'
                  f'bandit has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_bandit = range(5, 25)
            damage = random.choice(damagelist_bandit)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the bandit cast spells and hit each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'bandit has {player_stats.enemy_HP - player_damage} left\n'
                  f'bandit did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.enemy_HP -= player_damage
            player_stats.player_HP -= damage
    if player_stats.AI_action == 'dodge':
        if player_stats.player_action == 'attack':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'the bandit dodged right into youre attack.\n'
                  f'you did {player_damage} points of damage\n'
                  f'bandit has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('both you and the bandit dodged')
        if player_stats.player_action == 'block':
            print('you blocked, but the bandit dodged and so 0 points of damage to both.')
        if player_stats.player_action == 'magic':
            damagelist_bandit = range(5, 25)
            damage = random.choice(damagelist_bandit)
            print(f'the bandit dodged your spell and countered.\n'
                  f'bandit did {damage} points of damage.\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage

def responds_hellhound():
    if player_stats.AI_action == 'block':
        if player_stats.player_action == 'attack':
            damagelist_hellhound = range(10, 40)
            damage = random.choice(damagelist_hellhound)
            print(f'the hellhound block your attack and counterattacked.\n'
                  f'hellhound did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'magic':
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(
                f'the hellhound tried to block your attack, but the magic was to strong and hitted the enemy\n'
                f'you did {player_damage} points of damage.\n'
                f'hellhound has {player_stats.enemy_HP - player_damage} left')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('you dodged, but the hellhound blocked and so 0 points of damage to both.')
        if player_stats.player_action == 'block':
            print('both you and the hellhound blocked')
    if player_stats.AI_action == 'attack':
        if player_stats.player_action == 'attack':
            damagelist_hellhound = range(10, 40)
            damage = random.choice(damagelist_hellhound)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the hellhound attacked each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'hellhound has {player_stats.enemy_HP - player_damage} left\n'
                  f'hellhound did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_hellhound = range(10, 40)
            damage = random.choice(damagelist_hellhound)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you cast a spell and the hellhound attacked. both you and the hellhound got hit\n'
                  f'you did {player_damage} points of damage\n'
                  f'hellhound has {player_stats.enemy_HP - player_damage} left\n'
                  f'hellhound did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            damagelist_hellhound = range(10, 40)
            damage = random.choice(damagelist_hellhound)
            print(f'you dodged, but you dodge right in to the hellhounds attack\n'
                  f'hellhound did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'block':
            if player_stats.player_STR > player_stats.player_INT:
                multiplier = float(player_stats.player_STR * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the hellhounds attack and countered it with a attack of youre own\n'
                      f'you did {player_damage} points of damage\n'
                      f'hellhound has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
            elif player_stats.player_STR < player_stats.player_INT:
                multiplier = float(player_stats.player_INT * 0.01) + 1
                damagelist_player = range(5, 40)
                player_damage = random.choice(damagelist_player) * multiplier
                print(f'you blocked the hellhounds attack and countered it with a magic spell\n'
                      f'you did {player_damage} points of damage\n'
                      f'hellhound has {player_stats.enemy_HP - player_damage} left\n')
                player_stats.enemy_HP -= player_damage
    if player_stats.AI_action == 'magic':
        if player_stats.player_action == 'attack':
            damagelist_hellhound = range(10, 40)
            damage = random.choice(damagelist_hellhound)
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you attacked while the hellhound used magic. both got hit.\n'
                  f'you did {player_damage} points of damage\n'
                  f'hellhound has {player_stats.enemy_HP - player_damage} left\n'
                  f'hellhound did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'block':
            damagelist_hellhound = range(10, 40)
            damage = random.choice(damagelist_hellhound)
            print(f'you tried to block, but the hellhound overwhelmed you with magic.\n'
                  f'hellhound did {damage} points of damage.\n'
                  f' you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage
        if player_stats.player_action == 'dodge':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'you dodged the hellhounds spell and countered it with a attack of youre own\n'
                  f'you did {player_damage} points of damage\n'
                  f'hellhound has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'magic':
            damagelist_hellhound = range(10, 40)
            damage = random.choice(damagelist_hellhound)
            multiplier = float(player_stats.player_INT * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'both you and the hellhound cast spells and hit each other\n'
                  f'you did {player_damage} points of damage\n'
                  f'hellhound has {player_stats.enemy_HP - player_damage} left\n'
                  f'hellhound did {damage} points of damage\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.enemy_HP -= player_damage
            player_stats.player_HP -= damage
    if player_stats.AI_action == 'dodge':
        if player_stats.player_action == 'attack':
            multiplier = float(player_stats.player_STR * 0.01) + 1
            damagelist_player = range(5, 40)
            player_damage = random.choice(damagelist_player) * multiplier
            print(f'the hellhound dodged right into youre attack.\n'
                  f'you did {player_damage} points of damage\n'
                  f'hellhound has {player_stats.enemy_HP - player_damage} left\n')
            player_stats.enemy_HP -= player_damage
        if player_stats.player_action == 'dodge':
            print('both you and the hellhound dodged')
        if player_stats.player_action == 'block':
            print('you blocked, but the hellhound dodged and so 0 points of damage to both.')
        if player_stats.player_action == 'magic':
            damagelist_hellhound = range(10, 40)
            damage = random.choice(damagelist_hellhound)
            print(f'the hellhound dodged your spell and countered.\n'
                  f'hellhound did {damage} points of damage.\n'
                  f'you have {player_stats.player_HP - damage} left')
            player_stats.player_HP -= damage

