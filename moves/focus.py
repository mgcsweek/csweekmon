"""The implementation of the Focus move.

It is a much stronger version of Tackle that takes two turns to perform. You cannot do anything in
the meantime. It gets cancelled if you get put to Sleep."""

import random
from utils import Printer

NAME = 'Focus'
PP_COST = 4
SUCCESS_RATE = 95
CRIT_RATE = 10
CAN_DISABLE = False

def perform(user, _):
    """Perform Focus."""
    Printer.print_ui('  {} is building up strength.'.format(user.name))
    user.stats['Effects'].append('Focus')

def finally_perform(user, other):
    """Finally do the Focus hit."""
    user.stats['Effects'].remove('Focus')
    Printer.print_ui('  {} attacks with all its might!'.format(user.name))
    Printer.delay_ui(1)
    if random.randint(0, 99) < SUCCESS_RATE:
        if random.randint(0, 99) < CRIT_RATE:
            Printer.print_ui('  It\'s super effective!')
            Printer.delay_ui(1)
            base_damage = max(0, 1.8 * user.stats['Strength'] - 0.8 * other.stats['Defense'])
        else:
            base_damage = max(0, 1.8 * user.stats['Strength'] - 1.2 * other.stats['Defense'])
        damage = max(1, random.randint(int(0.8 * base_damage), int(1.2 * base_damage + 1)))
        if damage == 1:
            Printer.print_ui('  It deals {} point of damage.'.format(damage))
        else:
            Printer.print_ui('  It deals {} points of damage.'.format(damage))
        other.stats['Recent damage'] = damage
        other.stats['HP'] -= damage
    else:
        Printer.print_ui('  It\'s ineffective!')
