"""Implementation of the Health Kit item.

This item restores 50 HP."""

from utils import Printer

COST = 200
NAME = 'Health Kit'

def use(user, _):
    """Use a Health Kit."""
    new_hp = min(user.stats['HP'] + 50, user.stats['Max HP'])
    increase = new_hp - user.stats['HP']
    user.stats['HP'] = new_hp
    Printer.print_ui('  {} HP restored!'.format(increase))
