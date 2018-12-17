"""The implementation of the Disable move.

This move inflicts the Disable status effect. No damage is directly inflicted, but the opponent is
unable to use certain moves until Disable is removed. The probability of Success depends on the
user's Special.
"""

import random
from utils import Printer

NAME = 'Disable'
PP_COST = 7
SUCCESS_RATE = 60
CAN_DISABLE = True

def perform(user, other):
    """Perform Disable."""
    if random.randint(0, 99 - user.stats['Special']) > SUCCESS_RATE or \
            'Disable' in other.stats['Effects']:
        Printer.print_ui('  It\'s ineffective!')
    else:
        Printer.print_ui('  {} is now unable to perform certain moves!'.format(other.name))
        other.stats['Effects'].append('Disable')
