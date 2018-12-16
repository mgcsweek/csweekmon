"""Implementation of the Antidote item.

This item removes the Poison status effect."""

from utils import Printer

COST = 100
NAME = 'Antidote'

def use(user, _):
    """Use an Antidote."""
    if 'Poison' in user.stats['Effects']:
        user.stats['Effects'].remove('Poison')
        Printer.print_ui('  {} is no longer poisoned.'.format(user.name))
    else:
        Printer.print_ui('  It\'s ineffective!')
