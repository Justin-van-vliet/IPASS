import random
import player_stats
import strategys
import acties

def playActions():
    if player_stats.enemy == 'golem':
        acties.responds_golem(player_stats)
    if player_stats.enemy == 'fenrir':
        acties.responds_fenrir(player_stats)
    if player_stats.enemy == 'hydra':
        acties.responds_hydra()
    if player_stats.enemy == 'mothman':
        acties.responds_mothman()
    if player_stats.enemy == 'lizardman':
        acties.responds_lizardman()
    if player_stats.enemy == 'slime':
        acties.responds_slime()
    if player_stats.enemy == 'revenant':
        acties.responds_hellhound()
    if player_stats.enemy == 'bandit':
        acties.responds_bandit()
    if player_stats.enemy == 'hellhound':
        acties.responds_hellhound()

def computeEquilibriumStrategies():
    user_strat = strategys.strat_01
    AI_strat = strategys.strat_01
    return [user_strat,AI_strat]

def historiesAreDiffent(player_stats):
    player_stats.past_attack = player_stats.history_previous.count('attack')
    player_stats.past_dodge = player_stats.history_previous.count('dodge')
    player_stats.past_block = player_stats.history_previous.count('block')
    player_stats.past_magic = player_stats.history_previous.count('magic')
    player_stats.hisc_attack = player_stats.history_current.count('attack')
    player_stats.hisc_dodge = player_stats.history_current.count('dodge')
    player_stats.hisc_block = player_stats.history_current.count('block')
    player_stats.hisc_magic = player_stats.history_current.count('magic')
    lijst_p = [player_stats.past_attack,player_stats.past_dodge,player_stats.past_block,player_stats.past_magic]
    lijst_c = [player_stats.hisc_attack,player_stats.hisc_dodge,player_stats.hisc_block,player_stats.hisc_magic]
    if lijst_p == lijst_c:
        player_stats.HAD_result = 0
    else:
        player_stats.HAD_result = 1
    return player_stats.HAD_result

print(historiesAreDiffent(player_stats))

def historyIsEquilibrium(player_stats):
    if player_stats.history_current == player_stats.equilibriumStrategies[0]:
        player_stats.HIS_result = 0
    else:
        player_stats.HIS_result = 1

def computeOptimalStrategy():
    player_stats.hisc_attack = player_stats.history_current.count('attack')
    player_stats.hisc_dodge = player_stats.history_current.count('dodge')
    player_stats.hisc_block = player_stats.history_current.count('block')
    player_stats.hisc_magic = player_stats.history_current.count('magic')
    if len(player_stats.history_previous) == 0:
        player_stats.strategy = strategys.strat_01
    elif player_stats.hisc_attack >= 1 and player_stats.hisc_magic == 0 and player_stats.hisc_block == 0 and player_stats.hisc_dodge == 0:
        player_stats.strategy = strategys.strat_04
    elif player_stats.hisc_block >= 1 and player_stats.hisc_magic == 0 and player_stats.hisc_attack == 0 and player_stats.hisc_dodge == 0:
        player_stats.strategy = strategys.strat_05
    elif player_stats.hisc_dodge >= 1 and player_stats.hisc_magic == 0 and player_stats.hisc_block == 0 and player_stats.hisc_attack == 0:
        player_stats.strategy = strategys.strat_02
    elif player_stats.hisc_magic >= 1 and player_stats.hisc_attack == 0 and player_stats.hisc_block == 0 and player_stats.hisc_dodge == 0:
        player_stats.strategy = strategys.strat_03
    elif player_stats.hisc_attack >= 1 and player_stats.hisc_dodge >= 1 and player_stats.hisc_magic == 0 and player_stats.hisc_block == 0:
        player_stats.strategy = strategys.strat_07
    elif player_stats.hisc_attack >= 1 and player_stats.hisc_block >= 1 and player_stats.hisc_magic == 0 and player_stats.hisc_dodge == 0:
        player_stats.strategy = strategys.strat_11
    elif player_stats.hisc_attack >= 1 and player_stats.hisc_magic >= 1 and player_stats.hisc_dodge == 0 and player_stats.hisc_block == 0:
        player_stats.strategy = strategys.strat_09
    elif player_stats.hisc_dodge >= 1 and player_stats.hisc_block >= 1 and player_stats.hisc_magic == 0 and player_stats.hisc_attack == 0:
        player_stats.strategy = strategys.strat_08
    elif player_stats.hisc_dodge >= 1 and player_stats.hisc_magic >= 1 and player_stats.hisc_attack == 0 and player_stats.hisc_block == 0:
        player_stats.strategy = strategys.strat_06
    elif player_stats.past_block >= 1 and player_stats.hisc_magic >= 1 and player_stats.past_attack == 0 and player_stats.hisc_dodge == 0:
        player_stats.strategy = strategys.strat_10
    elif player_stats.hisc_attack == 1 and player_stats.hisc_dodge == 1 and player_stats.hisc_block == 1:
        player_stats.strategy = strategys.strat_14
    elif player_stats.hisc_attack == 1 and player_stats.hisc_dodge == 1 and player_stats.hisc_magic == 1:
        player_stats.strategy = strategys.strat_12
    elif player_stats.hisc_attack == 1 and player_stats.past_block == 1 and player_stats.hisc_magic == 1:
        player_stats.strategy = strategys.strat_15
    elif player_stats.hisc_dodge == 1 and player_stats.hisc_block == 1 and player_stats.hisc_magic == 1:
        player_stats.strategy = strategys.strat_13
    return player_stats.strategy

def awesome():
    while player_stats.enemy_HP > 0 and player_stats.player_HP > 0:
        APS = True
        APPE = True
        B = False
        T = 0
        player_stats.history_current = []
        player_stats.history_previous = []
        player_stats.equilibriumStrategies = computeEquilibriumStrategies()
        player_stats.strategy = player_stats.equilibriumStrategies[1]
        while APS:
            player_stats.AI_action = random.choice(player_stats.strategy)
            player_stats.player_action = input('What will you do? attack,block, dodge or magic? ')
            if player_stats.player_action == 'attack' or player_stats.player_action == 'dodge' or player_stats.player_action == 'block' or player_stats.player_action == 'magic':
                player_stats.history_current.append(player_stats.player_action)
                print(player_stats.player_action)
            else:
                print('that is not a valid action.')
                player_stats.player_action = input('What will you do? attack,block, dodge or magic? ')
                player_stats.history_current.append(player_stats.player_action)
            playActions()
            if APPE == False:
                if B == False:
                    historiesAreDiffent(player_stats)
                    if player_stats.HAD_result > 0:
                        APS = False
                B = False
                computeOptimalStrategy()
            if APPE == True:
                if len(player_stats.history_current) > len(player_stats.history_previous):
                    player_stats.history_previous.append(player_stats.player_action)
                historyIsEquilibrium(player_stats)
                if player_stats.HIS_result > 0:
                    APPE = False
                    player_stats.strategy = strategys.strat_01
                    B = True
            while len(player_stats.history_current) > 3:
                player_stats.history_current.remove(player_stats.history_current[0])
            while len(player_stats.history_previous) > 3:
                player_stats.history_previous.remove(player_stats.history_previous[0])
            player_stats.history_previous.append(player_stats.player_action)
            T += 1
            with open('stats.txt', 'a') as tpa:
                try:
                    tpa.write(player_stats.player_action+ '\n')
                finally:tpa.close()

