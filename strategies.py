"""A few default strategies."""

import random

from actions import Action
from utils import Printer

from game_engine import MOVES, ITEMS, MOVE_COUNT, MAX_ITEMS, MAX_COST, STAT_POINTS
from game_engine import HP_W, PP_W, STR_W, DEF_W, SPEC_W
ALL_MOVES_COUNT = len(MOVES)
ALL_ITEMS_COUNT = len(ITEMS)

class SimpleStrategy:

    def __init__(self):
        self.used_cookies = 0
        self.own_stats = {}
        self.enemy_stats = {}

    def set_initial_stats(self):
        return {'Name': 'Simple',
                'HP': 37,
                'PP': 17,
                'Strength': 10,
                'Defense': 5,
                'Special': 8,
                'Moves': [0, 1, 3],
                'Items': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

    def set_order_info(self, is_first):
        pass

    def receive_my_stats(self, own_stats):
        self.own_stats = own_stats

    def receive_enemy_stats(self, enemy_info):
        self.enemy_stats = enemy_info

    def choose_action(self):
        if self.own_stats['HP'] <= 10 and self.used_cookies <= 10:
            self.used_cookies += 1
            return Action.USE_ITEM, self.used_cookies - 1
        if 'Sleep' not in self.enemy_stats['Effects'] and self.own_stats['PP'] >= 6:
            return Action.PERFORM_MOVE, 2
        if 'Poison' not in self.enemy_stats['Effects'] and self.own_stats['PP'] >= 5:
            return Action.PERFORM_MOVE, 1
        return Action.PERFORM_MOVE, 0


class TankStrategy:

    def __init__(self):
        self.turn = 2
        self.stats = {}

    def set_initial_stats(self):
        return {'Name': 'Tank',
                'HP': 50,
                'PP': 10,
                'Strength': 8,
                'Defense': 8,
                'Special': 4,
                'Moves': [4, 0, 0],
                'Items': []}

    def set_order_info(self, is_first):
        pass

    def receive_my_stats(self, own_stats):
        self.stats = own_stats

    def receive_enemy_stats(self, enemy_info):
        pass

    def choose_action(self):
        if self.turn > 0:
            self.turn -= 1
            return Action.PERFORM_MOVE, 0
        return Action.PERFORM_MOVE, 1


class HugePowerStrategy:

    def __init__(self):
        self.stats = {}
        self.enemy_stats = {}
        self.cookies_left = 10

    def set_initial_stats(self):
        return {'Name': 'Huge Power',
                'HP': 35,
                'PP': 35,
                'Strength': 0,
                'Defense': 5,
                'Special': 10,
                'Moves': [6, 10, 12],
                'Items': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

    def set_order_info(self, is_first):
        pass

    def receive_my_stats(self, own_stats):
        self.stats = own_stats

    def receive_enemy_stats(self, enemy_info):
        self.enemy_stats = enemy_info

    def choose_action(self):
        if self.enemy_stats['Previous move'] == 'Focus':
            return Action.BLOCK, 0
        if self.stats['HP'] <= 15:
            if self.stats['PP'] >= 6:
                return Action.PERFORM_MOVE, 2
            if self.cookies_left > 0:
                self.cookies_left -= 1
                return Action.USE_ITEM, self.cookies_left
        if self.stats['PP'] >= 14:
            return Action.PERFORM_MOVE, 1
        if self.stats['PP'] >= 8:
            return Action.PERFORM_MOVE, 0
        return Action.BLOCK, 0

class GlassCannonStrategy:

    def __init__(self):
        self.stats = {}
        self.enemy_stats = {}

    def set_initial_stats(self):
        return {'Name': 'Glass Cannon',
                'HP': 30,
                'PP': 30,
                'Strength': 5,
                'Defense': 5,
                'Special': 10,
                'Moves': [0, 1, 6],
                'Items': []}

    def set_order_info(self, is_first):
        pass

    def receive_my_stats(self, own_stats):
        self.stats = own_stats

    def receive_enemy_stats(self, enemy_info):
        self.enemy_stats = enemy_info

    def choose_action(self):
        if self.enemy_stats['Previous move'] == 'Focus':
            return Action.BLOCK, 0
        if self.stats['PP'] >= 26:
            return Action.PERFORM_MOVE, 1
        if self.stats['PP'] >= 8:
            return Action.PERFORM_MOVE, 2
        return Action.PERFORM_MOVE, 0


class RandomStrategy:

    def __init__(self):
        pass

    def set_initial_stats(self):
        return {'Name': 'Random',
                'HP': 32,
                'PP': 12,
                'Strength': 15,
                'Defense': 5,
                'Special': 8,
                'Moves': [0, 1, 2],
                'Items': []}

    def set_order_info(self, is_first):
        pass

    def receive_my_stats(self, own_stats):
        pass

    def receive_enemy_stats(self, enemy_info):
        pass

    def choose_action(self):
        return Action.PERFORM_MOVE, random.randint(0, 2)


class HeavyHitStrategy:

    def __init__(self):
        self.used_kits = 0
        self.used_cookies = 0
        self.used_power = 0
        self.stats = {}

    def set_initial_stats(self):
        return {'Name': 'Heavy Hit',
                'HP': 60,
                'PP': 10,
                'Strength': 15,
                'Defense': 0,
                'Special': 0,
                'Moves': [0, 2, 7],
                'Items': [1, 0, 2]}

    def set_order_info(self, is_first):
        pass

    def receive_my_stats(self, own_stats):
        self.stats = own_stats

    def receive_enemy_stats(self, enemy_info):
        pass

    def choose_action(self):
        if self.stats['HP'] <= 20:
            if self.used_kits < 1:
                self.used_kits += 1
                return Action.USE_ITEM, 0
            if self.used_cookies < 1:
                self.used_cookies += 1
                return Action.USE_ITEM, 1
        if self.used_power < 1:
            self.used_power += 1
            return Action.USE_ITEM, 2
        if self.stats['PP'] >= 5 and self.stats['Recent damage'] >= 10:
            return Action.PERFORM_MOVE, 1
        if self.stats['PP'] >= 4:
            return Action.PERFORM_MOVE, 2
        return Action.PERFORM_MOVE, 0


class HumanStrategy:

    def __init__(self):
        self.my_stats = {}
        self.enemy_stats = {}

    def set_initial_stats(self):
        Printer.print_ui('***********************************')
        Printer.print_ui('        Initialise stats')
        name = 'Human'

        points_left = STAT_POINTS
        stats = {'HP': (0, HP_W),
                 'PP': (0, PP_W),
                 'Strength': (0, STR_W),
                 'Defense': (0, DEF_W),
                 'Special': (0, SPEC_W)}
        while points_left > 0:
            Printer.print_ui('Options: ({} points remaining)'.format(points_left))
            for key, val in stats.items():
                Printer.print_ui(' * \'{} n\' - Increase {} by at most {}'.format(key, key, \
                        points_left // val[1]))
            inp = input()
            inp = inp.split(' ')
            if len(inp) != 2:
                continue
            if inp[0] in [x for x, y in stats.items()]:
                points, weight = stats[inp[0]]
                if inp[1].isdigit:
                    stats[inp[0]] = (points + int(inp[1]), weight)
                points_left = points_left - weight * int(inp[1])

        moves = []
        while len(moves) < MOVE_COUNT:
            Printer.print_ui('Options:')
            for i, move in enumerate(MOVES):
                Printer.print_ui(' * \'{}\' - Add move {}'.format(i, move.NAME))
            inp = input()
            if inp.isdigit():
                moves.append(int(inp))

        items = []

        item_cost = [x.COST for x in ITEMS]
        money_remaining = MAX_COST
        while money_remaining >= min([item_cost[i] for i in range(ALL_ITEMS_COUNT)]) and \
              len(items) < MAX_ITEMS:
            Printer.print_ui('Options: ({} credits remaining)'.format(money_remaining))
            for i in range(ALL_ITEMS_COUNT):
                if item_cost[i] <= money_remaining:
                    Printer.print_ui(' * \'{}\' - Buy {} ({} credits)'.format(i + 1, ITEMS[i].NAME,
                                                                              ITEMS[i].COST))
            inp = input()
            if inp.isdigit():
                if int(inp) in range(1, ALL_ITEMS_COUNT + 1):
                    items.append(int(inp) - 1)
                    money_remaining -= ITEMS[int(inp) - 1].COST
                else:
                    break

        return {'Name': name,
                'HP': stats['HP'][0],
                'PP': stats['PP'][0],
                'Strength': stats['Strength'][0],
                'Defense': stats['Defense'][0],
                'Special': stats['Special'][0],
                'Moves': moves,
                'Items': items}

    def set_order_info(self, is_first):
        pass

    def receive_my_stats(self, own_stats):
        self.my_stats = own_stats

    def receive_enemy_stats(self, enemy_info):
        self.enemy_stats = enemy_info

    def choose_action(self):
        Printer.print_ui('***********************************')
        Printer.print_ui('        Choose Action')
        Printer.print_ui('Options:')
        for i in range(len(self.my_stats['Moves'])):
            move = self.my_stats['Moves'][i]
            Printer.print_ui(' * \'move {}\' - Perform {}'.format(i, MOVES[move].NAME))
        for i, item in enumerate(self.my_stats['Items']):
            if item != -1:
                Printer.print_ui(' * \'item {}\' - Use {}'.format(i, ITEMS[item].NAME))
        Printer.print_ui(' * \'block\'  - Perform Block')

        while True:
            inp = input()
            if inp == 'block':
                return Action.BLOCK, 0

            inp = inp.split(' ')

            if len(inp) == 2 and inp[1].isdigit():
                if inp[0] == 'move':
                    return Action.PERFORM_MOVE, int(inp[1])
                if inp[0] == 'item':
                    return Action.USE_ITEM, int(inp[1])
            Printer.print_ui('Invalid command!')
