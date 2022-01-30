
# RPG Bot

We are dedicated to making a discord bot
that is used for any TTRPG (Table Top Role Playing Game),
and since we are all facing these troubling times we might find
ourselves playing these games online. So we
decided to make it Easier.

## Current Version

RPG Bot Is Currently In Version (0.1.3), as of
Friday, January 28, 2022.

## Changelog

### Version (0.1.0)

Minimal functionality. Only able to go online
nothing more.

### Version (0.1.1)

Added some admin commands for shutdown functionality.

### Version (0.1.2)

Added dice rolling capability
we use [d20](https://pypi.org/project/d20/) for our dice rolling.

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

### Version (0.1.3)

Now it is Possible to generate new character stats using the -randchar command
