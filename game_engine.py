"""Main battle system implementation."""

from random import randint

# items
from items import antidote
from items import cookie
from items import echo_screen
from items import health_kit
from items import power_potion
from items import pp_restore

# moves
from moves import blast
from moves import blaze
from moves import counter
from moves import disable
from moves import drain
from moves import focus
from moves import glare
from moves import harden
from moves import kick
from moves import mimic
from moves import poison
from moves import sap
from moves import sing
from moves import tackle

from utils import Printer
from actions import Action

MOVES = [
    tackle,
    poison,
    counter,
    sing,
    harden,
    sap,
    blast,
    focus,
    disable,
    kick,
    blaze,
    mimic,
    drain,
    glare
]
ITEMS = [
    cookie,
    health_kit,
    power_potion,
    pp_restore,
    antidote,
    echo_screen
]
ALL_MOVES_COUNT = len(MOVES)
ALL_ITEMS_COUNT = len(ITEMS)
MOVE_COUNT = 3
MAX_ITEMS = 10
MAX_COST = 500
STAT_POINTS = 100
HP_W, PP_W, STR_W, DEF_W, SPEC_W = 1, 1, 2, 2, 2

def verify(csweekmon, max_cost=MAX_COST, stat_points=STAT_POINTS):
    """Verify that the players have valid initialisation."""
    item_cost = [x.COST for x in ITEMS]
    stats = csweekmon.stats
    health = stats['HP']
    ppoints = stats['PP']
    strength = stats['Strength']
    defense = stats['Defense']
    special = stats['Special']
    moves = stats['Moves']
    items = stats['Items']
    effects = stats['Effects']
    return (all([x >= 0 for x in [ppoints, strength, defense, special]])
            and health > 0
            and HP_W * health + PP_W * ppoints + STR_W * strength + \
                    DEF_W * defense + SPEC_W * special <= stat_points
            and len(moves) == MOVE_COUNT
            and all([i in range(ALL_MOVES_COUNT) for i in moves])
            and len(items) <= MAX_ITEMS
            and all([i in range(ALL_ITEMS_COUNT) for i in items])
            and sum([item_cost[i] for i in items]) <= max_cost
            and effects == [])


def write_stats(turn_number, agent_fst, agent_snd):
    """Displays both players' basic stats on the screen."""
    Printer.print_ui()
    Printer.print_ui('----- TURN {} ----------------------'.format(turn_number))
    Printer.print_ui('[{}]  HP: {}  PP: {}'.format(agent_fst.name,
                                                   agent_fst.stats['HP'], agent_fst.stats['PP']))
    Printer.print_ui('[{}]  HP: {}  PP: {}'.format(agent_snd.name,
                                                   agent_snd.stats['HP'], agent_snd.stats['PP']))
    Printer.print_ui()


def process_effects(agent_cur):
    """Process all status effects that may affect the current player.

    :param agent_cur: agent (AI instance) that needs to have effects inflicted
    :return: returns a pair of boolean values (will_break, will_continue), stating whether to end
    the battle or skip turn, respectively"""
    will_break, will_skip = False, False
    agent_cur.stats['Defense'] = agent_cur.stats['Base Defense']
    if 'Sleep' in agent_cur.stats['Effects']:
        if 'Focus' in agent_cur.stats['Effects']:
            agent_cur.stats['Effects'].remove('Focus')
        if sing.wakeup():
            Printer.print_ui('  {} wakes up!'.format(agent_cur.name))
            agent_cur.stats['Effects'].remove('Sleep')
            Printer.delay_ui(1)
        else:
            Printer.print_ui('  {} is still asleep. 💤'.format(agent_cur.name))
            will_skip = True
    if 'Poison' in agent_cur.stats['Effects']:
        damage = poison.latent(agent_cur)
        Printer.print_ui('  {} loses {} HP due to Poison! ☠'.format(agent_cur.name, damage))
        agent_cur.stats['HP'] -= damage
        Printer.delay_ui(1)
        if agent_cur.stats['HP'] <= 0:
            will_break = True
    if 'Disable' in agent_cur.stats['Effects']:
        Printer.print_ui('  {} is Disabled.'.format(agent_cur.name))
        Printer.delay_ui(1)
    # Focus not processed here
    return will_break, will_skip


