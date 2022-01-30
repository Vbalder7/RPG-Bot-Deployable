import lightbulb

plugin = lightbulb.Plugin("Admin")

#Shutdown Command
@plugin.command
@lightbulb.add_checks(lightbulb.owner_only )
@lightbulb.command("shutdown","Gracefully shuts down RPG Bot", aliases = ('sd', 'quit','die'))
@lightbulb.implements(lightbulb.PrefixCommand)
async def shutdown_cmd(ctx) -> None:
    await ctx.respond("Shutting down...")
    await ctx.bot.close()

#Latency Command to see how well the bot is running
@plugin.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("ping", "Get the average latency for the bot.")
@lightbulb.implements(lightbulb.PrefixCommand)
async def cmd_ping(ctx: lightbulb.PrefixContext) -> None:
    await ctx.respond(
        f"Latency: {ctx.bot.heartbeat_latency * 1_000:,.0f} ms."
    )
        
def load(bot: lightbulb.BotApp) -> None:
        bot.add_plugin(plugin)
        
def unload(bot: lightbulb.BotApp) -> None:
        bot.remove_plugin(plugin)