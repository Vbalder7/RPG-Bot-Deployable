
# RPG Bot

We are dedicated to making a discord bot
that is used for any TTRPG (Table Top Role Playing Game),
and since we are all facing these troubling times we might find 
ourselves playing these games online. So we 
decided to make it Easier.




## Current Version
RPG Bot Is Currently In Version (0.1.3), as of 
Friday, January 28, 2022.## Changelog

### Version (0.1.0)

Minimal functionality. Only able to go online
nothing more.

### Version (0.1.1)

Added some admin commands for shutdown functionality.

### Version (0.1.2)

Added dice rolling capability
we use [d20](https://pypi.org/project/d20/) for our dice rolling.

## Operators

| Syntax | Name | Description |
|---|---|---|
| k | keep | Keeps all matched values. |
| p | drop | Drops all matched values. |
| rr | re-roll | Rerolls all matched values until none match. (Dice only) |
| ro | re-role once | Rerolls all matched values once. (Dice only) |
| ra | reroll and add | Rerolls up to one matched value once, keeping the original roll. (Dice only) |
| e | explode on | Rolls another die for each matched value. (Dice only) |
| mi | minimum | Sets the minimum value of each die. (Dice only) |
| ma | maximum | Sets the maximum value of each die. (Dice only) |

## Selectors

| Syntax | Name | Description |
|---|---|---|
| X | literal | All values in this set that are literally this value. |
| hX | highest X | The highest X values in the set. |
| lX | lowest X | The lowest X values in the set. |
| >X | greater than X | All values in this set greater than X. |
| <X | less than X | All values in this set less than X. |

## Unary Operations

| Syntax | Name | Description |
|---|---|---|
| +X | positive | Does nothing. |
| -X | negative | The negative value of X. |

## Examples

```python
>>> r = roll("4d6kh3")  # highest 3 of 4 6-sided dice
>>> r.total
14
>>> str(r)
'4d6kh3 (4, 4, **6**, ~~3~~) = `14`'

>>> r = roll("2d6ro<3")  # roll 2d6s, then reroll any 1s or 2s once
>>> r.total
9
>>> str(r)
'2d6ro<3 (**~~1~~**, 3, **6**) = `9`'

>>> r = roll("8d6mi2")  # roll 8d6s, with each die having a minimum roll of 2
>>> r.total
33
>>> str(r)
'8d6mi2 (1 -> 2, **6**, 4, 2, **6**, 2, 5, **6**) = `33`'

>>> r = roll("(1d4 + 1, 3, 2d6kl1)kh1")  # the highest of 1d4+1, 3, and the lower of 2 d6s
>>> r.total
3
>>> str(r)
'(1d4 (2) + 1, ~~3~~, ~~2d6kl1 (2, 5)~~)kh1 = `3`'
```

### Version (0.1.3)

Now it is Possible to generate new character stats using the -randchar command

### Version (0.1.4)

Added the ability to roll Fate Core dice with `+ = +1` `- = -1` and the empty side is represented as a 0 the syntax is -r fc +mod  ex:`-r fc +3` output ex:`-1, -1, +1, 0, +3`

### Version (0.1.4.dev100)

Added spell lookup command, but the file containing all the spell data is not complete
so you will get a lot of filler text
## Deployment

To deploy this project run

Create a folder in the root directory called `secrets`.
inside there should be a file named `token` with no file extension
inside place your bot token. if you wish to deploy the bot 24/7 on your own
I suggest using heroku as the Procfile,requirements.txt, and runtime.txt are provided.
You need only make a private repository on GitHub add all files to the repository and then build the app with heroku.
once that is done you can go to the resources tab on the heroku dashboard and refresh the page.
then turn on the choice that says bot.py

