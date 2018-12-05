"""Implementation of the Power Potion item.

This item increases the user's Strength by a value between 4 and 6."""

import random
from utils import print_ui

COST = 250
NAME = 'Power Potion'

def use(user, _):
    """Use a Power Potion."""
    increase = random.randint(4, 7)
    user.stats['Strength'] += increase
    print_ui('  Strength boosted by {}.'.format(increase))
