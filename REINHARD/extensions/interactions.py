

import hikari
import lightbulb

interactions_plugin = lightbulb.Plugin("Interactions")
interactions_plugin.description = 'These are interaction commands.'

@interactions_plugin.command
@lightbulb.add_cooldown(5.0, 1, lightbulb.UserBucket)
@lightbulb.command("count", "Plants a simple counter.")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_count(ctx: lightbulb.Context) -> None:
   button_menue = (
      ctx.bot.rest.build_action_row()
      .add_button(hikari.ButtonStyle.PRIMARY, "count_button")
      .set_label("+1")
      .add_to_container()
   ) 
   count = 0 
   await ctx.respond("Count: 0", component=button_menue)
   while True:
      try:
         event = await ctx.bot.wait_for(hikari.InteractionCreateEvent, timeout=60)
      except:
         pass
      else:
         count += 1
         await event.interaction.create_initial_response(
            hikari.ResponseType.MESSAGE_UPDATE,
            f"Count: {count:,}"
         )

  
def load(bot: lightbulb.BotApp) -> None:
   bot.add_plugin(interactions_plugin)

def unload(bot: lightbulb.BotApp) -> None:
   bot.remove_plugin(interactions_plugin)
         