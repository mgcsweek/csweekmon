"""Entry point for the game."""

import sys

import game_engine
import strategies
from csweemon import Csweemon

STRATEGIES = [
    strategies.RandomStrategy,
    strategies.SimpleStrategy,
    strategies.TankStrategy,
    strategies.GlassCannonStrategy,
    strategies.HeavyHitStrategy
]
NSTRATEGIES = len(STRATEGIES)
SCORES = dict()

def main(argv):
    """Run tournament."""
    # TODO: parse command line arguments

    # Validate strategies and make sure they have unique names
    for strategy in STRATEGIES:
        agent = Csweemon(strategy, True)
        name = agent.stats['Name']
        if name in SCORES:
            print('Name {} used in two strategies, please change this and rerun.'.format(name))
            exit(0)
        if not game_engine.verify(agent):
            print("Strategy {} disqualified: failed game engine verification.".format(name))
            SCORES[name] = -1
        SCORES[name] = 0

    # Run the tournament
    for i in range(NSTRATEGIES):
        for j in range(NSTRATEGIES):
            if i != j:
                csw1, csw2 = Csweemon(STRATEGIES[i], True), Csweemon(STRATEGIES[j], False)
                if SCORES[csw1.name] == -1 or SCORES[csw2.name] == -1:
                    continue
                outcome = game_engine.run_battle(csw1, csw2)
                if outcome != -1:
                    if outcome == 1:
                        SCORES[csw1.name] += 1
                    else:
                        SCORES[csw2.name] += 1

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
    main(sys.argv[1:])
