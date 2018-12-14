"""The implementation of the Glare move.

This move is an attack based on Special that damages the enemy PP."""

import random
from utils import delay_ui, print_ui

NAME = 'Glare'
PP_COST = 4
SUCCESS_RATE = 75
CRIT_RATE = 10
CAN_DISABLE = True

def perform(user, other):
    """Perform Glare."""
    if random.randint(0, 100) < SUCCESS_RATE:
        if random.randint(0, 100) < CRIT_RATE:
            print_ui('  It\'s super effective!')
            delay_ui(1)
            base_damage = 0.5 * user.stats['Special']
        else:
            base_damage = 0.3 * user.stats['Special']
        damage = max(1, random.randint(int(0.8 * base_damage), int(1.2 * base_damage) + 1),
                     other.stats['PP'])
        print_ui('  {} loses {} PP'.format(other.NAME, damage))
        other.stats['PP'] -= damage
    else:
        print_ui('  It\'s ineffective!')
