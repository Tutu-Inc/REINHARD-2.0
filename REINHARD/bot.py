import os
import hikari
import lightbulb
from constants import GITHUB_LINK, TOKEN, DEFAULT_GUILD_ID, STDOUT_CHANNEL_ID

bot = lightbulb.BotApp(
   token = TOKEN,
   prefix = ".",
   intents = hikari.Intents.ALL,
   default_enabled_guilds = DEFAULT_GUILD_ID,
   help_slash_command=True,
   banner=None,
   case_insensitive_prefix_commands=True
)

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event: hikari.GuildMessageCreateEvent) -> None:
   if event.is_bot or not event.content:
      return
   else:
      print(event.content)

@bot.listen(hikari.StartedEvent)
async def on_started(event) -> None:
   channel = await bot.rest.fetch_channel(STDOUT_CHANNEL_ID)
   await channel.send(GITHUB_LINK)
   print("Im started")

@bot.command()
@lightbulb.add_cooldown(5.0, 1, lightbulb.UserBucket)
@lightbulb.option("text", "The thing to say.")
@lightbulb.command("say", "Make the bot say something.")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def cmd_say(ctx: lightbulb.Context) -> None:
   await ctx.respond(ctx.options.text)

bot.load_extensions_from("REINHARD/extensions/", must_exist=True)

def run() -> None:
   if os.name != "nt":
      import uvloop
      uvloop.install()
   bot.run()