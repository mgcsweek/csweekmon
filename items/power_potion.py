"""Implementation of the Power Potion item.

This item increases the user's Strength by a value between 4 and 6."""

import random
from utils import Printer

COST = 250
NAME = 'Power Potion'

def use(user, _):
    """Use a Power Potion."""
    increase = random.randint(4, 6)
    user.stats['Strength'] += increase
    Printer.print_ui('  Strength boosted by {}.'.format(increase))
