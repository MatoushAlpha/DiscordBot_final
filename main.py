
import discord
from discord.ext import commands
import hf
import json
import os



TOKEN = "ODA3OTQ5MDE1Mjk0NjcyOTQ2.YB_bKA.XVja2MI27JD5Soso6dfTgaDL9Bs"
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():

  print("Bot ready, sir. Beep, boop.")
  await hf.create_user_list()



@client.command()
async def credits(ctx):

  await hf.show_credits(ctx)



@client.command()
@commands.has_permissions(manage_messages = True)
async def quizz(ctx, *, arg):

  await hf.generate_quizz_embed(ctx, arg)


@client.event
async def on_reaction_add(reaction, user):
   
   await hf.store_reaction(reaction, user)


@client.command()
@commands.has_permissions(manage_messages = True)
async def true(ctx):

  await hf.add_points_if_true(ctx)


@client.command()
@commands.has_permissions(manage_messages = True)
async def false(ctx):

  await hf.add_points_if_false(ctx)




client.run(TOKEN)


