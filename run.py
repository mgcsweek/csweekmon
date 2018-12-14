"""Entry point for the game."""

import sys

import game_engine
import strategies
from strategies import Csweemon

AGENTS = [
    strategies.RandomStrategy,
    strategies.SimpleStrategy,
    strategies.TankStrategy,
    strategies.GlassCannonStrategy,
    strategies.HeavyHitStrategy
]
NAGENTS = len(AGENTS)
POINTS = [0] * NAGENTS

def main(argv):
    """Run tournament."""
    # TODO: parse command line arguments
    for i in range(NAGENTS):
        for j in range(NAGENTS):
            if i != j:
                csw1, csw2 = Csweemon(AGENTS[i], True), Csweemon(AGENTS[j], False)
                if not game_engine.verify(csw1):
                    POINTS[i] -= 1
                    break
                if not game_engine.verify(csw2):
                    POINTS[j] -= 1
                    break
                outcome = game_engine.run_battle(csw1, csw2)
                if outcome != -1:
                    if outcome == 1:
                        POINTS[i] += 1
                    else:
                        POINTS[j] += 1
    print('SCOREBOARD:')
    for i in range(NAGENTS):
        agent = Csweemon(AGENTS[i], True)
        print('  {}:    {}/{}'.format(agent.stats['Name'], POINTS[i], 2 * (NAGENTS - 1)))

if __name__ == "__main__":
    main(sys.argv[1:])
