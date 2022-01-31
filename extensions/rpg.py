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
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def cmd_roll(ctx: lightbulb.Context) -> None:
    sides = ctx.options.sides
    total = d20.roll(sides)
    await ctx.respond(f'{total}',reply=True, mentions_reply=True)
    
#Command for rolling Fate Core dice
@cmd_roll.child
@lightbulb.add_checks(lightbulb.guild_only)
@lightbulb.option('op1','',default='')
@lightbulb.command('fc','rolls Fate Core dice')
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def cmd_FC(ctx: lightbulb.Context) -> None:
    
    dice = ['+1','-1','0','+1','-1','0']
    op1 = ctx.options.op1
    x = [random.randint(1,5) for i in range(4)]
    a,b,c,d = x[0], x[1], x[2], x[3]
    if op1 != '':
        totals = (f'{dice[a]}, {dice[b]}, {dice[c]}, {dice[d]}, {op1}')
        await ctx.respond(totals)
    else:
        totals = (f'{dice[a]}, {dice[b]}, {dice[c]}, {dice[c]}')
        await ctx.respond(totals)

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