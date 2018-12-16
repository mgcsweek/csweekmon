"""Utilities for UI."""

import time

class Printer:
    VERBOSE_OUTPUT = True
    DELAY = 1

    @staticmethod
    def print_ui(text=''):
        """Print text to standard output if verbose output set."""
        if Printer.VERBOSE_OUTPUT:
            print(text)

    @staticmethod
    def delay_ui(seconds):
        """Delay for a certain number of seconds if verbose output set."""
        if Printer.VERBOSE_OUTPUT:
            time.sleep(seconds * Printer.DELAY)
