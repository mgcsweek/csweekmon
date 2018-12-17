"""Entry point for the game."""

import argparse

import game_engine
import strategies
from utils import Printer
from csweekmon import Csweekmon

STRATEGIES = [
    strategies.HumanStrategy,
    strategies.RandomStrategy,
    strategies.SimpleStrategy
]
NSTRATEGIES = len(STRATEGIES)
SCORES = dict()

def main():
    """Run tournament."""
    # Validate strategies and make sure they have unique names
    for strategy in STRATEGIES:
        agent = Csweekmon(strategy, True)
        name = agent.stats['Name']
        if name in SCORES:
            print('Name {} used in two strategies, please change this and rerun.'.format(name))
            exit(0)
        if not game_engine.verify(agent):
            print("Strategy {} disqualified: failed game engine verification.".format(name))
            SCORES[name] = -1
        else:
            print('Strategy {} is valid.'.format(name))
        SCORES[name] = 0

    # Run the tournament
    battle_idx = 0
    num_battles = NSTRATEGIES * (NSTRATEGIES - 1)
    for i in range(NSTRATEGIES):
        for j in range(NSTRATEGIES):
            if i != j:
                battle_idx += 1
                csw1, csw2 = Csweekmon(STRATEGIES[i], True), Csweekmon(STRATEGIES[j], False)
                print('###Battle {}/{}: {} vs {}'.format(battle_idx, num_battles,
                                                         csw1.name, csw2.name))
                if SCORES[csw1.name] == -1 or SCORES[csw2.name] == -1:
                    print('   Battle skipped, at least one competitor was DQ!')
                    continue
                outcome = game_engine.run_battle(csw1, csw2)
                
                if outcome == 1:
                    SCORES[csw1.name] += 3
                    print('   Winner: {}'.format(csw1.name))
                elif outcome == 2:
                    SCORES[csw2.name] += 3
                    print('   Winner: {}'.format(csw2.name))
                else:
                    SCORES[csw1.name] += 1
                    SCORES[csw2.name] += 1
                    print('   It\'s a draw!')

    # print scoreboard
    print('SCOREBOARD:')
    print('|-rank-|--------name--------|-pts-|-mpl-|')
    print('-'*41)
    matches_played = 2 * (NSTRATEGIES - 1)
    sorted_scores = sorted(SCORES.items(), key=lambda kv: kv[1], reverse=True)
    rank = 1
    for name, pts in sorted_scores:
        print('|{}|{}|{}|{}|'.format(str(rank).center(6), name.center(20),
                                     str(pts).center(5), str(matches_played).center(5)))
        rank += 1
    print('-'*41)

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    PARSER.add_argument('--no-verbose', action='store_true',
                        help='disable verbose output of the matches (skip to final scoreboard')
    PARSER.add_argument('--delay', type=float, metavar='D', default=1.0,
                        help='number of seconds between ui ticks if verbose mode is on')
    ARGS = PARSER.parse_args()
    Printer.VERBOSE_OUTPUT = not ARGS.no_verbose
    Printer.DELAY = ARGS.delay
    main()
