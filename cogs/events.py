# Dependencies
import discord
import json
from discord.ext import commands


# Colored Terminal
import colored
from colored import stylize


# Load the config file
with open('./config.json', 'r') as configfile:
    config = json.load(configfile)


class Events(commands.Cog):


    def __init__(self, client):
        self.client = client


    # Event triggered when the bot is online
    @commands.Cog.listener()
    async def on_ready(self):
        # Set the bots status
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=config["activity"]))
        # Print that the bot is online
        print('Bot is online.')


    # Event triggered when a member joins
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # DM Embed Creation
        embed = discord.Embed(
            title="**Welcome Message",
            description="Welcome to Top Gear Maths Shed! We hope you enjoy your stay :D",
            color=0x2ecc71
            )
        # Set the DM embed thumbnail to the users avatar
        embed.set_thumbnail(url = member.avatar_url)
        # Send the welcome embed to the users DMS
        await member.send(embed=embed)
        # Get the welcome channel from the config
        general = self.client.get_channel(config["welcome_channel"])
        # Send the welcome message 
        await general.send(member.mention + ' has joined the server B)')


    # Event triggered when a member leaves
    @commands.Cog.listener()   
    async def on_member_remove(self, member):
        # Get the leave channel from the config
        welcome = self.client.get_channel(config["welcome_channel"])
        # Send the leave message
        await welcome.send(member.mention + " has left the server B(")


def setup(client):
    client.add_cog(Events(client))
    