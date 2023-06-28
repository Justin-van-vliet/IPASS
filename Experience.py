import random
import player_stats

def EXP(player_STR, player_INT, player_DEX, player_HP, player_FP, enemy):
    if player_stats.enemy == 'slime':
        exp_earnedlist = range(1, 20)
    if player_stats.enemy == 'lizardman':
        exp_earnedlist = range(50, 75)
    if player_stats.enemy == 'bandit':
        exp_earnedlist = range(20, 40)
    if player_stats.enemy == 'revenant':
        exp_earnedlist = range(30, 60)
    if player_stats.enemy == 'hellhound':
        exp_earnedlist = range(40, 67)
    if player_stats.enemy == 'mothman':
        exp_earnedlist = range(30, 55)
    if player_stats.enemy == 'fenrir':
        exp_earnedlist = range(100, 300)
    if player_stats.enemy == 'golem':
        exp_earnedlist = range(100, 300)
    if player_stats.enemy == 'hydra':
        exp_earnedlist = range(100, 300)
    exp_earned = random.choice(exp_earnedlist)
    player_stats.EXP += exp_earned
    print('you have slayed the enemy\n'
          f'you earn {exp_earned} EXP\n'
          f'{player_stats.EXP}/75')
    while player_stats.EXP >= 75:
        upgrade = str(input('you have leveled-up choose a stat to upgrade\n'
                            'STR, INT, DEX or HP? '))
        if upgrade == str('STR'):
            player_stats.player_STR += 10
            player_stats.EXP -= 100
        elif upgrade == str('INT'):
            player_stats.player_INT += 10
            player_stats.EXP -= 100
        elif upgrade == str('DEX'):
            player_stats.player_DEX += 10
            player_stats.EXP -= 100
        elif upgrade == str('HP'):
            player_stats.player_HP += 100
            player_stats.EXP -= 100
        print(f'{player_stats.EXP}/75')