def run_battle(agent_fst, agent_snd):
    """Have two players fight each other."""
    Printer.delay_ui(1)
    Printer.print_ui('============================================================')
    Printer.print_ui('  {} is walking...'.format(agent_fst.name))
    Printer.delay_ui(1)
    Printer.print_ui('        ...a wild {} appears!'.format(agent_snd.name))
    turn_number = 0
    max_turns = 50
    current_player = 2
    # player turns
    while turn_number < max_turns:
        turn_number += 1
        # determine who plays now
        current_player = 3 - current_player
        if current_player == 1:
            agent_cur, agent_oth = agent_fst, agent_snd
        else:
            agent_cur, agent_oth = agent_snd, agent_fst
        # UI
        Printer.delay_ui(1)
        write_stats(turn_number, agent_fst, agent_snd)
        Printer.delay_ui(1)
        # status effects logic
        will_break, will_continue = process_effects(agent_cur)
        if will_break:
            agent_cur = agent_oth
            current_player = 3 - current_player
            break
        if will_continue:
            continue
        # pass status information to current player
        agent_cur.give_stats_info(agent_oth.stats)
        # player makes decision, unless delayed move
        if 'Focus' in agent_cur.stats['Effects']:
            focus.finally_perform(agent_cur, agent_oth)
            if agent_oth.stats['HP'] <= 0:
                break
            else:
                continue
        action, detail = agent_cur.choose_action()
        # process the player's decision
        if action == Action.PERFORM_MOVE:     # use move
            if detail < 0 or detail >= MOVE_COUNT:
                Printer.print_ui(
                    '  {} tries to perform a move, but stumbles!'.format(agent_cur.name))
            else:
                move = MOVES[agent_cur.stats['Moves'][detail]]
                Printer.print_ui('  {} uses {}.'.format(agent_cur.name, move.NAME))
                Printer.delay_ui(1)
                if agent_cur.stats['PP'] < move.PP_COST:
                    Printer.print_ui('  But {} does not have enough PP!'.format(agent_cur.name))
                elif 'Disabled' in agent_cur.stats['Effects'] and move.CAN_DISABLE:
                    Printer.print_ui('  But {} is Disabled!'.format(agent_cur.name))
                else:
                    agent_cur.stats['PP'] -= move.PP_COST
                    agent_cur.stats['Previous move'] = move
                    move.perform(agent_cur, agent_oth)
                    if agent_oth.stats['HP'] <= 0:
                        break
        elif action == Action.USE_ITEM:   # use item
            if detail < 0 or detail >= MAX_ITEMS:
                Printer.print_ui('  {} tries to use an item, but stumbles!'.format(agent_cur.name))
            else:
                item_index = agent_cur.stats['Items'][detail]
                if item_index == -1:
                    Printer.print_ui('  {} tries to use an item, but it\'s not ' \
                             'there!'.format(agent_cur.name))
                else:
                    item = ITEMS[item_index]
                    if item.NAME[0] in ['A', 'E', 'I', 'O', 'U']:
                        Printer.print_ui('  {} uses an {}'.format(agent_cur.name, item.NAME))
                    else:
                        Printer.print_ui('  {} uses a {}.'.format(agent_cur.name, item.NAME))
                    item.use(agent_cur, agent_oth)
                    agent_cur.stats['Items'][detail] = -1
        elif action == Action.BLOCK:   # block
            Printer.print_ui('  {} blocks.'.format(agent_cur.name))
            # temporary increase in Defense
            agent_cur.stats['Defense'] += randint(8, 12)
            # restore 3 to 5 PP
            agent_cur.stats['PP'] = min(agent_cur.stats['Max PP'],
                                        agent_cur.stats['PP'] + randint(3, 5))
        else:
            Printer.print_ui('  {} stumbles!'.format(agent_cur.name))

    Printer.delay_ui(1)
    Printer.print_ui()
    Printer.print_ui()
    Printer.print_ui('  Match over!')
    if agent_fst.stats['HP'] > 0 and agent_snd.stats['HP'] > 0:
        current_player = 0
    Printer.print_ui('============================================================')
    # Printer.print_ui()
    return current_player
