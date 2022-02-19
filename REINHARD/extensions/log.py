import hikari
import lightbulb
from REINHARD.data import TOKEN, DEFAULT_GUILD_ID, STDOUT_CHANNEL_ID, Style

log_plugin = lightbulb.Plugin("Log")

#============LOG-MESSAGE============
@log_plugin.listener(hikari.GuildMessageCreateEvent)
async def print_message(event: hikari.GuildMessageCreateEvent) -> None:
   if event.is_bot or not event.content:
      return
   else:
      print(Style.YELLOW + str(event.author) + ' sent ' + event.content)

def load(bot: lightbulb.BotApp) -> None:
   bot.add_plugin(log_plugin)