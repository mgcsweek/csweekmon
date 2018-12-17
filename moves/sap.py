"""The implementation of the Sap move.

This move decreases the opponent's Defense stat."""

import random
from utils import Printer

NAME = 'Sap'
PP_COST = 5
SUCCESS_RATE = 60
CAN_DISABLE = True

def perform(user, other):
    """Perform Sap."""
    if random.randint(0, 99 - user.stats['Special']) > SUCCESS_RATE:
        Printer.print_ui('  It\'s ineffective!')
    else:
        decrease = min(other.stats['Base Defense'], max(1, int(0.2 * user.stats['Special'])))
        other.stats['Base Defense'] -= decrease
        Printer.print_ui('  The Defense of {} drops by {}.'.format(other.name, decrease))
