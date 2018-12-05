"""The implementation of the Tackle move.

The most basic physical attack. It costs nothing and has no special side effects."""

import random
from utils import delay_ui, print_ui

NAME = 'Tackle'
PP_COST = 0
SUCCESS_RATE = 90
CRIT_RATE = 15

def perform(user, other):
    """Perform Tackle."""
    if random.randint(0, 100) < SUCCESS_RATE:
        if random.randint(0, 100) < CRIT_RATE:
            print_ui('  It\'s super effective!')
            delay_ui(1)
            base_damage = max(0, user.stats['Strength'] - 0.5 * other.stats['Defense'])
        else:
            base_damage = max(0, 0.7 * user.stats['Strength'] - other.stats['Defense'])
        damage = max(1, random.randint(int(0.8 * base_damage), int(1.2 * base_damage) + 1))
        if damage == 1:
            print_ui('  It deals {} point of damage.'.format(damage))
        else:
            print_ui('  It deals {} points of damage.'.format(damage))
        other.recent_damage = damage
        other.stats['HP'] -= damage
    else:
        print_ui('  It\'s ineffective!')
