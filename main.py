# Dependencies
import discord
import os
import json
from discord.ext import commands

# Load the config file
with open('./config.json', 'r') as configfile:
    config = json.load(configfile)

intents = discord.Intents.all()
client = commands.Bot(command_prefix = config["prefix"],
                      intents=intents,
                      owner_id = 623905710366785548
                     )


# Load commands
@commands.is_owner()
@client.command(hidden=True)
async def load(ctx, extension):
    try:
        client.load_extension(f'cogs.{extension}')
    except:
        print(f"Something went wrong loading cogs.{extension}")

# Unload commands
@commands.is_owner()
@client.command(hidden=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

# Reload commands
@commands.is_owner()
@client.command(hidden=True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f"Reloaded cogs.{extension}")

# Iterating through files in the cogs directory
for filename in os.listdir('./cogs'):
    # Make sure the file end in .py
    if filename.endswith('.py'):
        # Remove the .py (3 Characters) by splicing
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(config["token"])


