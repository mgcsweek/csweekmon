"""The implementation of the Sap move.

This move decreases the opponent's Defense stat."""

import random
from utils import print_ui

NAME = 'Sap'
PP_COST = 5
SUCCESS_RATE = 60

def perform(user, other):
    """Perform Sap."""
    if random.randint(0, 100 - user.stats['Special']) > SUCCESS_RATE:
        print_ui('  It\'s ineffective!')
    else:
        decrease = min(other.stats['Defense'], max(1, int(0.2 * user.stats['Special'])))
        user.stats['Defense'] -= decrease
        print_ui('  The Defense of {} drops by {}.'.format(other.name, decrease))
