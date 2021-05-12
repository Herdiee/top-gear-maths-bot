# Dependencies
import discord
import json


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


    # Suggest Command
    @commands.command(name='suggest',
                      brief='Make a suggestion',
                      description='Suggest things to improve the server',
                      aliases=['suggestion']
                      )
    async def suggest(self, context, *, message):
        # Embed Creation
        imgembed= discord.Embed(
                  title="Suggestion",
                  description=f"{message}"
                  )
        # Set the embed footer to the authors tag and avatar
        imgembed.set_footer(text=f"From {context.author}", icon_url=context.author.avatar_url)
        try:
            image = context.message.attachments[0].url
            imgembed.set_image(url=image)
        except IndexError:
            image = None
        # Send the embed message
        embmessage = await context.send(embed=imgembed)
        # React with tick
        await embmessage.add_reaction("✅")
        # react with X
        await embmessage.add_reaction("❌")


    # Tutor Help
    @commands.command(name='tutor',
                      brief='Ping all tutors',
                      description='Ping all tutors',
                      aliases=['helpers']
                      )
    async def tutor(self, context, *, message):
        # Get the math helper role from the config file
        math_helper = discord.utils.get(context.guild.roles, id=config["tutor_role"])
        # Send the message
        await context.send(f"{math_helper.mention} please help {context.author.mention} with ```{message}```")

def setup(client):
    client.add_cog(Utility(client))