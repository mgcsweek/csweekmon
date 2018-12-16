class Csweemon:
    """Class representing instances of fighters."""

    def __init__(self, ai_strategy, is_first):
        self.strategy = ai_strategy()
        self.stats = self.strategy.set_initial_stats()
        self.stats['Max HP'] = self.stats['HP']
        self.stats['Max PP'] = self.stats['PP']
        self.stats['Base Defense'] = self.stats['Defense']
        self.stats['Effects'] = []
        self.stats['Previous move'] = None
        self.stats['Recent damage'] = 0
        self.stats['Poison strength'] = 0
        self.name = self.stats['Name']
        self.strategy.set_order_info(is_first)

    def give_stats_info(self, other_stats):
        """Forward information about own and enemy stats to underlying strategy."""
        self.strategy.receive_my_stats(self.stats)
        self.strategy.receive_enemy_stats(other_stats)

    def choose_action(self):
        """Perform an action during own turn."""
        return self.strategy.choose_action()