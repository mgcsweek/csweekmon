"""Entry point for the game."""

import argparse

import game_engine
import strategies
from utils import Printer
from csweekmon import Csweekmon

STRATEGIES = [
    (strategies.SimpleStrategy, strategies.RandomStrategy),
    (strategies.TankStrategy, strategies.GlassCannonStrategy),
    (strategies.HeavyHitStrategy, strategies.HugePowerStrategy)
]
NSTRATEGIES = len(STRATEGIES)
SCORES = dict()
WINS = dict()
DRAW = dict()
LOSS = dict()

def main():
    """Run tournament."""
    # Validate strategies and make sure they have unique names
    for strategy in STRATEGIES:
        agent_a = Csweekmon(strategy[0], True)
        agent_b = Csweekmon(strategy[1], True)
        name_a = agent_a.stats['Name']
        name_b = agent_b.stats['Name']
        if name_a in SCORES:
            print('Name {} used in two strategies, please change this and rerun.'.format(name_a))
            exit(0)
        if name_b in SCORES:
            print('Name {} used in two strategies, please change this and rerun.'.format(name_b))
            exit(0)
        SCORES[name_a] = 0
        if not game_engine.verify(agent_a):
            print("Strategy {} disqualified: failed game engine verification.".format(name_a))
            SCORES[name_a] = -1
        else:
            print('Strategy {} is valid.'.format(name_a))
        if not game_engine.verify(agent_b):
            print("Strategy {} disqualified: failed game engine verification.".format(name_b))
            SCORES[name_a] = -1
        else:
            print('Strategy {} is valid.'.format(name_b))
        WINS[name_a] = 0
        DRAW[name_a] = 0
        LOSS[name_a] = 0

    # Run the tournament
    battle_idx = 0
    num_battles = NSTRATEGIES * (NSTRATEGIES - 1)
    for i in range(NSTRATEGIES):
        for j in range(NSTRATEGIES):
            if i != j:
                battle_idx += 1
                csw1_a, csw2_a = (Csweekmon(STRATEGIES[i][0], True),
                                  Csweekmon(STRATEGIES[j][0], False))
                csw1_b, csw2_b = (Csweekmon(STRATEGIES[i][1], False),
                                  Csweekmon(STRATEGIES[j][1], False))
                print('###Battle {}/{}: {} & {} vs {} & {}'.format(battle_idx, num_battles,
                                                                   csw1_a.name, csw1_b.name,
                                                                   csw2_a.name, csw2_b.name))
                if SCORES[csw1_a.name] == -1 or SCORES[csw2_a.name] == -1:
                    print('   Battle skipped, at least one competitor was DQ!')
                    continue
                outcome = game_engine.run_battle(csw1_a, csw2_a, csw1_b, csw2_b)

                if outcome == 1:
                    SCORES[csw1_a.name] += 3
                    WINS[csw1_a.name] += 1
                    LOSS[csw2_a.name] += 1
                    print('   Winner: {} & {}'.format(csw1_a.name, csw1_b.name))
                elif outcome == 2:
                    SCORES[csw2_a.name] += 3
                    WINS[csw2_a.name] += 1
                    LOSS[csw1_a.name] += 1
                    print('   Winner: {} & {}'.format(csw2_a.name, csw2_b.name))
                else:
                    SCORES[csw1_a.name] += 1
                    SCORES[csw2_a.name] += 1
                    DRAW[csw1_a.name] += 1
                    DRAW[csw2_a.name] += 1
                    print('   It\'s a draw!')

    # print scoreboard
    print('SCOREBOARD:')
    print('|-rank-|--------name--------|-pts-|-mpl-|--v--|--d--|--l--|')
    print('-'*59)
    matches_played = 2 * (NSTRATEGIES - 1)
    sorted_scores = sorted(SCORES.items(), key=lambda kv: kv[1], reverse=True)
    rank = 1
    for name, pts in sorted_scores:
        print('|{}|{}|{}|{}|{}|{}|{}|'.format(str(rank).center(6), name.center(20),
                                              str(pts).center(5), str(matches_played).center(5),
                                              str(WINS[name]).center(5), str(DRAW[name]).center(5),
                                              str(LOSS[name]).center(5)))
        rank += 1
    print('-'*59)

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
