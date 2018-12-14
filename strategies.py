"""A few default strategies."""

import random
from actions import Action

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


class GlassCannonStrategy:

    def __init__(self):
        self.stats = {}

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
        pass

    def choose_action(self):
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
