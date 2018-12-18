"""The implementation of the Counter move.

It is a slightly stronger version of Tackle. Its effectiveness increases if you just received a
significant amount of damage.
"""

import random
from utils import Printer

NAME = 'Counter'
PP_COST = 5
SUCCESS_RATE = 90
CRIT_RATE = 20
CAN_DISABLE = False

def perform(user, other):
    """Perform Counter."""
    if random.randint(0, 99) < SUCCESS_RATE:
        if random.randint(0, 99) < CRIT_RATE:
            Printer.print_ui('  It\'s super effective!')
            Printer.delay_ui(1)
            base_damage = max(0, user.stats['Recent damage'] + \
                    user.stats['Strength'] - 0.5 * other.stats['Defense'])
        else:
            base_damage = max(0, 0.5 * user.stats['Recent damage'] + \
                    user.stats['Strength'] - other.stats['Defense'])
        damage = max(1, random.randint(int(0.8 * base_damage), int(1.2 * base_damage + 1)))
        if damage == 1:
            Printer.print_ui('  It deals {} point of damage.'.format(damage))
        else:
            Printer.print_ui('  It deals {} points of damage.'.format(damage))
        user.stats['Recent damage'] = damage
        other.stats['Recent damage'] = damage
        other.stats['HP'] -= damage
    else:
        Printer.print_ui('  It\'s ineffective!')
