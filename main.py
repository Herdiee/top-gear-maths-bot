import discord      # API Wrapper
import os           # Required for cogs
import json         # Parse JSON Config file

from discord.ext import commands            # Discord Commands
from discord_slash import SlashCommand      # Discord Slash Commands

with open('./config.json', 'r') as configfile:      # Load config file
    config = json.load(configfile)

intents = discord.Intents.all()     # Bot requires intents

client = commands.Bot(command_prefix = config["prefix"],    # Use Prefix from Config
                      intents=intents,                      # Intents defined earlier
                      owner_id = 623905710366785548         # Owner ID
                     )

slash = SlashCommand(client, sync_commands=True)    # Create slash commands

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

for filename in os.listdir('./cogs'):                   # Iterate through cogs directory
    if filename.endswith('.py'):                        # Check that file ends in py
        client.load_extension(f'cogs.{filename[:-3]}')  # Strip file extension

client.run(config["token"]) # Use bot token to log in