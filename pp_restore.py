"""Implementation of the PP Restore item.

This item restores 25 PP."""

from utils import print_ui

COST = 200
NAME = 'PP Restore'

def use(user, _):
    """Use a PP Restore."""
    new_pp = min(user.stats['PP'] + 25, user.stats['Max PP'])
    increase = new_pp - user.stats['PP']
    user.stats['PP'] = new_pp
    print_ui('  {} PP restored!'.format(increase))
