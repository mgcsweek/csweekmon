"""The implementation of the Blast move.

This move is a powerful attack based on the Special stat."""

import random
from utils import Printer

NAME = 'Blast'
PP_COST = 8
SUCCESS_RATE = 80
CRIT_RATE = 15
CAN_DISABLE = True

def perform(user, other):
    """Perform Blast."""
    if random.randint(0, 99) < SUCCESS_RATE:
        if random.randint(0, 99) < CRIT_RATE:
            Printer.print_ui('  It\'s super effective!')
            Printer.delay_ui(1)
            base_damage = max(0, 1.8 * user.stats['Special'])
        else:
            base_damage = max(0, 1.2 * user.stats['Special'] - 0.2 * other.stats['Defense'])
        damage = max(1, random.randint(int(0.8 * base_damage), int(1.2 * base_damage) + 1))
        if damage == 1:
            Printer.print_ui('  It deals {} point of damage.'.format(damage))
        else:
            Printer.print_ui('  It deals {} points of damage.'.format(damage))
        other.stats['HP'] -= damage
    else:
        Printer.print_ui('  It\'s ineffective!')
