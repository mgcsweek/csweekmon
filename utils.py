"""Utilities for UI."""

import time

VERBOSE_OUTPUT = True
TIME_SCALE = 1

def print_ui(text=''):
    """Print text to standard output if verbose output set."""
    if VERBOSE_OUTPUT:
        print(text)

def delay_ui(seconds):
    """Delay for a certain number of seconds if verbose output set."""
    if VERBOSE_OUTPUT:
        time.sleep(seconds * TIME_SCALE)
