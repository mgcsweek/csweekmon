# csweekmon
Made for [CS Week v5.0](http://www.csnedelja.mg.edu.rs/ "mgcsweek website") in December 2018. This is a simple Python 3 miniproject whose goal is to program very simple AI agents for a [Pokemon](https://www.pokemon.com "Pokemon") style turn based RPG (only for the battle system). It comes with a few default AIs, used mainly for testing purposes.

## Usage

### Running
Just run `game_engine.py`. For example, from the command line:
```bash
python3 game_engine.py
```
This will start a text crawl that shows the progress of the battle.

The only reason why `python3` is used is for more cosmetic features: Unicode characters feature in the text crawl.

### UI Settings
If you want to speed up the text crawl, modify the `delay_ui` function in `utils.py`. If you want to do away with all the text and just get the final scoreboard, set the `VERBOSE_OUTPUT` variable in `utils.py` to `False`.

### Adding your own AI
You will need to create your own strategy in a separate file, for example `<file>.py`. It should look like a class resembling the ones in `strategies.py`. To get your AI to compete in a tournament, simply edit `game_engine.py` and modify it slightly:
 - at the top:
```python
import <file>
```
 - add your class to the `AGENTS` list
If you managed to do this right, your AI will start competing in a tournament the next time you run `game_engine.py`.

## TODO (wish list)
 - Restructure repository into directories (mainly `items` and `moves`).
 - Add a `run.py` containing the main tournament logic, so `game_engine.py` only covers the mechanics of an individual battle and verifies that all the stats are correct.
 - Switch to using command line flags to set UI and battle settings.
 - Add a `Block` action (code 2) that increases `Defense` for the next turn, as well as restores a small amount of `HP` and `PP`.
 - Add a `Disable`/`Stop` move and status effect that prevents the opponent from using 'non-physical' moves, such as `Poison`, `Sing`, `Blast` and similar. It should also be possible to buy an item that heals it.
 - Add a `Human` strategy, where the user controls the battle.
 - Add a `strategy_gen.py`, which would be a standalone application that generates a new strategy class and file.
 - Work on improving overall balance.
 - UI tweaks (possibly settable, and maybe use `ncurses`).
