import player_stats

def Class(player_STR, player_INT, choose, player_DEX, player_HP, player):
    while player_stats.choose == 0:
        player_stats.choose = int(input('choose your class: warrior(1)/mage(2)/rogue(3): '))
        if player_stats.choose > 4:
            print('that class doesnt exist.')
            player_stats.choose = 0
        if player_stats.choose == 1:
            print('class: warrior\n'
                  'STR = 10\n'
                  'INT = 3\n'
                  'DEX = 4\n'
                  'HP = 125\n')
            player_stats.Player_Class = 'warrior'
            player_stats.player_STR += 10
            player_stats.player_INT += 3
            player_stats.player_DEX += 4
            player_stats.player_HP += 25
        elif player_stats.choose == 2:
            print('class: mage\n'
                  'STR = 2\n'
                  'INT = 15\n'
                  'DEX = 6\n')
            player_stats.Player_Class = 'mage'
            player_stats.player_STR += 2
            player_stats.player_INT += 10
            player_stats.player_DEX += 6
        elif player_stats.choose == 3:
            print('class: rogue\n'
                  'STR = 4\n'
                  'INT = 5\n'
                  'DEX = 9\n')
            player_stats.Player_Class = 'rogue'
            player_stats.player_STR += 4
            player_stats.player_INT += 5
            player_stats.player_DEX += 9
        elif player_stats.choose == 4:
            print('class: god of death\n'
                  'str = 100\n'
                  'int = 100\n'
                  'dex = 100\n'
                  'HP = 10000\n '
                  'FP = 10000\n')
            player_stats.Player_Class = 'god of death'
            player_stats.player_STR += 100
            player_stats.player_INT += 100
            player_stats.player_DEX += 100
            player_stats.player_HP += 9900
        sure = str(input('are you sure? Y/N '))
        if sure == str('Y'):
            print(f'youre class is now {player_stats.Player_Class}\n')
            print(f'STR: {player_stats.player_STR} INT: {player_stats.player_INT} DEX: {player_stats.player_DEX} HP: {player_stats.player_HP} ')
        elif sure == str('N'):
            player_stats.player_STR = 0
            player_stats.player_INT = 0
            player_stats.player_DEX = 0
            player_stats.player_HP = 100
            player_stats.choose = 0