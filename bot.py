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

import logging as log

import hikari
import lightbulb as lb
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone, utc

from config import Config


def App() -> None:

    bot = lb.BotApp(token=Config.TOKEN,
                    owner_ids=Config.OWNER_ID,
                    default_enabled_guilds=Config.GUILD_ID,
                    prefix='$',
                    case_insensitive_prefix_commands=True
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
        scheduler.configure(timezone=utc)
        scheduler.start()
        log.info('BOT READY!')

    @bot.listen(hikari.StoppingEvent)
    async def on_stopping(event: hikari.StoppingEvent) -> None:
        scheduler.shutdown()
        log.info('BOT IS DEAD!')

    bot.run(activity=hikari.Activity(
            name=f"$help|Version={Config.VERSION}",
            type=hikari.ActivityType.WATCHING,
            )
            )
