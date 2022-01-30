from contextvars import Context
import lightbulb
import hikari

from __init__ import OWNER_ID

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
        .add_field("Authors",(f"<@{guild.get_member(OWNER_ID)}>"))
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