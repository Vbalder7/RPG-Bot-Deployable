import logging as log

import hikari
import lightbulb as lb

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone,utc
from __init__ import __version__

with open('secrets/token','r',encoding='utf-8') as f:
    token = f.read().strip()
    
bot = lb.BotApp(token = token,
                prefix='$',
                )

scheduler = AsyncIOScheduler()

@bot.listen(lb.CommandErrorEvent)
async def on_error(event: lb.CommandErrorEvent) -> None:
    
    exception = event.exception
    
    if isinstance(exception, lb.NotOwner):
        await event.context.respond("You are not the owner of this bot.")
    elif isinstance(exception, lb.CommandNotFound):
        await event.context.respond("I'm sorry, but I cannot find that command.")
    elif isinstance(exception, lb.NotEnoughArguments):
        await event.context.respond("You have not input all the required arguments.")
    else:
        raise exception

@bot.listen(hikari.StartingEvent)
async def on_starting(event: hikari.StartingEvent) -> None:
    bot.load_extensions_from("extensions")
    
@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartedEvent) -> None:
    scheduler.configure(timezone = utc)
    scheduler.start()
    log.info('BOT READY!')
    
@bot.listen(hikari.StoppingEvent)
async def on_stopping(event: hikari.StoppingEvent) -> None:
    scheduler.shutdown()
    log.info('BOT IS DEAD!')


bot.run(activity=hikari.Activity(
            name=f"RPG Bot | Version = {__version__}",
            type=hikari.ActivityType.WATCHING,
        )
    )