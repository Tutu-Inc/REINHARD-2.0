import os
import hikari
import lightbulb
from data import TOKEN, DEFAULT_GUILD_ID, STDOUT_CHANNEL_ID, Style

bot = lightbulb.BotApp(
   token = TOKEN,
   prefix = ".",
   intents = hikari.Intents.ALL,
   default_enabled_guilds = DEFAULT_GUILD_ID,
   help_slash_command=True,
   banner=None,
   case_insensitive_prefix_commands=True,
   logs=None
)

#============START-MESSAGE============
@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartedEvent) -> None:
   channel = await bot.rest.fetch_channel(STDOUT_CHANNEL_ID)
   await channel.send(str(bot.get_me().username) + ' is online.')
   print(Style.GREEN + str(bot.get_me()) + ' is online.')

#============ERROR-MESSAGE============
@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
   if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(f"Something went wrong during invocation of command `{event.context.command.name}`.")
        raise event.exception



bot.load_extensions_from("REINHARD/extensions/", must_exist=True)

if __name__ == "__main__":
   if os.name != "nt":
      import uvloop
      uvloop.install()
   bot.run()