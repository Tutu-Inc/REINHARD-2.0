from audioop import add
import os

import hikari
import lightbulb

from REINHARD.constants import MODERATOR_ROLE_NAME, TOKEN, DEFAULT_GUILD_ID, STDOUT_CHANNEL_ID

bot = lightbulb.BotApp(
   token = TOKEN,
   prefix = ".",
   intents = hikari.Intents.ALL,
   default_enabled_guilds = DEFAULT_GUILD_ID,
   help_slash_command=True,
   case_insensitive_prefix_commands=True
)

@bot.listen(hikari.StartedEvent)
async def on_starting(event: hikari.StartedEvent) -> None:
   print("Im starting")

@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartedEvent) -> None:
   channel = await bot.rest.fetch_channel(STDOUT_CHANNEL_ID)
   await channel.send("online")
   print("Im started")

@bot.command()
@lightbulb.add_cooldown(5.0, 1, lightbulb.UserBucket)
#@lightbulb.add_checks(lightbulb.owner_only, lightbulb.has_roles(601422939765604400))
@lightbulb.option("text", "The thing to say.")
@lightbulb.command("say", "Make the bot say something.")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_say(ctx: lightbulb.SlashContext) -> None:
   await ctx.respond(ctx.options.text)

def run() -> None:
   if os.name != "nt":
      import uvloop
      uvloop.install()
   bot.run()

    
