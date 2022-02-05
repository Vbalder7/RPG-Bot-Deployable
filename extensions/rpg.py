import lightbulb,d20,random,json
from functions import tital
from hikari import Guild

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

@plugin.command
@lightbulb.add_checks(lightbulb.guild_only)
@lightbulb.option('op5','',default='')
@lightbulb.option('op4','',default='')
@lightbulb.option('op3','',default='')
@lightbulb.option('op2','',default='')
@lightbulb.option('op1','',default='')
@lightbulb.command('spell', 'Finds spell info')
@lightbulb.implements(lightbulb.PrefixCommand)
async def spell_lookup(ctx) -> None:
    op1,op2,op3,op4,op5 = [ctx.options.op1,
                           ctx.options.op2,
                           ctx.options.op3,
                           ctx.options.op4,
                           ctx.options.op5]
    with open('resources/json/spells.json', 'r') as f:
        info = json.load(f)
    spellName = (f'{op1} {op2} {op3} {op4} {op5}')
    spellName = spellName.strip()
    spellName = tital.titalize(spellName)
    for spell in info['spells']:
        if spell['name'] == spellName:
            spellBlock = (f"""\n
`Spell Name`: **{spell['name']}**
`Source Book`: __***{spell['source']}***__
`Base Level`: *{spell['level']}*
`Spell Description`: *{spell['desc']}*
`Range`: __***{spell['range']}***__
`Casting Time`: __***{spell['casting_time']}***__
`Duration`: __***{spell['duration']}***__
`School`: {spell['school']}
`Spell Classes`: *{spell['class']}*

""")
            await ctx.respond(spellBlock)

def load(bot: lightbulb.BotApp) -> None:
        bot.add_plugin(plugin)
        
def unload(bot: lightbulb.BotApp) -> None:
        bot.remove_plugin(plugin)