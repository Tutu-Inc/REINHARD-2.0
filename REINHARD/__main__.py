import os

import hikari
import lightbulb
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import timezone, utc

from REINHARD.constants import TOKEN, GUILD_ID, STDOUT_CHANNEL_ID

bot = lightbulb.BotApp(
    token = TOKEN,
    prefix = ".",
    intents = hikari.Intents.ALL,
    default_enabled_guilds = GUILD_ID,
    help_slash_command=True,
    case_insensitive_prefix_commands=True
)
bot.d.scheduler = AsyncIOScheduler()
bot.d.scheduler.configure(timezone=utc)


@bot.listen(hikari.StartedEvent)
async def on_starting(event: hikari.StartedEvent) -> None:
    print("Im starting")

@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartedEvent) -> None:
    channel = await bot.rest.fetch_channel(STDOUT_CHANNEL_ID)
    await channel.send("online")
    print("Im started")
    
if __name__ == "__main__":
    if os.name != "nt":
        import uvloop
        uvloop.install()
         
bot.run()
