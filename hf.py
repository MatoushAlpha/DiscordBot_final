

import discord 
from discord.ext import commands
import json
import os



async def create_user_list():

  with open("data.json", "r") as f:
    users = json.load(f)

    users["id_list"] = []

  with open("data.json", "w") as f:
    json.dump(users, f)




async def generate_quizz_embed(ctx, arg):

  embed = discord.Embed(title = arg, description = "True or false?")
  embed.set_author(name = "quizz")

  message = await ctx.send(embed = embed)
  await message.add_reaction("✅")
  await message.add_reaction("❎")




async def store_reaction(reaction, user):

  with open("data.json", "r") as f:
    users = json.load(f)

  if str(user.id) in users:
    users[str(user.id)]["last_reaction"] = str(reaction)

  else:
    users["id_list"].append(str(user.id))
    users[str(user.id)] = {}
    users[str(user.id)]["credits"] = 100
    users[str(user.id)]["last_reaction"] = str(reaction)

  with open("data.json", "w") as f:
    json.dump(users, f)





async def add_points_if_true(ctx):

  with open("data.json", "r") as f:
    users = json.load(f)

  max = len(users["id_list"])

  for x in range(0, max):

    user_id = users["id_list"][x]

    if users[user_id]["last_reaction"] == "\u2705":
      users[user_id]["credits"] += 0.1 * users[user_id]["credits"]

  with open("data.json", "w") as f:
    json.dump(users, f)




async def add_points_if_false(ctx):

  with open("data.json", "r") as f:
    users = json.load(f)

  max = len(users["id_list"])

  for x in range(0, max):

    user_id = users["id_list"][x]

    if users[user_id]["last_reaction"] == "\u274e":
      users[user_id]["credits"] += 0.1 * users[user_id]["credits"]

  with open("data.json", "w") as f:
    json.dump(users, f)



async def show_credits(ctx):

  user = ctx.author

  with open("data.json", "r") as f:
    users = json.load(f)

  if str(user.id) in users:
    pass

  else:
    users["id_list"].append(str(user.id))
    users[str(user.id)] = {}
    users[str(user.id)]["credits"] = 100
    
  credits_amount = users[str(user.id)]["credits"]

  embed = discord.Embed(title = f"{user.name}'s balance")
  embed.add_field(name = credits_amount, value = "credits")

  await ctx.send(embed = embed)

  with open("data.json", "w") as f:
    json.dump(users, f)
