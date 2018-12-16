"""Implementation of the Echo Screen item.

This item removes the Disable status effect."""

from utils import Printer

COST = 100
NAME = 'Echo Screen'

def use(user, _):
    """Use an Echo Screen."""
    if 'Disable' in user.stats['Effects']:
        user.stats['Effects'].remove('Disable')
        Printer.print_ui('  {} can use special moves again.'.format(user.name))
    else:
        Printer.print_ui('  It\'s ineffective!')
