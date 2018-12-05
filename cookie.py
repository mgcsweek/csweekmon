"""Implementation of the Cookie item.

This item restores 20 HP."""

from utils import print_ui

COST = 50
NAME = 'Cookie'

def use(user, _):
    """Use a Cookie."""
    new_hp = min(user.stats['HP'] + 20, user.stats['Max HP'])
    increase = new_hp - user.stats['HP']
    user.stats['HP'] = new_hp
    print_ui('  {} HP restored!'.format(increase))
