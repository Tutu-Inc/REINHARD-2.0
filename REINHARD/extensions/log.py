

import hikari
import lightbulb
from REINHARD.data.data import TOKEN, DEFAULT_GUILD_ID, STDOUT_CHANNEL_ID, Style

log_plugin = lightbulb.Plugin("Log")
log_plugin.description = 'These are the log commands.'

#============LOG-MESSAGE============
@log_plugin.listener(hikari.GuildMessageCreateEvent)
async def print_message(event: hikari.GuildMessageCreateEvent) -> None:
   if event.is_bot or not event.content:
      return
   else:
      print(Style.CYAN + str(event.author) + ' sent "' + str(event.content) + '" in channel [' + str(event.channel_id) + '].')

def load(bot: lightbulb.BotApp) -> None:
   bot.add_plugin(log_plugin)
   
def unload(bot: lightbulb.BotApp) -> None:
   bot.remove_plugin(log_plugin)  