#Copyright (c) 2022, Vbalder7
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#3. Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from contextvars import Context
import lightbulb
import hikari
from config import Config


plugin = lightbulb.Plugin("Info")

@plugin.command
@lightbulb.command('info','Gives info about the bot', aliases=('i','details'))
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def info_group(ctx: lightbulb.Context) -> None:
    if not (guild := ctx.get_guild()):
        return

    if not (me := guild.get_my_member()):
        return

    if not (member := ctx.member):
        return

    await ctx.respond(
        hikari.Embed(
            title="About RPG Bot",
            description="""We are dedicated to making a discord bot
that is used for any TTRPG (Table Top Role Playing Game),
and since we are all facing these troubling times we might find
ourselves playing these games online. So we
decided to make it Easier."""
        )
        .set_thumbnail(me.avatar_url)
        .set_author(name="Information")
        .set_footer(f"Requested by {member.display_name}", icon=member.avatar_url)
        .add_field("Source Code","<https://github.com/Vbalder7/RPG-Bot>")
        .add_field("Authors",(f"<@{Config.OWNER_ID}>"))
        .add_field(
            "License",
            '[BSD 3-Clause "New" or "Revised" License]'
            f"(https://github.com/Vbalder7/RPG-Bot/blob/main/LICENSE)",
        )
    )

@info_group.child
@lightbulb.command('bots', 'gives info about the bots in RPG Haven')
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def bot_info(ctx: lightbulb.Context) -> None:
    await ctx.respond(f""">>> Prefix for RPG Bot: -
Prefix for Dyno Bot: !
Prefix for Rythm: ?
Prefix for D&D Vault: /
                      """)

@info_group.child
@lightbulb.command('game','Gives info for current game')
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def camp_info(ctx: lightbulb.Context) -> None:
    title = "   __*** \"Princes of the Apocalypse\"***__"
    ent_summary =f"""
    {title.center(50)}
    >>> ```Abolish an ancient evil threatening devastation
in this adventure for the world's greatest roleplaying game!
Called by the Elder Elemental Eye to serve,
four corrupt prophets have risen from the depths of anonymity
to claim mighty weapons with direct links to the power of the elemental princes.
Each of these prophets has assembled a cadre of cultists and creatures to serve
them in the construction of four elemental temples of lethal design.
It is up to adventurers from heroic factions such as the Emerald Enclave 
and the Order of the Gauntlet to discover where the true power of each prophet lay,
and dismantle it before it comes boiling up to obliterate the Realms.``` """
    await ctx.respond(ent_summary)

def load(bot: lightbulb.BotApp) -> None:
        bot.add_plugin(plugin)
        
def unload(bot: lightbulb.BotApp) -> None:
        bot.remove_plugin(plugin)