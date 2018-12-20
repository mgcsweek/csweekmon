"""The implementation of the Mimic move.

It performs the most recent move performed by the opponent (not action), no matter what type it was.
It does not consider moves not performed due to lack of PP or Disable, but it does consider the ones
that were ineffective. It comes a constant cost. It can be Disabled.
"""

from utils import Printer

NAME = 'Mimic'
PP_COST = 9
CAN_DISABLE = True

def perform(user, other):
    """Perform Mimic."""
    move = other.stats['Previous move']
    if move is not None:
        Printer.print_ui('  {} mimics {} using {}.'.format(user.name, other.name, move.NAME))
        Printer.delay_ui(1)
        user.stats['Previous move'] = move
        move.perform(user, other)
    else:
        Printer.print_ui('  It\'s ineffective!')
