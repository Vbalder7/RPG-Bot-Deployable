from hikari import Guild
import lightbulb
import d20
import random
import json
from functions import tital

plugin = lightbulb.Plugin('RPG')

#Command to roll dice
@plugin.command
@lightbulb.add_checks(lightbulb.guild_only)
@lightbulb.option('sides', 'sides on the die')
@lightbulb.command('r', 'rolls a set of dice', aliases=("roll", "dice"))
@lightbulb.implements(lightbulb.PrefixCommand)
async def cmd_roll(ctx) -> None:
    sides = ctx.options.sides
    total = d20.roll(sides)
    await ctx.respond(f'{total}',reply=True, mentions_reply=True)

#Command to generate random Character Stats
@plugin.command
@lightbulb.add_checks(lightbulb.guild_only)
@lightbulb.command('randchar', 'rolls stats for a new character')
@lightbulb.implements(lightbulb.PrefixCommand)
async def cmd_randchar(ctx) -> None:
    stats = []
    for i in range(6):
        stat = [random.randint(1,5) for i in range(4)]
        x = stat.index(min(stat))
        stat.pop(x)
        charstat = sum(stat)
        stats.append(charstat)
    await ctx.respond(f"These are your new stats {stats}", reply=True, mentions_reply=True)



def load(bot: lightbulb.BotApp) -> None:
        bot.add_plugin(plugin)
        
def unload(bot: lightbulb.BotApp) -> None:
        bot.remove_plugin(plugin)