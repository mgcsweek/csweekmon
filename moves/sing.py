"""The implementation of the Sing move.

This move inflicts the Sleep status effect. There is no immediate damage, but the opponent will not
be able to perform any actions until they wake up.
"""

import random
from utils import Printer

NAME = 'Sing'
PP_COST = 6
SUCCESS_RATE = 50
WAKEUP_RATE = 40
CAN_DISABLE = True

def perform(user, other):
    """Perform Sing."""
    Printer.print_ui('  ♪ The sound of {} singing fills the area. ♫'.format(user.name))
    Printer.delay_ui(1)
    if random.randint(0, 100 - user.stats['Special']) > SUCCESS_RATE or \
            'Sleep' in other.stats['Effects']:
        Printer.print_ui('  It\'s ineffective!')
    else:
        Printer.print_ui('  {} is now asleep!'.format(other.name))
        other.stats['Effects'].append('Sleep')

def wakeup():
    """Determine whether the afflicted should wake up."""
    return random.randint(0, 100) < WAKEUP_RATE
