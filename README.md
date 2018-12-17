# csweekmon
Made for [CS Week v5.0](http://www.csnedelja.mg.edu.rs/ "mgcsweek website") in December 2018. This is a simple Python 3 miniproject whose goal is to program very simple AI agents for a [Pokemon](https://www.pokemon.com "Pokemon") style turn based RPG (only for the battle system). It comes with a few default AIs, used mainly for testing purposes.

## Usage

### Running
Just run `run.py`. For example, from the command line:
```bash
python3 run.py
```
This will start a text crawl that shows the progress of the battle.

The only reason why `python3` is used is for more cosmetic features: Unicode characters feature in the text crawl.

You can use the `--no-verbose` flag to suppress most of the output, and `--delay <time>` to change the delay between messages being displayed. For example, to double the speed of the text crawl:
```bash
python3 run.py --delay=0.5
```

### Adding your own AI
You will need to create your own strategy in a separate file, for example `<file>.py`. It should look like a class resembling the ones in `strategies.py`. To get your AI to compete in a tournament, simply edit `run.py` and modify it slightly:
 - at the top:
```python
import <file>
```
 - add your class to the `STRATEGIES` list

You can either adapt the existing code or use the helper `create_strategy.py` program.

If you managed to do this right, your AI will start competing in a tournament the next time you run `run.py`.

