# Dependencies
import discord
import json
import random


# Additional Dependencies
from discord.ext import commands
from discord_slash import cog_ext, SlashCommand


# Guild ids for slash commands
guild_ids = [840240462039089182]


# Colored Console
import colored
from colored import stylize


# Load the config file
with open('./config.json', 'r') as configfile:
    config = json.load(configfile)


class Utility(commands.Cog):


    def __init__(self, client):
        self.client = client


    # Ping slash command
    @cog_ext.cog_slash(name="ping", guild_ids=guild_ids)
    async def _ping(self, ctx):
        await ctx.send(f"Pong! ({self.client.latency*1000}ms)")

    
    # 8ball slash command
    @cog_ext.cog_slash(name="8ball", guild_ids=guild_ids)
    async def _8ball(self, ctx):
        # Potential Outcomes
        answers = ['It is certain.', 'It is decidedly so.', 'You may rely on it.', 'Without a doubt.',
                   'Yes - definitely.', 'As I see, yes.', 'Most likely.', 'Outlook good.', 'Yes.',
                   'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
                   'Cannot predict now.', 'Concentrate and ask again later.', 'Don\'t count on it.', 'My reply is no.',
                   'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
        # Pick a response
        success = answers[random.randint(0, len(answers))]
        # Embed Creation
        embed = discord.Embed(
            title="**8ball Answer:**",
            description=success,
            color=0xf1c40f
        )
        # Send the message
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Utility(client))