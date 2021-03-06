

import hikari
import lightbulb
from REINHARD.data.data import GITHUB_LINK

basic_plugin = lightbulb.Plugin("Basic")
basic_plugin.description = 'These are the basic commands.'

@basic_plugin.command
@lightbulb.add_cooldown(5.0, 1, lightbulb.UserBucket)
@lightbulb.option("text", "The thing to say.")
@lightbulb.command("say", "Make the bot say something.")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_say(ctx: lightbulb.Context) -> None:
   await ctx.respond(ctx.options.text)

@basic_plugin.command
@lightbulb.command("github", "Make the bot send its Github-Link.")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_github(ctx: lightbulb.Context) -> None:
   await ctx.respond(GITHUB_LINK)

def load(bot: lightbulb.BotApp) -> None:
   bot.add_plugin(basic_plugin)
   
def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(basic_plugin)   