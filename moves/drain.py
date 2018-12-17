"""The implementation of the Drain move.

This move is a weak attack based on Special that will also heal the user by the amount that it
damages the target."""

import random
from utils import Printer

NAME = 'Drain'
PP_COST = 6
SUCCESS_RATE = 80
CRIT_RATE = 10
CAN_DISABLE = True

def perform(user, other):
    """Perform Drain."""
    if random.randint(0, 99) < SUCCESS_RATE:
        if random.randint(0, 99) < CRIT_RATE:
            Printer.print_ui('  It\'s super effective!')
            Printer.delay_ui(1)
            base_damage = max(0, 0.6 * user.stats['Special'])
        else:
            base_damage = max(0, 0.4 * user.stats['Special'] - 0.2 * other.stats['Defense'])
        damage = max(1, random.randint(int(0.8 * base_damage), int(1.2 * base_damage) + 1),
                     other.stats['HP'])
        Printer.print_ui('  {} drains {} HP from {}.'.format(user.NAME, damage, other.NAME))
        other.stats['HP'] -= damage
        user.stats['HP'] = min(user.stats['Max HP'], user.stats['HP'] + damage)
    else:
        Printer.print_ui('  It\'s ineffective!')
