"""Implementation of the Antidote item.

This item removes the Poison status effect."""

from utils import print_ui

COST = 100
NAME = 'Antidote'

def use(user, _):
    """Use an Antidote."""
    if 'Poison' in user.stats['Effects']:
        user.stats['Effects'].remove('Poison')
        print_ui('  {} is no longer poisoned.'.format(user.name))
    else:
        print_ui('  It\'s ineffective!')
