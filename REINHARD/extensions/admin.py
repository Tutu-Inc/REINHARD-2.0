

import hikari
import lightbulb
from REINHARD.data.data import Style

from pathlib import Path
EXTENSION_PREFIX = ".".join(Path(__file__).parts[-3:-1]) + "."

admin_plugin = lightbulb.Plugin("Admin")
admin_plugin.description = 'These commands can only be used by the owner.'

#============SHUTDOWN-COMMAND============
@admin_plugin.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("shutdown", "Shut the bot down.", ephemeral=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_shutdown(ctx: lightbulb.SlashContext) -> None:
   await ctx.respond("Now shutting down.")
   await ctx.bot.close()

#============GROUP-EXTENSION-COMMAND============
@admin_plugin.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("extension", "Load, unload and reload extensions.", ephemeral=True)
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def cmd_extension(ctx) -> None:
   pass
#============SUB-EXTENSION-COMMAND============
@cmd_extension.child
@lightbulb.option("name", "The name of the extension.")
@lightbulb.command("load", "Load an extension.", inherit_checks = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cmd_extension_load(ctx: lightbulb.Context) -> None:
   ctx.bot.load_extensions(EXTENSION_PREFIX + ctx.options.name.lower())
   await ctx.respond(f"Loading extension `{ctx.options.name}`.")
   print(Style.YELLOW + str(ctx.author) + ' loaded the extension [' + str(ctx.options.name) + '].')
#============SUB-EXTENSION-COMMAND============ 
@cmd_extension.child
@lightbulb.option("name", "The name of the extension.")
@lightbulb.command("unload", "Unload an extension.", inherit_checks = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cmd_extension_unload(ctx: lightbulb.Context) -> None:
   if ctx.options.name.lower() == "admin":
      await ctx.respond(f"You cannot unload the `{ctx.options.name}` extension!")
      print(Style.RED + str(ctx.author) + ' tried to unload the extension [' + str(ctx.options.name) + '].')
   else:
      ctx.bot.unload_extensions(EXTENSION_PREFIX + ctx.options.name.lower())
      await ctx.respond(f"Unloading extension `{ctx.options.name}`.")
      print(Style.YELLOW + str(ctx.author) + ' unloaded the extension [' + str(ctx.options.name) + '].')
#============SUB-EXTENSION-COMMAND============  
@cmd_extension.child
@lightbulb.option("name", "The name of the extension.")
@lightbulb.command("reload", "Reload an extension.", inherit_checks = True)
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cmd_extension_reload(ctx: lightbulb.Context) -> None:
   ctx.bot.reload_extensions(EXTENSION_PREFIX + ctx.options.name.lower())
   await ctx.respond(f"Reloading extension `{ctx.options.name}`.")
   print(Style.YELLOW + str(ctx.author) + ' reloaded the extension [' + str(ctx.options.name) + '].')


def load(bot: lightbulb.BotApp) -> None:
   bot.add_plugin(admin_plugin)

def unload(bot: lightbulb.BotApp) -> None:
   bot.remove_plugin(admin_plugin)