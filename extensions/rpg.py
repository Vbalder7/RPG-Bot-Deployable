# Copyright (c) 2022, Vbalder7
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import json
import random

import d20
import lightbulb
import requests
from hikari import Guild

from functions import tital

plugin = lightbulb.Plugin('RPG')

# Command to roll dice


@plugin.command
@lightbulb.add_checks(lightbulb.guild_only)
@lightbulb.option('sides', 'sides on the die')
@lightbulb.command('r', 'rolls a set of dice', aliases=("roll", "dice"))
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def cmd_roll(ctx: lightbulb.Context) -> None:
    sides = ctx.options.sides
    total = d20.roll(sides)
    await ctx.respond(f'{total}', reply=True, mentions_reply=True)

# Command for rolling Fate Core dice


@cmd_roll.child
@lightbulb.add_checks(lightbulb.guild_only)
@lightbulb.option('op1', '', default='')
@lightbulb.command('fc', 'rolls Fate Core dice')
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def cmd_FC(ctx: lightbulb.Context) -> None:

    dice = ['+1', '-1', '0', '+1', '-1', '0']
    op1 = ctx.options.op1
    x = [random.choices(dice, k=4)]
    if op1 != '':
        totals = (",".join(f'{i}' for i in x) + op1)
        await ctx.respond(totals)
    else:
        totals = (",".join(f'{i}' for i in x))
        await ctx.respond(totals, reply=True, mentions_reply=True)

# Command to generate random Character Stats


@plugin.command
@lightbulb.add_checks(lightbulb.guild_only)
@lightbulb.command('randchar', 'rolls stats for a new character')
@lightbulb.implements(lightbulb.PrefixCommand)
async def cmd_randchar(ctx) -> None:
    stats = []
    for i in range(6):
        stat = [random.randint(1, 5) for i in range(4)]
        x = stat.index(min(stat))
        stat.pop(x)
        charstat = sum(stat)
        stats.append(charstat)
    await ctx.respond(f"These are your new stats {stats}", reply=True, mentions_reply=True)


@plugin.command
@lightbulb.add_checks(lightbulb.guild_only)
@lightbulb.option('op5', '', default='')
@lightbulb.option('op4', '', default='')
@lightbulb.option('op3', '', default='')
@lightbulb.option('op2', '', default='')
@lightbulb.option('op1', '', default='')
@lightbulb.command('spell', 'Finds spell info')
@lightbulb.implements(lightbulb.PrefixCommand)
async def spell_lookup(ctx) -> None:

    # defining variables with the input for the command
    options = [ctx.options.op1,
               ctx.options.op2,
               ctx.options.op3,
               ctx.options.op4,
               ctx.options.op5]

    with open('resources/json/srd_api.json', 'r') as f:
        info = json.load(f)

    # Concatenating all variables into one readable spell name and formating it
    spellName = (" ".join(f'{i}' for i in options))

    spellName = spellName.strip()

    # base url for the spell api
    base = 'https://www.dnd5eapi.co'

    # Titalize function breaks with single word spells so we check for multiple spaces
    # indicating multile words
    if spellName.count(' ') > 1:
        name = tital.titalize(spellName)
    else:
        name = spellName.title()

    # For loop to check if the spell that was input matches a spell in the api
    for spell in info['results']:

        if name == spell['name']:
            endpoint = spell['url']
            url = (f'{base}{endpoint}')
            response = requests.get(url)
            new_str = json.loads(response.text)

            with open('resources/json/temp_spell_file.json', 'w') as g:
                json.dump(new_str, g, indent=4)

            with open('resources/json/temp_spell_file.json', 'r') as h:
                spell_info = json.load(h)

            spellBlock = (f"""\n
`Spell Name`: **{spell_info['name']}**
`Base Level`: *{spell_info['level']}*
`Components`: *{spell_info['components']}*
`Spell Description`: *{spell_info['desc'][0]}*
`Range`: __***{spell_info['range']}***__
`Casting Time`: __***{spell_info['casting_time']}***__
`Duration`: __***{spell_info['duration']}***__
`School`: {spell_info['school']['name']}
`Concentration`: *{spell_info['concentration']}*
""")
            await ctx.respond(spellBlock)


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)
